# 181218  수업정리

## 1. 개발환경 설정

* chocolatey

  * enter  하고 tab누르면 이렇게 됨
  * 윈도우 패키지 매니저

* python -v 3.6.7

* git

  * version control system

* vscode

  * code editor
  * ctrl+shift+p -> shell 입력 -> select default shell -> git bash 그 후 ctrl+`
  * cd = changedirectory, ls = list, cd로 내부폴더로 들어갔을때 ~로 바뀌면 그것이 나타내는것이 home이다.  굳이 cd Users/student 안치고 cd 만 쳐도  home으로 갈 수 있다.
  * 파일 폴더를 만들때 터미널에  mkdir  폴더이름 으로 만들 수 있다. ex)mkdir day_1 day_2
  * 지울 때는 rmdir을 사용
  * 파일을 만들때는  touch 명령어 사용
  * 코드를 실행할때는 터미널에 python 파일이름 을 통해 실행한다. ex) python first_python.py
  * $ 명령싸인, >>> 파이썬 코드싸인, exit() 누르면 다시 명령프롬프트로 돌아감
  * clear 쓰면 화면을 밀수있다 혹은 ctrl+L
  * *는 곱하기, **는 제곱, / 은 나누기(실수로 값변경), %은 나머지값 

* chrome

  * browser

* typora

  *  노트정리
  * typora -> ctrl+1 누르면 크기 커짐 2는 작아짐


## 2. Python  기초 문법

1. 문자열을 합치는 법

```python
print('happy hacking')

first_name = 'Yoon'
last_name = 'Jinyung'
full_name = first_name + ' ' + last_name
print(full_name)
```



2.  짝수와 홀수를 판단하는 법

```python
if (10 % 2 == 1):  #나머지 연산자
    print('odd')
else:
    print('even')
```



3. BMI 계산

```python
height = 1.82
weight = 90
bmi = weight / height ** 2  
# / 는 나눗셈 연산자 정수값이 실수값으로 바뀐다, **은 제곱
print(bmi)
```



4. 변수 타입 알아보기

```python
x= True
y= 1
z= 10.4
k= 'hi'
print(type(x)) #bool
print(type(y)) #int
print(type(x)) #float
print(type(k)) #str
```



5. list

```python
family = ['mom', 1.66, 'dad', 1.77, 'sis', 1.70]
family_1 = {'mom' : 1.66, 'dad' : 1.77, 'sis' : 1.70} #딕셔너리
family[2:4] #리스트안에 요소를 불러옴. -를 붙이면 맨 뒤부터 불러옴

mcu = [['ironman','captin'],['xmen','deadpool'],['spiderman']] # list안에 list를 또 만들 수 있다
mcu_1 = [
    ['ironman','captin','dr.strange'],
    ['xmen','deadpool'],
    ['spiderman']
]    # 리스트안에 리스트문을 만들때는 줄을 나눠주는게 가독성이 좋다.
disney = mcu_1[0]
disney[2]
mcu_1[0][2] #리스트의 리스트안에 한개 요소만 불러옴
mcu_1[1][1]

#int(), list(), str(), bool(), float() 등을 통해 괄호안의 것의 형태를 바꿔줄 수 있다.

numbers = list(range(1,46))
numbers[5:10:2]  #리스트 내에서 원하는 부분을 잘라서 가져옴 
                 #[start:end:interval] , start 이상 end 미만

x = ['life', 'is', 'short', True, 123,['you', 'need', 'python']]
my_bool = x[3] 
my_bool = x[-3] #리스트안의 원하는 요소를 꺼낼 수 있는 2가지 방법



team = [
    'john', 10000,
    'neo', 100,
    'tak', 40500
]

type(team[2:4])  #리스트에서 슬라이싱으로 뽑으면 리스트의 형태로 뽑힘
new_member = ['js', 10]
#team = team + new_member
team += new_member
# len(team) == 8
del(team[2])
# len(team) == 7

del(team[2:4]) #통째로 지울수도있음
# len(team) == 5
```



6.  dictionary

```python
my_info = {
    'name' : 'ji', 
    'job' : 'hacker',
    'mobile' : '01023592054',
    'email' : 'jny4594@gmail.com'
}
hphk_info = [
    {
        'name' : 'john',
        'email' : 'john@hphk.io'
    },
    {
        'name' : 'cona',
        'email' : 'cona@hphk.io',
        'married' : False
    },
    {
        'name' : 'tak',
        'email' : 'tak@hphk.io'
    }
]
my_info['email']

p=hphk_info[2]
print(p['name'])
hphk_info[0]['email']

#가장 현실세계의 정보를 담기 좋은 것이 딕셔너리
```

| str      | int  | list           | bool    | <=class  |
| -------- | ---- | -------------- | ------- | -------- |
| 'python' | 100  | ['a','b',True] | 'False' | <=object |



7. Method

메서드느 함수다! 다만 **[주어].동사()**의 형식으로 이루어 지며, [주어]자리에 오는 object 들이 할 수 있는 행동(함수)들이다.



```python
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

```





git init 쓰면 깃 설정 (master) .git 이라는 디렉토리를 만들어줌

ls -a 하고 rm -rf .git/ 하면 깃 설정 사라짐

