```python
## VS code
# alt + shift + 방향키 = 복사
# alt + 방향키 = 이동


# 변수명을 잘못 적었을 경우 ex) print
# 변수명을 지우고 실행시킨다.
del 변수명


# 변수 값 확인
print(변수명, type(변수명))

# 출력 방법
print('{}{}'.format( , ))
print(f'{변수이름}')  --> 변수가 바로 줄력됨

# 같은줄에 계속 출력
print('', end = "")

# slicing
# 거꾸로 바꾸기
list2 = list1(::-1)
# 2칸마다 얻기
list2 = list1(::2)

import random
# 리스트에서 하나 뽑는 코드
변수 = random.choice(리스트)
# data에서 갯수만큼 뽑는 코드
변수 = random.sample(data, 갯수)

# sum 활용, 2차원 1차원으로 만들기
a = sum(순환객체, 시작값)
# 시작값은 기본 0, []로 설정하면 2차원을 1차원으로 바꾼다.

# 수열 리스트로 저장
변수 = list(range(시작, 끝+1))
# 홀수만 저장
변수 = list(i for i in range(시작, 끝+1) if i % 2 == 1)

# 리스트에서 특정 조건을 만족하는 필터로 거른 값
변수 = list(filter(lambda x: x에 대한 식, 리스트데이터))

# 리스트 값을 특정 식으로 바꾸는 방법
변수 = list(map(lambda x: x에 대한 식, 리스트데이터))


# 입력
# 여러 입력을 정수로 변환해 리스트로 저장하는 방법
변수 = list(map(int, input().split(",")))
# split() 안에 아무것도 안넣으면 공백 여러개나 엔터도 처리해준다.
a, b = map(int, input().split())

# 숫자 리스트를 하나씩 띄어서 출력
result = ' '.join(map(str, list))


"""
data = []
for i in range(n):
    data.append(int(input().split()))
"""
# 정해진 입력의 끝이 없는 경우
# 파일이 끝까지 가면 EOFError를 발생시킨다. 에러가 나면 멈추도록 try, except를 사용한다.
            
# 반복문으로 많은 입력을 받을 때
import sys
# sys.stdin.readline()은 줄 단위로 받기 때문에 개행도 받음
# 한개
a = int(sys.stdin.readline())
# 정해진 개수 한 줄에 입력
a, b, c = map(int,sys.stdin.readline().split())


# 임의의 개수 한 줄에 입력
data = list(map(int,sys.stdin.readline().split()))
# 임의의 개수 정수를 n줄 입력받아 2차원 저장
data = []
n = int(sys.stdin.readline())	# n = int(input())도 가능
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))
# 문자열 n줄 리스트 저장
# strip()은 문자열 맨 앞과 맨 끝 공백 제거
# rstrip()은 오른쪽 공백 제거, lstrip()은 왼쪽 공백 제거
n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]
           

# 딕셔너리 키 밸류 따로 for 문 돌리는 법
for key, value in data.items():
           
# 날짜, 시간 함수
import datetime
today = datetime.datetime.now()
print(today)
print(f'오늘은 {today:%y}년 {today:%m}월 {today:%d}일 {today:%A}')           

# 가변형 인자
def 함수명(*x):
         
    return ~~~~

함수명(1, 2, 3, 4, 5)



# 클래스
class class_name:
    def __init__(self, one, two):
        self.__one = one
        self.__two = two
        
    @property
    def one(self):
        return self.__one
    @property
    def two(self):
        return self.__two
    
    
    def function(self):
        return self.one * self.two

           
# 버블 정렬
# 인접한 두 수를 비교하여 큰 수를 맨 뒤로 보낸다.
# 한 번 루프가 돌면 맨 끝에 가장 큰 수가 가게 된다.
# 첫 번째 for문이 한 번 돌 때마다 맨 뒤에 정렬되는 숫자가 하나씩 늘어나므로
# 두 번째 for문에서는 첫 번째 for 문이 돈 수만큼 돌지 않아도 된다.
# 첫 번째 루프는 리스트 길이 만큼 돌기 위함
# 두 번째 루프는 비교하며 바꾸기 위함
for i in range(num_len-1):
    for j in range(num_len-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

            
# 행렬 회전
print('------전치--------')
lst2 = list(map(list, zip(*lst)))

print('------반시계90도--------')
lst3 = list(map(list, zip(*lst)))[::-1]

print('------시계90도--------')
lst4 = list(map(list, zip(*lst[::-1])))

##파일 열기
with open('파일명') as f:
    read_data = f.read
f.close()


# 예제 입력, 출력
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

# 예제 시간 측정
import time
start = time.time()
print(time.time()-start)


import json
x = [1, 2, 3]
x.json.dump


# 딕셔너리 접근 방법
dict.get(key, default)	# None 값으로 들어감
dict.get(key, <임의값>)	# 임의 값이 들어감

# 파일 열기
a_json = open('<파일위치>.json', encoding='UTF8')
a = json.load(a_json)

# 딕셔너리 키 바꾸기
dictionary[new_key] = dictionary[old_key]
del dictionary[old_key]
```

