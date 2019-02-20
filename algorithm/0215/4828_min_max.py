import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    a = arr[0]
    for i in arr:
        if i > a:
            a = i
    b = arr[0]
    for j in arr:
        if j < b:
            b = j
    print(f'#{test_case} {a-b}')