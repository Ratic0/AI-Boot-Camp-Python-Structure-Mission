import random
import time

## 함수 선언 부분 ##
def selc_sort(ary) :
    n = len(ary)
    for i in range(0, n-1) :
        min_idx = i
        for k in range(i+1, n) :
            if (ary[min_idx] > ary[k]) :
                min_idx = k
        tmp = ary[i]
        ary[i] = ary[min_idx]
        ary[min_idx] = tmp

    return ary

def q_sort(arr, start, end) :
    if end <= start :
        return

    low = start
    high = end

    pivot = arr[(low + high) // 2]	# 작은 값은 왼쪽, 큰 값은 오른쪽으로 분리한다.
    while low <= high:
        while arr[low] < pivot :
            low += 1
        while arr[high] > pivot :
            high -= 1
        if low <= high :
            arr[low], arr[high] = arr[high], arr[low]
            low, high = low + 1, high - 1

    mid = low

    q_sort(arr, start, mid - 1)
    q_sort(arr, mid, end)

def quick_sort(ary) :
    q_sort(ary, 0, len(ary) - 1)

## 메인 코드 부분 ##
count_ary = [1000, 10000, 12000, 15000]

for count in count_ary :
    temp_ary = [random.randint(10000, 99999) for _ in range(count)]
    select_ary = temp_ary[:]
    quick_ary = temp_ary[:]

    print("## 데이터 수 : ", count, "개")
    start = time.time()
    selc_sort(select_ary)
    end = time.time()
    print("	선택 정렬 --> %10.3f 초" % (end-start))
    start = time.time()
    quick_sort(select_ary)
    end = time.time()
    print("	퀵 정렬  --> %10.3f 초" % (end-start))
    print()

    count *= 5