# 숫자 1부터 45까지 중 무작위 6개를 뽑아서 출력해주는 코드를 작성해 보세요.
#random.sample을 사용할 겁니다.

import random # random 모듈 사용하기 위해 가져오기
arr = [] # 숫자 넣을 박스 만들기
for i in range(1, 46): # 포문돌려서 1~46의 범위로
    arr.append(i)      # 박스에 숫자추가하기

s = random.sample(arr, 6) #숫자 들어가있는 박스에서 6개 랜덤하게 뽑기
s.sort() #정렬하기
print(s) #랜덤하게 뽑고 정렬까지한거 출력하기