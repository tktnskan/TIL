# lo, hi = 0, 10
# mid = (lo + hi) // 2
# print(mid)
#
# # 비트 연산자
# mid = (lo + hi) >> 1
# print(mid)

print('-----------------------------------\n')
#
# arr = [[1,2,3,4,5],
#        [10,9,8,7,6],
#        [11,12,13,14,15],
#        [20,19,18,17,16],
#        [21,22,23,24,25]]
#
# for i in range(len(arr)):
#     if i % 2 == 0:
#         for j in range(len(arr[0])):
#             print(arr[i][j], end=" ")
#     else:
#         for j in range(len(arr[0])-1,-1,-1):
#             print(arr[i][j], end=" ")
print('-----------------------------------\n')

arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]
for c in range(len(arr)):
    arr[c].append(arr[c][-1])
    arr[c].append(arr[c][0])
arr.append(arr[-1])
arr.append(arr[0])
di_x = [0, 0, 1, 1]
di_y = [1, 1, 0, 0]
a = 0
for i in range(len(arr) - 2):
    for j in range(len(arr) - 2):
        for k in range(4):
            a += abs(arr[i - di_x[k]][j] - arr[i][j])
            a += abs(arr[i][j] - arr[i][j - di_y[k]])

print(a)

print('-----------------------------------\n')

arr = [1, 3, 5]
bit = [0] * len(arr)
for i in [0, 1]:
    bit[0] = i
    for j in [0, 1]:
        bit[1] = j
        for k in [0, 1]:
            bit[2] = k
            print(bit)

print('-----------------------------------\n')

arr = [3, 6, 7, 1, 5, 4]
N = len(arr)

for i in range(1 << len(arr)):  # 0 ~ 63
    # 2^0 ~ 2^5 에 해당하는 비트 값을 확인
    for j in range(N):
        if i & (1 << j) != 0:
            print(arr[j], end=" ")
    print()
print('-----------------------------------\n')

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
for i in range(1 << len(arr)):
    a = []
    for j in range(N):
        if i & (1 << j) != 0:
            a.append(arr[j])
    total = 0
    for k in a:
        total += k
    if total == 10:
        print(a)
print('-----------------------------------\n')
for i in range(1 << len(arr)):
    SUM = 0
    for j in range(N):
        if i & (1 << j) != 0:
            SUM += arr[j]
    if SUM == 10:
        for j in range(N):
            if i & (1 << j) != 0:
                print(arr[j], end=", ")
        print()

print('-----------------------------------\n')


# arr = [2, 5, 7, 8, 12,
#        16, 21, 23, 33,
#        39, 42, 45, 45,
#        49, 62, 88]
#
#
# def binary_search(arr, key):
#     start, end = 0, len(arr) - 1
#
#     while start <= end:
#         mid = (start + end) >> 1
#         if arr[mid] == key:
#             return mid
#         elif arr[mid] > key:
#             end = mid - 1
#         else:
#             start = mid - 1
#     return -1
#
#
# print(binary_search(arr, 33))
#
#
# def binary_Search(arr, start, end, key):
#     if start > end: return -1
#     mid = (start + end) >> 1
#     if arr[mid] == key:
#         return mid
#     elif arr[mid] > key:
#         return binary_Search(arr, start, mid - 1, key)
#     else:
#         return binary_Search(arr, mid + 1, end, key)
#
#
# print('-----------------------------------\n')



# sort
arr = [64, 25, 10, 22, 11]
N = len(arr)
for i in range(N - 1):
    minIdx = i
    for j in range(minIdx + 1, N):
        if arr[minIdx] > arr[j]: minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]
    print(arr)

print('-----------------------------------\n')


# k번째로 작은 원소를 찾는 알고리즘

a = [64, 25, 10, 22, 11]
def select(a, k):
    for i in range(k):
        minIdx = i
        for j in range(minIdx + 1, N):
            if a[minIdx] > a[j]: minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]
    return a[k-1]
print(select(a, 3))

print('-----------------------------------\n')





