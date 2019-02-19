arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

arr_new = []
for i in range(len(arr)):
    for j in range(len(arr)):
        arr_new.append(arr[i][j])
N = len(arr_new)
for i in range(N - 1):
    for j in range(i + 1, N):
        if arr_new[i] > arr_new[j]:
            arr_new[i], arr_new[j] = arr_new[j], arr_new[i]

o = 0
while o < len(arr) - 2:
    arr[o][o:len(arr) - o] = arr_new[:len(arr) - 2*o]
    del arr_new[:len(arr) - 2*o - 1]

    for i in range(o, len(arr) - o, 1):
        arr[i][- 1 - o] = arr_new[i - o]
    del arr_new[:len(arr) - 2*o - 1]

    arr[len(arr) - 1 - o][o:len(arr) - o] = arr_new[len(arr) - 1 - 2*o::-1]
    del arr_new[:len(arr) - 1 - 2*o:]

    for i in range(o, len(arr) - o - 1, 1):
        arr[len(arr) - 1 - i][o] = arr_new[i - o]
    del arr_new[:len(arr) - 1 - 2*o]

    o += 1

print(arr)

