import sys
sys.stdin = open('GNS_test_input.txt', 'r')

# --------------------------첫번째풀이---------------------------------------

T = int(input())
for test_case in range(1, T + 1):
    N = [x for x in input().split()]
    arr = [x for x in input().split()]
    arr_new = []
    for i in arr:
        if i == 'ZRO':
            arr_new.append(i)
    for i in arr:
        if i == 'ONE':
            arr_new.append(i)
    for i in arr:
        if i == 'TWO':
            arr_new.append(i)
    for i in arr:
        if i == 'THR':
            arr_new.append(i)
    for i in arr:
        if i == 'FOR':
            arr_new.append(i)
    for i in arr:
        if i == 'FIV':
            arr_new.append(i)
    for i in arr:
        if i == 'SIX':
            arr_new.append(i)
    for i in arr:
        if i == 'SVN':
            arr_new.append(i)
    for i in arr:
        if i == 'EGT':
            arr_new.append(i)
    for i in arr:
        if i == 'NIN':
            arr_new.append(i)
    arr_new = " ".join(arr_new)
    print(f'{N[0]}\n{arr_new}')


# ----------------------------두번째풀이-------------------------------------

T = int(input())
for test_case in range(1, T + 1):
    N = [x for x in input().split()]
    arr = [x for x in input().split()]
    arr_new = []
    alpha = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count = 0
    while len(arr_new) < int(N[1]):
        for i in arr:
            if i == alpha[count]:
                arr_new.append(i)
        count += 1
    arr_new = " ".join(arr_new)
    print(f'{N[0]}\n{arr_new}')


# ---------------------------세번째풀이--------------------------------------

T = int(input())
for test_case in range(1, T + 1):
    N = [x for x in input().split()]
    arr = [x for x in input().split()]
    a = []
    alpha = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count = 0
    while len(a) < int(N[1]):
        for i in arr:
            if i == alpha[count]:
                a.append(i)
        count += 1
    print(f'{N[0]}\n{" ".join(a)}')


# ---------------------------네번째풀이--------------------------------------


T = int(input())
for test_case in range(1, T + 1):
    N = [x for x in input().split()]
    arr = [x for x in input().split()]
    a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    while len(a) < int(N[1]):
        for i in arr:
            if i == a[0]:
                a.append(i)
        del a[0]
    print(f'{N[0]}\n{" ".join(a)}')


# --------------------------다섯번째풀이---------------------------------------

T = int(input())
for test_case in range(1, T + 1):
    N = [x for x in input().split()]
    arr = [x for x in input().split()]
    a = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    count = 0
    while len(a) < int(N[1]) + 10:
        for i in arr:
            if i == a[count]:
                a.append(i)
        count += 1
    print(f'{N[0]}\n{" ".join(a[10:])}')