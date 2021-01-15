import requests
from pprint import pprint

# 1. 발급 받은 api key로 미세먼지 정보 요청 보내기
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=1Apf7aXtrknyZmTDFz5ZkwJXoiZvM1h%2FPm9DcVBIASIftB7H29nRwMeE8AV71nX7F%2B7VUL%2BK2fqn9XbxnHdLxQ%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EA%B2%BD%EB%B6%81&ver=1.0'
response = requests.get(url).json()
pprint(response)

# 2. 응답 받은 데이터로 sidoNmae, pm10Value 출력하기