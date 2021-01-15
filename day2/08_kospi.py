import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
kospi = soup.select_one('#KOSPI_now')  #네이버 증시에서 ctrl+F12 해서 따온정보

# print(response) # (두개의 차이는, 그냥 텍스트로 받은 리스폰즈는 복잡하게 나오고)
print(kospi)     #(뷰티풀숩으로 받은건 좀 깔끔해서 우리가 필요로하는 정보를 찾기가 쉽다) 이 kospi는 네이버증시에서 딴 고유정보임
                 # <span class="num" id="KOSPI_now">3,149.93</span> 결과가 이렇게 나오는데, 우리가 필요한 정보는 3,149.93 이부분 만이다.

print(kospi.text) # 이 코드를 치면 우리가 원하는 그 숫자만 출력이 되는데, 그건 BeautifulSoup이라는 패키지만의 함수이다. 