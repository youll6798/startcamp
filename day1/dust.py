import random
key = 'JK6kb4rYpz1N3820QzQZkPEs9HCjHzIwlbJ2qNs7Q0cY%2FN8b1my3UGYaV80JlIaBYNvJi49z5m306pyqBZK4hg%3D%3D'


import requests
from bs4 import BeautifulSoup

url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'
response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[5]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.

if dust > 150:
    print("매우나쁨")
elif 80<dust<=150:
    print("나쁨")
elif 30<dust<=80:
    print("보통")
else:
    print("좋음")