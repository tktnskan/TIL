# 함수가 필요한 이유? 
# 문제를 해결하기 위해 반복구문을 사용할때, 번거로움을 줄이기 위해

print('hi')
len('hi')
type('a')
scores = [45, 60, 78, 88]
highest_score = max(scores)

round(1.8) #반올림 2
round(1.876, 2) #소수점 두번째까지 반올림하여 표기
lowest_score = min(scores)

first = [11.25,18.0,20.0]
second = [10.75,9.50]

#full 에 first와 second을 합쳐서 저장
full = first + second
#full_sorted 에 함수 full 을 정렬해서 저장
full_sorted = sorted(full)
# *reverse_sorted 에 full을 내림차순으로 정렬해서 저장
reverse_full_sorted = sorted(full,reverse=True)


def avg(a):
    total =0
    for i in a:
        total += i
    avg = total / len(a)
    print(avg)
    
