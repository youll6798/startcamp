import requests

token = '1556526336:AAHU1-MwPWDdAYidx-X6ig3W4VLlRBFO9D0'
url = f'https://api.telegram.org/bot{token}/'
ngrok_url = 'https://namgyukim.pythonanywhere.com'    #원래 오전에는 이거 엥그록으로 했었는데 이제 파이썬에니웨얼로 바꿨다. (그냥 파이썬에니웨어가서 서버만들고 그 서버로 주소만 바꿨음)
                                                      #원래 local서버(나혼자만들어올수있는 서버)로 텔레그램챗봇 만들었었는데 
                                                      # 파이썬애니웨어로 배포서버만들어서 하니까 이제 vscord꺼도 챗봇 쌉가능
set_url = url + 'setWebhook?url=' + ngrok_url +'/telegram'

print(set_url)

print(requests.get(set_url))






# 1556526336:AAHU1-MwPWDdAYidx-X6ig3W4VLlRBFO9D0

# https://api.telegram.org/bot<token>/METHOD_NAME

# [내 API 넣은 getMe주소]
# https://api.telegram.org/bot1556526336:AAHU1-MwPWDdAYidx-X6ig3W4VLlRBFO9D0/getMe

# "id": 1589670816

# [아이디와 메시지(안녕) 넣은 주소]
# https://api.telegram.org/bot1556526336:AAHU1-MwPWDdAYidx-X6ig3W4VLlRBFO9D0/sendMessage?chat_id=1589670816&text=%EC%95%88%EB%85%95

# [ngrok 주소]
# https://2c7da33d72eb.ngrok.io -> http://localhost:5000 