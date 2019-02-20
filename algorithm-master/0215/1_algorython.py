import sys



# sys.stdin = open('sample_input.txt', 'r')
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     print(arr)
#     a = arr[0]
#     for i in arr:
#         if i > a:
#             a = i
#     b = arr[0]
#     for j in arr:
#         if j < b:
#             b = i
#     print(f'#{test_case} {a-b}')


# sys.stdin = open('sample_input(2).txt', 'r')
#
#
# T = int(input())
# for test_case in range(1, T + 1):
#     arr_KNM = list(map(int, input().split()))
#     arr_M = list(map(int, input().split()))
#     a = arr_KNM[0]
#     count = 0
#     count_M = 0
#     for i in range(1, arr_KNM[1] + 1):
#         arr_KNM[0] -= 1
#         if i == arr_M[count_M]:
#             if arr_KNM[0] < 0:
#                 count = 0
#             else:
#                 if count_M == len(arr_M) - 1:
#                     if arr_KNM[0] >= arr_KNM[-2] - arr_M[count_M]:
#                         count = count
#                     else:
#                         count += 1
#                         arr_KNM[0] = a
#                 else:
#                     if arr_KNM[0] >= arr_M[count_M + 1] - arr_M[count_M]:
#                         count = count
#                         count_M += 1
#                     else:
#                         count += 1
#                         arr_KNM[0] = a
#                         count_M += 1
#
#         if arr_KNM[0] < 0 or count > a:
#             count = 0
#     print(f'#{test_case} {count}')
#
#


# sys.stdin = open('sample_input(3).txt', 'r')
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = [int(x) for x in input()]
#     a = arr[0]
#     for i in arr:
#         if i > a:
#             a = i
#     cnt = [0] * (a+1)
#     count = 0
#     for i in arr:
#         cnt[i] += 1
#     b = cnt[0]
#     for j in cnt:
#         if j > b:
#             b = j
#     for i in range(len(cnt)-1, -1, -1):
#         if cnt[i] == b:
#             print(f'#{test_case} {i}')
#             break
#
#
# sys.stdin = open('sample_input(4).txt', 'r')
#
# T = int(input())
# for test_case in range(1, T + 1):
#     arr_1 = list(map(int, input().split()))
#     arr_2 = list(map(int, input().split()))
#     a = []
#     for i in range(arr_1[0] - (arr_1[1] - 1)):
#         q = 0
#         for j in range(i, arr_1[1] + i, 1):
#             q += arr_2[j]
#         a.append(q)
#     print(a)
#     b = a[0]
#     c = a[0]
#     for i in a:
#         if i > b:
#             b = i
#     print(b)
#     for j in a:
#         if j < c:
#             c = j
#     print(c)
#     print(f'#{test_case} {b-c}')
#
#
# sys.stdin = open('input(6).txt', 'r')


# for test_case in range(1, 11):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(N):
#         a = arr[0]
#         for j in arr:
#             if j > a:
#                     a = j
#         b = arr[0]
#         for k in arr:
#             if k < b:
#                 b = k
#
#         for q in range(len(arr)):
#             if arr[q] == a:
#                 arr[q] -= 1
#                 break
#         for p in range(len(arr)):
#             if arr[p] == b:
#                 arr[p] += 1
#                 break
#     a = arr[0]
#     for j in arr:
#         if j > a:
#             a = j
#
#     b = arr[0]
#     for k in arr:
#         if k < b:
#             b = k
#
#     print(f'#{test_case} {a - b}')



# for test_case in range(1, 11):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(N):
#         a = arr[0]
#         b = arr[0]
#         a = i for i in arr if i > a
#             if i > a:
#                     a = i
#         for i in arr:
#             if i < b:
#                 b = i
#         for i in range(len(arr)):
#             if arr[i] == a:
#                 arr[i] -= 1
#                 break
#         for i in range(len(arr)):
#             if arr[i] == b:
#                 arr[i] += 1
#                 break
#     a = arr[0]
#     for i in arr:
#         if i > a:
#             a = i
#     b = arr[0]
#     for i in arr:
#         if i < b:
#             b = i
#
#     print(f'#{test_case} {a - b}')

sys.stdin = open('input(7).txt', 'r')
for test_case in range(1, 11):
    T = int(input())
    a = []
    for i in range(16):
        arr = [int(x) for x in input()]
        a.append(arr)

    di = ''
    x = 1
    y = 1
    n = 0
    while n < 5000:
        if di != 'l' and di != 'r' and (a[y][x - 1] == 0 or a[y][x - 1] == 3 or a[y][x - 1] == 2):
            while a[y][x] != 1:
                x -= 1
            di = 'l'
            x += 1
            # print(di, y, x, a[x][y])
        elif di != 'u' and di != 'd' and (a[y + 1][x] == 0 or a[y + 1][x] == 3 or a[y + 1][x] == 2):
            while a[y][x] != 1:
                y += 1
            di = 'd'
            y -= 1
            # print(di, y, x, a[x][y])
        elif di != 'r' and di != 'l' and (a[y][x + 1] == 0 or a[y][x + 1] == 3 or a[y][x + 1] == 2):
            while a[y][x] != 1:
                x += 1
            di = 'r'
            x -= 1
            # print(di, y, x, a[x][y])
        elif di != 'u' and di != 'd' and (a[y - 1][x] == 0 or a[y - 1][x] == 3 or a[y - 1][x] == 2):
            while 1 != a[y][x]:
                y -= 1
            di = 'u'
            y += 1
            # print(di, y, x, a[x][y])

        if a[y + 1][x] == 1 and a[y - 1][x] == 1 and a[y][x + 1] == 1:
            di = 'r'
        elif a[y + 1][x] == 1 and a[y - 1][x] == 1 and a[y][x - 1] == 1:
            di = 'r'
        elif a[y + 1][x] == 1 and a[x - 1][x] == 1 and a[y][x + 1] == 1:
            di = 'u'
        elif a[y -1][x] == 1 and a[x - 1][x] == 1 and a[y][x + 1] == 1:
            di = 'u'
            

        if a[y][x] == 3:
            print(f'#{test_case} {1}')
            break

        n += 1
    if n >= 5000:
        print(f'#{test_case} {0}')



