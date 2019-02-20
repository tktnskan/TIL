import sys
sys.stdin = open('input(9).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    a = []
    for i in range(0, len(arr), 2):
        a.append([arr[i], arr[i + 1]])
    b = []
    for i in a:
        c = [i[0], i[1]]
        g = 0
        while g <= 1000:
            for j in a:
                g += 1
                if j[0] == c[-1]:
                    c.append(j[0])
                    c.append(j[1])
                    break
        b.append(c)
    d = []
    for i in b:
        d.append(len(i))
    for i in b:
        if len(i) == max(d):
            e = []
            for j in i:
                e.append(str(j))
            e = " ".join(e)
            print(f'#{test_case} {e}')
            break



