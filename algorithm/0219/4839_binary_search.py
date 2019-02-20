import sys
sys.stdin = open('sample_input(9).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    start, end, mid = 1, arr[0], 0
    count1, count2 = 0, 0
    while mid != arr[1]:
        mid = (start + end) // 2
        if mid == arr[1]:
            count1 += 1
            break
        elif mid > arr[1]:
            end = mid
            count1 += 1
        else:
            start = mid
            count1 += 1
    start, end, mid = 1, arr[0], 0
    while mid != arr[2]:
        mid = (start + end) // 2
        if mid == arr[2]:
            count2 += 1
            break
        elif mid > arr[2]:
            end = mid
            count2 += 1
        else:
            start = mid
            count2 += 1

    if count1 == count2:
        print(f'#{test_case} 0')
    elif count1 > count2:
        print(f'#{test_case} B')
    else:
        print(f'#{test_case} A')

