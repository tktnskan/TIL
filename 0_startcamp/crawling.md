```
# 크롤링 코드

## 1.날씨

​```python
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID={}".format(key)

data = requests.get(url).json()
weather = data['weather'][0]['description']
temp = float(data['main']['temp'])-273.15
temp_min = float(data['main']['temp_min'])-273.15
temp_max = float(data['main']['temp_max'])-273.15

print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
최저/최고 온도는 {:.1f}/{:.1f}도 입니다.
""".format(weather, temp, temp_min, temp_max)
)
​```



## 2.환율

​```python
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex/'

response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

data_set = soup.select('.value')
data = data_set[1].text

print("JPY")
print(data)
​```



```





```
# 날씨 
import requests

url = "https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID={}".format(key)

data = requests.get(url).json()
weather = data['weather'][0]['description']
temp = float(data['main']['temp'])-273.15
temp_min = float(data['main']['temp_min'])-273.15
temp_max = float(data['main']['temp_max'])-273.15

print("""서울의 오늘 날씨는 [{}] 이며, 섭씨 {:.1f}도 입니다.
최저/최고 온도는 {:.1f}/{:.1f}도 입니다.
""".format(weather, temp, temp_min, temp_max)
)


# 미세먼지
import requests
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={}&sidoName=서울&pageNo=3'.format(key)
response = requests.get(url).text
soup = BeautifulSoup(response, 'xml')
gn = soup('item')[7]
location = gn.stationName.text
time = gn.dataTime.text

# 얘가 중요한 것!
dust = int(gn.pm10Value.text)

print('{0} 기준: 서울시 {1}의 미세먼지 농도는 {2} 입니다.'.format(time, location, dust))

# 그래서 지금 공기가 어느정도로 안좋은건데..?
if dust > 150:
  print('매우 나쁨')
elif dust > 80:
  print('나쁨')
elif dust > 30:
  print('보통')
else:
  print('좋음')


#환율
import requests
from bs4 import BeautifulSoup

response = requests.get('https://finance.naver.com/marketindex/')
doc = response.text
soup = BeautifulSoup(doc, 'html.parser')
data_set = soup.select('.value')
usd = data_set[0].text
jyp = data_set[1].text

print('달러 : ' + usd)
print('엔화 : ' + jyp)
```





import requests

url = '<https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837>'

response = requests.get(url)
response.text # 이건 class가 str임
response.json() # 이게 dict임 이걸 data라고 부름
lotto_data = response.json()

real_numbers = []

# for key in lotto_data:

# if 'drwtNo' in key:

# real_numbers.append(lotto_data[key]) # key 말고 i 같은 다른 문자가 와도 됨

for key, value in lotto_data.items():
if 'drwtNo' in key:
real_numbers.appent(value)

print(sorted(real_numbers))
bonus_number = lotto_data['bnusNo']







```
import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

response = requests.get(url)
response.text # 이건 class가 str임
response.json() # 이게 dict임 이걸 data라고 부름
lotto_data = response.json()

real_numbers = []

for key, value in lotto_data.items():
if 'drwtNo' in key:
real_numbers.appent(value)

print(sorted(real_numbers))
bonus_number = lotto_data['bnusNo']
```

