from flask import Flask, request
import requests  # Flask는 서버를 만드는 프레임워크다.

app = Flask(__name__)  #이건 Flask모듈에 내장되어있는 코드라서 건들이면 안됨.

token = '1556526336:AAHU1-MwPWDdAYidx-X6ig3W4VLlRBFO9D0'
url = f'https://api.telegram.org/bot{token}/'

@app.route('/') # url을 설정하는 위치  # 결론적으로 이 코드는 우리가 인터넷에 www.naver.com 을 쳐서 요청하는것과 같다.
def hello_world():              # def는 함수를 정의하는 기능   
    return 'Hello, World!'      # return은 반환하는 기능



# /ssafy 라는 주소로 접근하면
@app.route('/ssafy')

# ssafy 라는 함수를 정의하고
# 'hello, ssafy!' 문자열을 보여주는 페이지를 만들어보자.
def ssafy():
    return 'hello, ssafy!'
# cf)한번 서버에 접속하면 터미널에서 ctrl+C로 서버종료시켜주고 다시 서버들어가서 새로고침하면 된다.

@app.route('/telegram', methods=['POST'])  #get방식과 POST방식의 디테일한 기능은 본과정 들어가서 배우자.

def telegram():
    # 텔레그램으로부터 요청이 들어오면 아래의 코드를 실행하겠다.
    # 요청이 들어온 정보는 == getUpdates에서 확인할 수 있었던 정보가 들어있다.
    # print(request)   # 텔레그램에 안녕 이라고 치면 <Request 'http://2c7da33d72eb.ngrok.io/telegram' [POST]>
    #                  # 127.0.0.1 - - [15/Jan/2021 14:09:18] "POST /telegram HTTP/1.1" 200 - 라는 결과값이 나오는데 성공적으로 받아왔다는 뜻이다.
    # print(dir(request))
    print(request.get_json()) # 이거치고 텔레에 안녕치면 누가(id) 보냈는지 그런 정보들이 실시간으로 다 출력 된다.
                              # request는 내 서버로 온 정보들이 있다. 그중에서 json을 뽑아보니 내 챗봇에 메세지를 누가 보냈고 그런 정보들이 달려있다.
    response = request.get_json()
    # chat_id = response['message']['from']['id']
    # text = response['message']['text']
    # print(dir(request))
    # print(chat_id)
    # print(text)
    # 요청이 들어온 정보는
    # getUpdates에서 확인할 수 있었던 정보가 들어있다.

    #url = 'api/bot<token>/' + methodName?queryString
    # 요청을 보내주기 위한 코드
    # requests.get(url + f'sendMessage?chat_id={chat_id}&text={text}')
    if response.get('message') != None:
        chat_id = response.get('message').get('from').get('id')
        text = response.get('message').get('text')
        if text == '안녕':
            answer = '안녕하세요!'
        else :
            answer = '안녕 말고는 무슨 말인지 못알아들어요.'
        requests.get(url + f'sendMessage?chat_id={chat_id}&text={answer}')    #안녕이라고 말한건 그대로 받아치는데 안녕말고 다른말은 못알아듣는척 하는 if문

    return '', 200











if __name__ == '__main__':   # 이름이 메인코드면
    app.run(debug=True)      # 디버그를 True로 기억하겠다.