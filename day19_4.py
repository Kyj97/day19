def data_sort(list):
    l = len(list)
    for i in range(0, l):
        for j in range(i + 1, l):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def get_median(a):
    a_len = len(a)
    if (a_len == 0): return None
    a_center = int(a_len / 2)
    return a[a_center]



data = [[55, 33, 250, 44], [88, 1, 67, 23], [199, 222, 38, 47], [155, 145, 20, 99]]
data1 = []

for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        data1.append(data[i][j])

print(f'1차원 변경 후, 정렬 전 -> {data1}')
data_sort(data1)
print(f'1차원 변경 후, 정렬 후 -> {data1}')
print(f'중앙값 -> {get_median(data1)}')
