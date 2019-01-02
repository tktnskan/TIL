# 190102

좌석표 : zzu.li/ss3_seat



* Day_1 : 자기소개 + 파이썬 기초 + 챗봇
* Day_2 : chocolatey 를 이용하여 프로그램(python, git, typora, vscode, chrome) 설치 + 기초 파이썬
* Day_3 : 퀴즈 (로또 및 날씨) 코딩
* Day_4 : 로또 코딩을 실제 동행로또 사이트에서 정보를 받아와 내 번호와 비교해보는 코딩
* Day_5 : api서버를 이용하여 챗봇(텔레그램) 구동, 궁합 등..



## Scratch

* 재밌다..
* projects/23980991/#editor 에 들어가면 선생님이 짠 스크래치 코드있음
* 심심할때 해보자





## Python (jupyter_notebook)

* pip -V 로 설치 확인
* `pip install jupyter`
* cd TIL 치면 ~/TIL (master) 로 바뀜, cd 뒤에 폴더명을 쓰면 그 안으로 들어감
* `git clone https://github.com/eduyu/jupyter_notebooks.git                      ` 하면 파이썬 폴더안에 다운로드 됨
* ls  라 치면 주피터_노트북이 나옴
* cd jupyter_notebooks/  --> ls -a  -->  rm -rf .git (깃 삭제) --> ls -a (확인) --> jupyter notebook 치면 크롬에서 켜짐!
* ctrl+c 누르면  jupyter notebook 종료 가능
* 주피터 노트북에서 playground 폴더 만들고 안에들어가서  python3클릭
* esc 누르면 파란색 (커맨드 모드) , 클릭하면 초록색 (에디터 모드)
* 주피터는 셀 단위로 코드가 실행됨 in 하나하나가 각자의 셀
* b==> add cell
* 커맨드 창에서 00 누르고 리셋하면 in[1]로 바뀜, 즉 모든 셀 안의 코드 초기화
* kernel 에  restart & clear output 하면 아예 초기화됨 []숫자까지
* h 키 누르면 모든 단축키 확인가능



주피터에 최대공약수, 최소공배수 구해보기

``` python
num1 = int(input('첫번째숫자 입력: '))
num2 = int(input('두번째숫자 입력: '))


numbers= [num1] + [num2]
min_numbers = min(numbers)


n = 1
cd = []

while n<=min_numbers:
    if num1 % n == 0 and num2 % n == 0:
        cd.append(n) 
        n = n + 1
    else:
        n = n + 1
        
print('공약수는',cd)

gcd = max(cd)
lcm = num1*num2//gcd

print(str(num1) + '과' + str(num2) + '의 최대공약수는 ' + str(gcd))
print(str(num1) + '과' + str(num2) + '의 최소공배수는 ' + str(lcm))


```











깃!

cd til  -> git init ->  echo '.ipynb_checkpoints/' (til 폴더 안에서 해야함) >> .gitignore  ->  git config --global core.autocrlf true





