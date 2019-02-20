# import sys
# sys.stdin = open('s_input.txt', 'r')
#
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     count = 0; s = 0; f = 0
#     for i in range(N):
#         a = [int(x) for x in input().split()]
#         s += a[0]
#         f += a[1]
#         if s <= f:
#             count += 1
#     print(f'#{test_case} {count}')

print(ord('A'))
print(chr(65))
print(0x41)  # 16진수 41을 의미


str1 = 'abcde'
str2 = str1
print(id(str1), id(str2))
str2 = str2 + 'x'
print(id(str1), id(str2))


list1 = [0, 1, 2, 3]
list2 = list1
list2[0] = -1
print(list1, list2)


# 정수를 문자열로 변환
num = int(input("정수 입력: "))

# str() 함수 사용
numstr = str(num)
print(numstr)


# /, % 연산자 사용
numstr = ''

if num == 0:
    numstr = '0'
else:
    while num > 0:
        digit = num % 10
        num = num//10
        numstr += str(digit)

numstr = numstr[::-1]

print(numstr)

#문자열 뒤집기

arr = 'algorithm'
arr = arr[::-1]

print(arr)

arr = arr[::-1]

print(arr)

# 문자열 리스트 변환

STR1 = 'algorithm'

LIST = list(STR1)
print(LIST)

STR2 = ''.join(LIST)

print(STR2)



#인코딩 테스트

print(ord('A'))
print(chr(65))

import sys
import codecs
#sys.stdin = codecs.open("input_utf8.txt", 'r', 'utf-8')
sys.stdin = open("input.txt")

T = int(input())
for i in range(T):
    tmp = input()
    print(tmp)



# 회문 검사

def isPalindrome(arr):
    N = len(arr)
    cnt = N // 2

    i = 0
    while i < cnt:
        if arr[i] != arr[N - 1 - i]:
            return False
        i += 1

    return True


arr1 = 'abacxcaba'
arr2 = 'bbbbabbb'

print(isPalindrome(arr1))
print(isPalindrome(arr2))





num = 12345

A = []
while num > 0:
    A.append(num % 10)
    num = num // 10
N = len(A)
for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            A[i], A[j] = A[j], A[i]
print(A)





### 패턴매칭

p = "CATTCCCTGCGCCGC"
t = "ADFDVEGSGCVSGERHERHEWGEWGWEHWWHBVCATTCCCTGCGCCGCCCASGEGVVCCCGCFDDWWFWGEDGJOKDPOJBNVNVNDKKDOODSJ"
n, m = len(t), len(p)
i = j = 0
while i < n:
    if t[i] != p[j]:
        i = i - j
        j = -1
    i, j = i + 1, j + 1
    if j == m:
        print(t[i - j: i])

# i = 0
# while i <= n - m:
#     j = 0
#     while j < m:
#         if t[i + j] != p[j]: break
#         j += 1
#     if j == m:
#         print(t[i:i + m])
#         i = i + m - 1
#     i += 1

next = [0] * (m + 1)
#전처리
next[0] = -1
i, j = 0, -1
while i < m:
    while j >= 0 and p[j] != p[i]:
        j = next[j]
    i, j = i + 1, j + 1
    next[i] = j
print(next)

# 매칭
i = j = 0
while i < n:
    while j >= 0 and p[j] != t[i]:
        j = next[j]


p = "CATTCCCTGCGCCGC"                                                                       # pattern
t = "ATTTGTGCATGTTTGAGCTTTTACGTACGAGAAACTGAACGTACCTACGACATTCCCTGCGCCGCCACCCGCTTTTTGAA"      # text

# 1. 문자열.find() 사용
idx = t.find(p)
print(p)
print(t[idx:])


# 2. Brute-Force1
m, n = len(p), len(t)
for i in range(n - m + 1):
    j = 0
    while j < m:
        if p[j] != t[i + j]: break
        j += 1

    if j == m:
        print(t[i:])
        break


# 3. Brute-Force2
i = j = 0
while i < n:
    if p[j] != t[i]:
        i = i - j
        j = -1

    i, j = i + 1, j + 1
    if j == m:
        print(t[i- j:])
        break

## 패턴매칭 -kmp

p = 'abcdabcef'                                                                       # pattern
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text


m, n = len(p), len(t)
next = [0] * (m + 1)

# 전처리
next[0] = -1
i, j = 0, -1
while i < m:
    while j >= 0 and p[j] != p[i]:
        j = next[j]

    i, j = i + 1, j + 1
    next[i] = j

print(next)

# 매칭
i = j = 0
while i < n:
    while j >= 0 and p[j] != t[i]:
        j = next[j]

    i, j = i + 1, j + 1

    if j == m:
        print(t[i - j:])
        break



# karprabin 패턴매칭

p = 'abcdabcef'                                                                    # pattern
t = 'alksdabcdabcflaskjflkabcdjsaflkjasdkdsajfabcdabceflksadjabcdaksfjffsdaf'      # text


n = len(t)
m = len(p)

th, ph, h0 = 0, 0, 1
for i in range(m):
    th = (th * 10 + ord(t[i])) % 12345
    ph = (ph * 10 + ord(p[i])) % 12345

for i in range(m - 1):
    h0 = (h0 * 10) % 12345

for i in range(n - m + 1):
    if ph == th:
        j = 0
        while j < m:
            if t[i + j] != p[j]:
                break
            j += 1
        if j == m:
            print(i, t[i:])
            break


    if i == n - m: break
    th = ((th - ord(t[i]) * h0) * 10 + ord(t[i + m])) % 12345
    if th < 0: th += 997
