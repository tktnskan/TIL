import sys
sys.stdin = open('sample_input(4).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    arr_1 = list(map(int, input().split()))
    arr_2 = list(map(int, input().split()))
    a = []
    for i in range(len(arr_2) - (arr_1[1] - 1)):
        q = 0
        for j in range(i, arr_1[1] + i, 1):
            q += arr_2[j]
        a.append(q)
    b = a[0]
    for i in a:
        if i > b:
            b = i
    c = a[0]
    for j in a:
        if j < c:
            c = j
    print(f'#{test_case} {b-c}')

