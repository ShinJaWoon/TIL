# 다음 아래 3줄은 예제 파일로 테스트 하기 위함. 제출할 땐 주석처리 할 것
# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w')

# 다음은 시간 측정 코드
import time
start = time.time()
# print(time.time()-start)

def check(n):
    h = n // 100
    t = n // 10 - h*10
    u = n % 10

    if (h-t) == (t-u):
        return 1
    else:
        return 0

def hundreds(n):
    cnt = 0
    for i in range(100, n+1):
        cnt += check(i)
    return cnt + 99



N = int(input())
if N < 100:
    print(N)
else:
    print(hundreds(N))


            







print(time.time()-start)