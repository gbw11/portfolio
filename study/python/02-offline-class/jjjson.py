#  json과 dictionary의 공통점
# key : value 형태로 되어있다.

# json과 dictionary의 차이점
# 1. json의 key는 반드시 문자열이어야 한다. 큰따옴표("")로 감싼다!!
'''
1. 문자열(string) : "Hello World" ---> 반드시 큰 따옴표
2. 숫자(Number) : 27, 31.4 ---> 정수 실수 나누지 않고 Number
3. 불리언(Boolean) : true, false ---> t와 f가 소문자
4. Null ---> python의 None과 같다.
5. 객체(Object) : {} ---> 파이썬의 딕셔너리
6. 배열(Array) : [] ---> 파이썬의 리스트
'''

import requests

url = ('https://api.tvmaze.com/singlesearch/shows?q=narcos&embed=episodes')

r = requests.get(url).text


print(r)