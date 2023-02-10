import random
import time


def select_sort(list):
    l = len(list)
    for i in range(0, l):
        for j in range(i + 1, l):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def quick_sort(list, start, end):
    if end <= start+






        :
        return

    low = start
    high = end
    pivot = list[(low + high) // 2]

    while low <= high:
        while list[low] < pivot:
            low = low + 1
        while list[high] > pivot:
            high = high - 1
        if low <= high:
            list[low], list[high] = list[high], list[low]
            low = low + 1
            high = high - 1

    mid = low
    quick_sort(list, start, mid - 1)
    quick_sort(list, mid, end)


def sort_quick(list):
    quick_sort(list, 0, len(list) - 1)


times = [1000, 10000, 12000, 15000]

for count in times:
    temp = [random.randint(10000, 99999) for _ in range(count)]
    select_array = temp[:]
    quick_array = temp[:]

    print(f"##데이터 수 : {count}개")
    start = time.time()
    select_sort(select_array)
    end = time.time()
    print(f"선택 정렬 -> {end - start:.3f}초")
    start = time.time()
    sort_quick(quick_array)
    end = time.time()
    print(f"퀵 정렬 -> {end - start:.3f}초")
    print()

    count *= 5
