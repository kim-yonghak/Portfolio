import csv
import time
import os
import sys
import subprocess
import re

def get_installed_packages(keyword):
    pm_list_output = execute_adb_command("pm list packages")
    package_names = [p.split(":")[1].strip() for p in pm_list_output.split('\n') if keyword in p]
    return package_names

def get_pid(package_name):
    #cmd = f"ps | grep '{package_name}$' | awk '{{print $2}}'"
    cmd = f"ps | grep '{package_name}$' | tr -s ' ' | cut -d' ' -f2"#8이하 버전 기준(awk 작동안함)
    pid_output = execute_adb_command(cmd)
    if not pid_output:
        return None
    return pid_output.strip()

def execute_adb_command(cmd: str, raise_on_error: bool = False) -> str:
    adb_command = ["adb", "shell"] + cmd.split()
    try:
        adb_command_output = subprocess.check_output(adb_command)
        return adb_command_output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        if raise_on_error:
            raise
        else:
            print(f"Error: {str(e)}")
            return ""

def get_cpu_usage01(package_name, pid):
    top_output = execute_adb_command(f"top -n 1 | grep {pid}")

    print(f"CPU시작")  # Debugging line
    print(top_output)  # Debugging line
    print("CPU종료")  # Debugging line
    
    for line in top_output.splitlines():#8버전 이상 작동확인
        if str(pid) in line:
            cpu_stat = line.strip().split()[8].replace('%', '')
            try:
                return float(cpu_stat)
            except ValueError:
                return None

def get_cpu_usage02(package_name, pid):
    #top_output = execute_adb_command(f"top -n 1 | grep {pid}")
    top_output = execute_adb_command(f"top -n 1")#7버전 기준
    for line in top_output.splitlines():
        if pid in line:
            top_output = line

    print(f"CPU시작")  # Debugging line
    print(top_output)  # Debugging line
    print("CPU종료")  # Debugging line

    cpu_stat = top_output.split()[4].replace('%', '')#7버전 기준
    return float(cpu_stat)
    
    #for line in top_output.splitlines():#8버전 이상 작동확인
        #if str(pid) in line:
            #cpu_stat = line.strip().split()[8].replace('%', '')
            #try:
            #    return float(cpu_stat)
            #except ValueError:
            #    return None

def get_mem_usage(package_name):
    mem_output = execute_adb_command(f"dumpsys meminfo {package_name}").splitlines()
    print(f"MEM시작")  # Debugging line
    print(mem_output)  # Debugging line
    print("MEM종료")  # Debugging line
    mem_usage = ""
    for line in mem_output:
        if 'TOTAL' in line:
            mem_usage = line.split()[1]
            break
    return int(mem_usage) if mem_usage else 0

def get_cpu_temperature():
    try:
        temp_path = "/sys/devices/virtual/thermal/thermal_zone3/temp"
        #temp_path = "/sys/class/thermal/thermal_zone0/temp"
        cpu_temp = execute_adb_command(f"cat {temp_path}")
        print(f"TEM시작")  # Debugging line
        print(cpu_temp)  # Debugging line
        print("TEM종료")  # Debugging line
        return float(cpu_temp) / 1000.0

    except ValueError:
        return 0  # 측정할 수 없는 경우 온도를 0으로 반환합니다.

def get_battery_temperature():
    battery_temp = execute_adb_command("dumpsys battery | grep temperature").split()[1]
    return int(battery_temp) / 10.0


#def get_fps_surface_flinger(package_name: str):#표면 데이터 노출 코드
    #fps_output = execute_adb_command("dumpsys SurfaceFlinger --latency")
    #print(f"FPS시작")  # Debugging line
    #print(fps_output)  # Debugging line
    #print("FPS종료")  # Debugging line

    #return 0

def get_fps_surface_flinger01(package_name: str):
    cmd = f"dumpsys gfxinfo {package_name} framestats"
    fps_output = execute_adb_command(cmd)
    print(f"FPS시작")  # Debugging line
    print(fps_output)  # Debugging line
    print("FPS종료")  # Debugging line

    lines = fps_output.split('\n')
    for line in lines:
        if 'Total frames rendered' in line:
            values = re.findall(r'\d+', line.strip())
            total = int(values[0])
            #print(total)
    
    frame_values = []
    
    # '---PROFILEDATA---'로 시작해서 '---PROFILEDATA---'로 끝나는 부분을 추출
    profile_data_pattern = re.compile(r'---PROFILEDATA---(.*?)---PROFILEDATA---', re.DOTALL)
    profile_data_match = profile_data_pattern.search(fps_output)

    if profile_data_match:
        profile_data_text = profile_data_match.group(1).strip()
        # 각 줄로 나누기
        lines = profile_data_text.split('\n')
        
        for line in lines:
            values = re.findall(r'\d+', line)
            if len(values) >= 22:
                if(values[0] == '0'): #flag 값이 1만 뜰 경우 이 부분 주석처리 필요
                    temp = int(values[16])-int(values[2])#11이상 버전
                    #print(line)  # Debugging line
                    #print(f"끝")  # Debugging line
                    #print(f'{temp}')  # Debugging line
                    if(temp > 0):
                        frame_values.append(temp)
                        
        if len(frame_values) == 0:
            return 0
 
    # 결과 출력
    #print("Frame Values:",frame_values)  # Debugging line

    # FPS 계산
    #sub = ((sum(frame_values) / len(frame_values)) / 1000000000)
    #print(sub)  # Debugging line
    #temp = total / sub
    temp = 1000000000 / (sum(frame_values) / len(frame_values))
    fps = round(temp,2)
    
    return fps

def get_fps_surface_flinger02(package_name: str):
    cmd = f"dumpsys gfxinfo {package_name} framestats"
    fps_output = execute_adb_command(cmd)
    print(f"FPS시작")  # Debugging line
    print(fps_output)  # Debugging line
    print("FPS종료")  # Debugging line

    lines = fps_output.split('\n')
    for line in lines:
        if 'Total frames rendered' in line:
            values = re.findall(r'\d+', line.strip())
            total = int(values[0])
            #print(total)
    
    frame_values = []
    
    # '---PROFILEDATA---'로 시작해서 '---PROFILEDATA---'로 끝나는 부분을 추출
    profile_data_pattern = re.compile(r'---PROFILEDATA---(.*?)---PROFILEDATA---', re.DOTALL)
    profile_data_match = profile_data_pattern.search(fps_output)

    if profile_data_match:
        profile_data_text = profile_data_match.group(1).strip()
        # 각 줄로 나누기
        lines = profile_data_text.split('\n')
        
        for line in lines:
            values = re.findall(r'\d+', line)
            if len(values) >= 15:
                if(values[0] == '0'): #flag 값이 1만 뜰 경우 이 부분 주석처리 필요
                    temp = int(values[13])-int(values[1])#11미만 버전
                    #print(line)  # Debugging line
                    #print(f"끝")  # Debugging line
                    #print(f'{temp}')  # Debugging line
                    if(temp > 0):
                        frame_values.append(temp)

        if len(frame_values) == 0:
            return 0
        
    temp = 1000000000 / (sum(frame_values) / len(frame_values))
    fps = round(temp,2)
    
    return fps

def get_fps_surface_flinger03(package_name: str):
    cmd = f"dumpsys gfxinfo {package_name} framestats"
    fps_output = execute_adb_command(cmd)
    print(f"FPS시작")  # Debugging line
    print(fps_output)  # Debugging line
    print("FPS종료")  # Debugging line

    lines = fps_output.split('\n')
    for line in lines:
        if 'Total frames rendered' in line:
            values = re.findall(r'\d+', line.strip())
            total = int(values[0])
            #print(total)
    
    frame_values = []
    
    # '---PROFILEDATA---'로 시작해서 '---PROFILEDATA---'로 끝나는 부분을 추출
    profile_data_pattern = re.compile(r'---PROFILEDATA---(.*?)---PROFILEDATA---', re.DOTALL)
    profile_data_match = profile_data_pattern.search(fps_output)

    if profile_data_match:
        profile_data_text = profile_data_match.group(1).strip()
        # 각 줄로 나누기
        lines = profile_data_text.split('\n')
        
        for line in lines:
            values = re.findall(r'\d+', line)
            if len(values) >= 13:
                if(values[0] == '0'): #flag 값이 1만 뜰 경우 이 부분 주석처리 필요
                    temp = int(values[13])-int(values[1])#7 버전
                    #print(line)  # Debugging line
                    #print(f"끝")  # Debugging line
                    #print(f'{temp}')  # Debugging line
                    if(temp > 0):
                        frame_values.append(temp)

        if len(frame_values) == 0:
            return 0

    temp = 1000000000 / (sum(frame_values) / len(frame_values))
    fps = round(temp,2)
    
    return fps

def write_to_csv(file_name, headers, data):
    file_exists = os.path.isfile(file_name)
    with open(file_name, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(headers)
        writer.writerow(data)

# 이전 함수들...

if __name__ == "__main__":
    OS = input("\nInput Os Ver(ex 11): ")
    keyword = input("\nInput Package Developer(ex smilegate): ")

    print("Installed packages:")
    package_names = get_installed_packages(keyword)
    print("\n".join(package_names))

    package_name = input("\nChoose a package from the list: ")

    pid = get_pid(package_name)

    if not pid:
        print("Could not find a process ID for the given package. Make sure the app is running.")
        sys.exit(1)

    print(f"App's PID: {pid}")
    pid = input("Enter PID:")

    run_date = time.strftime("%Y-%m-%d", time.localtime())

    csv_filename = f"{package_name}_performance_data_{run_date}.csv"
    header_row = ['timestamp', 'cpu_usage', 'memory_usage', 'cpu_temperature', 'battery_temperature', 'fps']

    if(int(OS) >= 11):
        with open(csv_filename, mode="a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header_row)
            if not os.stat(csv_filename).st_size > 0:
                writer.writeheader()
            
            # Start the loop within the 'with' statement block
            start_time = time.time()
            interval = 1 # 1 second interval
            while time.time() - start_time < 60 * 1: # 시간 조절(단위 : 초)
                current_time = time.time()

                cpu_usage = get_cpu_usage01(package_name, pid)
                mem_usage = get_mem_usage(package_name)
                # Get CPU temperature
                cpu_temperature = get_cpu_temperature()
                battery_temperature = get_battery_temperature()
                fps = get_fps_surface_flinger01(package_name)
                print(f"FPS: {fps}")  # Debugging line
                print(f"CPU_usage: {cpu_usage}")  # Debugging line
                print(f"MEM_usage: {mem_usage}")  # Debugging line
                print(f"CPU_temp: {cpu_temperature}")  # Debugging line
                print(f"BAT_temp: {battery_temperature}")  # Debugging line

                # Write data to the file
                writer.writerow({
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "cpu_usage": cpu_usage,
                    "memory_usage": mem_usage,
                    "cpu_temperature": cpu_temperature,
                    "battery_temperature": battery_temperature,
                    "fps": fps
                })
                # Calculate how long the operations took and subtract that from the sleep time
                elapsed_time = time.time() - current_time
                sleep_duration = max(interval - elapsed_time, 0)
                time.sleep(sleep_duration)

    if(int(OS) >= 8):
        with open(csv_filename, mode="a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header_row)
            if not os.stat(csv_filename).st_size > 0:
                writer.writeheader()
            
            # Start the loop within the 'with' statement block
            start_time = time.time()
            interval = 1 # 1 second interval
            while time.time() - start_time < 60 * 1: # 시간 조절(단위 : 초)
                current_time = time.time()

                cpu_usage = get_cpu_usage01(package_name, pid)
                mem_usage = get_mem_usage(package_name)
                # Get CPU temperature
                cpu_temperature = get_cpu_temperature()
                battery_temperature = get_battery_temperature()
                fps = get_fps_surface_flinger02(package_name)
                print(f"FPS: {fps}")  # Debugging line
                print(f"CPU_usage: {cpu_usage}")  # Debugging line
                print(f"MEM_usage: {mem_usage}")  # Debugging line
                print(f"CPU_temp: {cpu_temperature}")  # Debugging line
                print(f"BAT_temp: {battery_temperature}")  # Debugging line

                # Write data to the file
                writer.writerow({
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "cpu_usage": cpu_usage,
                    "memory_usage": mem_usage,
                    "cpu_temperature": cpu_temperature,
                    "battery_temperature": battery_temperature,
                    "fps": fps
                })
                # Calculate how long the operations took and subtract that from the sleep time
                elapsed_time = time.time() - current_time
                sleep_duration = max(interval - elapsed_time, 0)
                time.sleep(sleep_duration)

    if(int(OS) <= 7):
        with open(csv_filename, mode="a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header_row)
            if not os.stat(csv_filename).st_size > 0:
                writer.writeheader()
            
            # Start the loop within the 'with' statement block
            start_time = time.time()
            interval = 1 # 1 second interval
            while time.time() - start_time < 60 * 1: # 시간 조절(단위 : 초)
                current_time = time.time()

                cpu_usage = get_cpu_usage02(package_name, pid)
                mem_usage = get_mem_usage(package_name)
                # Get CPU temperature
                cpu_temperature = get_cpu_temperature()
                battery_temperature = get_battery_temperature()
                fps = get_fps_surface_flinger03(package_name)
                print(f"FPS: {fps}")  # Debugging line
                print(f"CPU_usage: {cpu_usage}")  # Debugging line
                print(f"MEM_usage: {mem_usage}")  # Debugging line
                print(f"CPU_temp: {cpu_temperature}")  # Debugging line
                print(f"BAT_temp: {battery_temperature}")  # Debugging line

                # Write data to the file
                writer.writerow({
                    "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                    "cpu_usage": cpu_usage,
                    "memory_usage": mem_usage,
                    "cpu_temperature": cpu_temperature,
                    "battery_temperature": battery_temperature,
                    "fps": fps
                })
                # Calculate how long the operations took and subtract that from the sleep time
                elapsed_time = time.time() - current_time
                sleep_duration = max(interval - elapsed_time, 0)
                time.sleep(sleep_duration)
