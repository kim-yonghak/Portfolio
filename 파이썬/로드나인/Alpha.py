import subprocess

def get_connected_devices():
    """연결된 모든 안드로이드 기기 리스트 가져오기"""
    result = subprocess.run(["adb", "devices"], capture_output=True, text=True)
    devices = result.stdout.strip().split("\n")[1:]  # 첫 줄 제거
    device_list = [line.split("\t")[0] for line in devices if "device" in line]
    return device_list

devices = get_connected_devices()
print("연결된 장치:", devices)
