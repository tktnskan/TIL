import sys
sys.stdin = open('sample_input(3).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [int(x) for x in input()]
    a = arr[0]
    for i in arr:
        if i > a:
            a = i
    cnt = [0] * (a+1)
    count = 0
    for i in arr:
        cnt[i] += 1
    b = cnt[0]
    for j in cnt:
        if j > b:
            b = j
    for i in range(len(cnt)-1, -1, -1):
        if cnt[i] == b:
            print(f'#{test_case} {i} {b}')
            break