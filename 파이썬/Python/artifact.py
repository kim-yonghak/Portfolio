import random

indexes = [0] * 78
indexes_check = [0] * 78

# 총 돌릴 반복문의 수
num_repeats = 1000

count_list = []
countFinish_list = []
index_list = []

for _ in range(num_repeats):
    # 한번 돌릴 때 마다 필요한 뽑기의 수
    count = 0
    repeat_check = 0
    first_run = 0

    while repeat_check == 0:
        i = random.randint(0, 77)

        indexes[i] += 1

        count += 1

        if indexes[i] == 75:
            indexes_check[i] = 1
            if first_run == 0:
                count_list.append(count)
                sum_index = sum(indexes)
                index_list.append(sum_index/78)
                first_run = 1

        j_check = 0
        for j in range(78):
            if indexes_check[j] == 1:
                j_check += 1
                if j_check == 78:
                    countFinish_list.append(count)
                    repeat_check = 1

    indexes = [0] * 78
    indexes_check = [0] * 78

avg_count = sum(count_list) / num_repeats

avg_countFinish = sum(countFinish_list) / num_repeats

avg_index = sum(index_list) / num_repeats

print("유물 한개를 전설을 찍기 위해 필요한 평균 뽑기의 수:", avg_count)
print("이 때 유물들의 평균 갯수:", avg_index)
print("유물 전부를 전설을 찍기 위해 필요한 평균 뽑기의 수:", avg_countFinish)

