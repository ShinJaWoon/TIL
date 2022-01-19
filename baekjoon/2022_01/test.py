# 다음 아래 3줄은 예제 파일로 테스트 하기 위함. 제출할 땐 주석처리 할 것
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')

import sys
C = int(input())
for idx in range(C):
    data = list(map(int, sys.stdin.readline().split()))
    N = data[0]
    scores = data[1:]
    average = sum(scores) / N
    per = len(list(filter(lambda x: x > average, scores)))/ N * 100
    print(f'{per:.3f}%')



