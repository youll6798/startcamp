import requests
from flask import Flask, request

# 기본설정
token = '1556526336:AAHU1-MwPWDdAYidx-X6ig3W4VLlRBFO9D0'
url = f'https://api.telegram.org/bot{token}/'

# 챗봇이 받은 메세지 정보 -> getUpdates


# 메시지 보낸 사람의 chat_id 받아오기
# url = https://api.telegram.org/bot{token}/getUpdates
response = requests.get(url + 'getUpdates').json()
print(response)
chat_id = response['result'][0]['message']['from']['id']  # 단순히 키값으로 접근하여 id값 얻기 (만약, id값이 없다면 에러가 난다)
text = response['message']['text']
# chat_id = response.get('result')[0].get('message').get('from').get('id')  #(이렇게 requests모듈의 .get으로 접근한다면 id 값이 없을때 None이 반환된다)
print(chat_id)

# 받은 chat_id 유저에게 안녕하세요 메세지 보내기 -> sendMessage
text = '안녕하세요'
result = requests.get(url + f'sendMessage?chat_id={chat_id}&text={text}')
print(result) # 보내는데 성공했는지 여부만 알기! (200이라는 값이 결과값으로 반환되면 성공한거임)