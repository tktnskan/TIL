import sys
sys.stdin = open('sample_input(8).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    arr = list(map(int, input().split()))
    N, K = arr[0], arr[1]
    b = []
    for i in range(1 << len(A)):
        a = []
        for j in range(len(A)):
            if i & (1 << j) != 0:
                a.append(A[j])
        total = 0
        for k in a:
            total += k
        if total == K and len(a) == N:
            b.append(a)
    print(f'#{test_case} {len(b)}')