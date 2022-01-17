```python
# 변수명을 잘못 적었을 경우 ex) print
# 변수명을 지우고 실행시킨다.
del 변수명


# 변수 값 확인
print(변수명, type(변수명))

# 출력 방법
print('{}{}'.format( , ))
print(f'{변수이름}')  --> 변수가 바로 줄력됨



import random
# 리스트에서 하나 뽑는 코드
변수 = random.choice(리스트)
# data에서 갯수만큼 뽑는 코드
변수 = random.sample(data, 갯수)


# 수열 리스트로 저장
변수 = list(range(시작, 끝+1))
# 홀수만 저장
변수 = list(i for i in range(시작, 끝+1) if i % 2 == 1)

# 리스트에서 특정 조건을 만족하는 필터로 거른 값
변수 = list(filter(lambda x: x에 대한 식, 리스트데이터))

# 리스트 값을 특정 식으로 바꾸는 방법
변수 = list(map(lambda x: x에 대한 식, 리스트데이터))

# 여러 입력을 정수로 변환해 리스트로 저장하는 방법
변수 = list(map(int, input().split(",")))

# 딕셔너리 키 밸류 따로 for 문 돌리는 법
for key, value in data.items():

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

```

