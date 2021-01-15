import requests
from bs4 import BeautifulSoup  #html을 파씽해주는 모듈임

url = 'https://finance.naver.com/marketindex/'
response = requests.get(url).text  #url에서 받아온 정보를 파이썬 문자열 형태로 변환해준다. (이 과정 안하니 결과가 아예 안나왔엇음..)
soup = BeautifulSoup(response, 'html.parser')  #html을 파싱해주고 그걸 soup이라는 박스에 넣어준다. (파씽한다 == 분석한다)
kospiexchange = soup.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value')  #네이버 증시에서 ctrl+F12 해서 따온정보

print(kospiexchange.text) # 이 코드를 치면 우리가 원하는 그 숫자만 출력이 되는데, 그건 BeautifulSoup이라는 패키지만의 함수이다.