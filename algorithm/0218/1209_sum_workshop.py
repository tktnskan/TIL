import sys
sys.stdin = open('input(8).txt', 'r')

#
# for test_case in range(1, 11):
#     T = int(input())
#     l = []; a = []
#     for i in range(100):
#         l.append(list(map(int, input().split())))
#     for i in range(100):
#         d = 0; e = 0; f = 0; g =0
#         for j in range(100):
#             d += l[i][j]
#             e += l[j][i]
#             if i == j:
#                 f += l[i][j]
#             elif i + j == 99:
#                 g += l[i][j]
#         a.append(d); a.append(e); a.append(f); a.append(g)
#     print(f'#{T} {max(a)}')



# 선생님 답안

for test_case in range(1, 11):
    N = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    Max = diag1 = diag2 = 0
    for i in range(100):
        diag1 += arr[i][i]
        diag2 += arr[i][99 - i]
        rsum = csum = 0
        for j in range(100):
            rsum += arr[i][j]
            csum += arr[j][i]
        Max = max(Max, rsum, csum)
    Max = max(Max, diag1, diag2)
    print(Max)
