my_list = [4,7,9,1,3,6]
#최대/최소
max (my_list)
min (my_list)
#특정 요소의 인덱스?
my_list.index()
#리스트를 뒤집으려면?
my_list.reverse()

dust= 100 #<class: int> 101
lang = 'python' #str
samsung = ['elec','sds', 's1'] #list

#method는  object 에 속해있는 함수, object가 할수있는 행동들

lang.capitalize()  #대문자
lang.replace('on','off') #교체
samsung.index('sds') #인덱스
samsung.count('s1')  #카운트

samsung.sort() #어떤 method 는 결과를 출력해주고 원본은 유지되지만, 일부는 결과 출력없이 원본을 바꿔버린다

numbers = [8,5,4,2,3]
sorted_numbers = numbers.sort() #이렇게 하면 sorted_numbers는 출력되지않지만 numbers는 오름차순으로 바뀐다.
new_samsung = samsung.append('bio') #원본이 바뀐다!
