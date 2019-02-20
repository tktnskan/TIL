import sys
sys.stdin = open('sample_input(11).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    c = []
    for i in range(len(arr)):
        c.append(i)
    a = []
    for i in range(1 << len(c)):
        b = []
        for j in range(N):
            if i & (1 << j) != 0:
                b.append(c[j])
        if len(b) == N // 2:
            a.append(b)
    result = []
    if len(a[0]) == 2:
        for i in a:
            for j in a:
                if (i[0] not in j) and (i[1] not in j):
                    result.append(abs((arr[i[0]][i[1]] + arr[i[1]][i[0]]) - (arr[j[0]][j[1]] + arr[j[1]][j[0]])))
        print(f'#{test_case} {min(result)}')

    elif len(a[0]) > 2:
        for i in a:
            h = list(set(c) - set(i))
            result1 = []
            result2 = []
            for j in i:
                for k in i:
                    if j != k:
                        result1.append(arr[j][k] + arr[k][j])
            result.append(sum(result1))
            for j in h:
                for k in h:
                    if j != k:
                        result2.append(arr[j][k] + arr[k][j])
            result.append(abs(sum(result1)-sum(result2)))
        print(f'#{test_case} {min(result)//2}')



















