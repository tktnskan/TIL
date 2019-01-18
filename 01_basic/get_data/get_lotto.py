# 주간 박스오피스
# https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=087ca6a1490cb65922d848fe9ea7121b&targetDt=20190113

# 영화 상세정보
# http://www.kobis.or.kr/kobisopenapi/webservice/soap/movie/searchMovieInfo.json
# ?
# key=
# &
# movieCd=20185485
# 087ca6a1490cb65922d848fe9ea7121b

'''
https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837
'''

import requests

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837'

got = requests.get(url)

print(got)