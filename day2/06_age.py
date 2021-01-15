import requests

# url = 'https://api.agify.io/?name=viktor'
# response = requests.get(url).json() 
# print(response) # status_code == 200이라는 출력값을 돌려받는다. 200이라는 값은 성공적으로 요청받고 응답했다는 뜻이다.
#                 # 그리고 json()을 붙이면 정렬된 데이터를 준다.

# 1. 자신의 이름을 url에 넣어서 데이터를 받아오시오.
name = 'kim'
url = 'https://api.agify.io/?{name}'
response = requests.get(url).json() 
print(response)

# 2. 받아온 데이터에서 이름과 나이를 출력하시오.
print(f"이름은 {response['name']}이고 나이는 {response['age']}입니다.")


#수민씨코드
# #1. 자신의 이름을 url에 넣어서 데이터를 받아오시오.
# url = 'https://api.agify.io/?name=sumin'
# response = requests.get(url).json()
# #2. 받아온 데이터에서 이름과 나이를 출력하시오.
# print(f"이름은 {response['name']}이고 나이는 {response['age']}입니다.")