menu = ["김치찌개", "짜장면", "국밥"]
# print(menu)
# print(menu[1])

# ramdom module 사용하기

# 1. ramdom 가져오기
import random
# 2. ramdom 모듈이 가지고 있는 choice함수를 사용해서 menu리스트로부터 무작위 값 하나 반환받기
dinner = random.choice(menu)
print(dinner)