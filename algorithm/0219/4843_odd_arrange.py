import sys
sys.stdin = open('sample_input(10).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr_new = []
    for i in range(len(arr) - 1):
        minIdx = i
        for j in range(minIdx + 1, len(arr)):
            if arr[minIdx] > arr[j]: minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]
    while len(arr_new) < 10:
        a = arr[0]
        for j in arr:
                if j > a:
                    a = j
        arr_new.append(str(a))
        del arr[-1]
        b = arr[0]
        for k in arr:
                if k < b:
                    b = k
        arr_new.append(str(b))
        del arr[0]
    arr_new = " ".join(arr_new)
    print(f'#{test_case} {arr_new}')
