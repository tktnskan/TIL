import sys
sys.stdin = open('sample_input(2).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    arr_KNM = list(map(int, input().split()))
    arr_M = list(map(int, input().split()))
    a = arr_KNM[0]
    count = 0
    count_M = 0
    for i in range(1, arr_KNM[1] + 1):
        arr_KNM[0] -= 1
        if i == arr_M[count_M]:
            if arr_KNM[0] < 0:
                count = 0
            else:
                if count_M == len(arr_M) - 1:
                    if arr_KNM[0] >= arr_KNM[-2] - arr_M[count_M]:
                        count = count
                    else:
                        count += 1
                        arr_KNM[0] = a
                else:
                    if arr_KNM[0] >= arr_M[count_M + 1] - arr_M[count_M]:
                        count = count
                        count_M += 1
                    else:
                        count += 1
                        arr_KNM[0] = a
                        count_M += 1

        if arr_KNM[0] < 0 or count > arr_KNM[2]:
            count = 0
    print(f'#{test_case} {count}')


# 선생님 답안

# for test_case in range(1, T + 1):
#     K, N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     arr.insert(0, 0)
#     arr.append(N)
#     ans = bus = 0 # ans : 답 bus : 시작위치
#     for i in range(1, M + 2):
#         if arr[i] - arr[i - 1] > K:
#             ans = 0
#             break
#         if bus + K > arr[i]:
#             bus = arr[i - 1]
#             ans += 1
#     print(ans)