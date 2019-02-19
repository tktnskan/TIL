# # 문제 1 : 낙차 값 구하기  ( 배열(Array) 활용 예제 )
#
# arr = [7, 4, 2, 0, 0, 6, 0, 7, 0]
# maxH = 0
# for i in range(len(arr)):
#     height = len(arr) - 1 - i # 상자가 없을 때 낙하값
#     cnt = 0
#     for j in range(i + 1, len(arr)):
#         if arr[i] <= arr[j]: cnt += 1
#     height -= cnt
#     maxH = max(height, maxH)
# print('--------------------문제 1---------------------------')
# print(maxH)
#
#
# # 문제 2 : 순열 ( 4개의 알파벳 중 3개 무작위로 선정 )
#
# arr ='ABCD'
#
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i == j: continue
#         for k in range(len(arr)):
#             if k == i or k == j: continue
#             print('\n----------------------문제 2-------------------------')
#             print(arr[i], arr[j], arr[k])
#
#
#
# # 문제 3 : Bubble sort ( 인접한 두개의 원소를 비교하교 자리를 계속 교환하는 방식 )
#
# arr = [213, 4, 2, 5345, 123, 41, 3]
#
# for i in range(len(arr)-1, 0, -1):
#     for j in range(0, i):
#         if arr[j] > arr[j + 1]:  # 부호 조정을 통해 오름차순, 내림차순 변경가능
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print('\n---------------------문제 3--------------------------')
# print(arr)
#
#
#
# arr = [55 ,7, 78, 12, 42]
# N = len(arr)
# for i in range(N-1):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
# print('\n----------------------문제 3 (1)-------------------------')
# print(arr)
#
#
# for i in range(N-2):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
# print('\n----------------------문제 3 (2)-------------------------')
# print(arr)
#
# for i in range(N-3):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
# print('\n----------------------문제 3 (3)-------------------------')
# print(arr)
#
# for i in range(N-4):
#     if arr[i] > arr[i + 1]:
#         arr[i], arr[i + 1] = arr[i + 1], arr[i]
# print('\n----------------------문제 3 (4)-------------------------')
# print(arr)
#
# for i in range(N - 1, 0, -1):
#     for j in range(i):
#         if arr[j] > arr[j + 1]:
#             arr[j], arr[j + 1] = arr[j + 1], arr[j]
# print('\n----------------------문제 3 (1) ~ (4)-------------------------')
# print(arr)
#
#
#
# # 문제 4: 카운팅 정렬
# K = 4
# arr = [0, 4, 1, 3, 1, 2, 4, 1]
# cnt = [0] * (K + 1)
# sorted = [0] * len(arr)
# #빈도수 계산
# for val in arr:
#     cnt[val] += 1
# print('\n----------------------문제 4-1-1-------------------------')
# print(cnt)
#
# # 누적 빈도수 계산
# for i in range(1, K + 1):
#     cnt[i] += cnt[i - 1]
# print('\n----------------------문제 4-1-2-------------------------')
# print(cnt)
#
# # 뒤에서부터 채우기 (sorted)
# for i in range(len(arr)-1, -1, -1):
#     cnt[arr[i]] -= 1
#     sorted[cnt[arr[i]]] = arr[i]
# print('\n----------------------문제 4-1-3-------------------------')
# print(sorted)
#
#
# def Counting_Sort(A, B, k):
#     C = [0] * k
#     for i in range(1, len(B) + 1):
#         C[A[i]] += 1
#     for i in range(1, len(C) + 1):
#         C[i] += C[i-1]
#     for i in range(len(B)-1, -1, -1):
#         B[C[A[i]] - 1] = A[i]
#         C[A[i]] -= -1
# Counting_Sort([4, 3, 2, 621, 23, 34], [])

import sys
sys.stdin = open('input.txt', 'r')
# sys.stdout = open('input.txt', 'w') # 이렇게하면 출력은 안되지만 실제 값은 입력되어있음


for test_case in range(1, 11):
    N = int(input())
    arr = [int(x) for x in input().split()]
    a = []
    for i in range(2, N - 2):
        b = [arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2]]
        if arr[i] > max(b):
                a.append(arr[i]-max(b))
    print(f'#{test_case} {sum(a)}')


# 선생님 답!

for test_case in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    ans = 0
    for i in range(2, N - 2):
        maxH = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])
        if arr[i] > maxH:
            ans = ans + (arr[i] - maxH)
    print("#%d %d" % (test_case, ans))



