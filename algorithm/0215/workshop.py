# import sys
# sys.stdin = open('input(6).txt', 'r')
#
# for test_case in range(1, 11):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     for i in range(N):
#         a = arr[0]
#         for j in arr:
#             if j > a:
#                     a = j
#
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


# 선생님 답안

import sys
sys.stdin = open('input(6).txt', 'r')

for test_case in range(1, 11):
    dump = int(input())
    arr = list(map(int, input().split()))
    cnt = [0] * 101
    MinIdx, MaxIdx = 0 , 100
    for i in range(dump):
        while cnt[MinIdx] == 0:
            MinIdx += 1
        while cnt[MaxIdx] == 0:
            MaxIdx -= 1
        cnt[MinIdx] -= 1
        cnt[MinIdx + 1] += 1
        cnt[MaxIdx] -= 1
        cnt[MaxIdx - 1] += 1