import sys
sys.stdin = open('sample_input(7).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(10):
        arr.append([0]*10)
    for j in range(N):
        a = list(map(int, input().split()))
        if a[4] == 1:
            for k in range(a[0], a[2] + 1):
                for q in range(a[1], a[3] + 1):
                    if arr[k][q] == 2 or arr[k][q] == 3:
                        arr[k][q] = 3
                    else:
                        arr[k][q] =1
        elif a[4] == 2:
            for k in range(a[0], a[2] + 1):
                for q in range(a[1], a[3] + 1):
                    if arr[k][q] == 1 or arr[k][q] == 3:
                        arr[k][q] = 3
                    else:
                        arr[k][q] = 2
    count = 0
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 3:
                count += 1

    print(f'#{test_case} {count}')
