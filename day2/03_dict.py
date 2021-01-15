# dictionay

# 딕셔너리 선언
my_dict = {
    '지역' : '구미', # '지역'이라는 key값이 가지고 있는 '구미'라는 value를 지정함
    '반' : '2반'
}

# 요소에 접근하는 방법
print(my_dict['지역'])
print(my_dict.get('지역'))

# 요소를 변경하는 방법
my_dict['지역'] = 'gumi'
print(my_dict['지역'])

# [] 접근과 .get 접근의 차이
print(my_dict.get('이름'))
print(my_dict['이름'])