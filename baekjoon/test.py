import sys

num = int(input())
num_first = num
cnt = 0

while 1:
    if num < 10:
        a = 0
        b = num
    else:
        a = num // 10
        b = num % 10
    c = a + b
    num = b*10 + c%10
    cnt += 1
    if num == num_first:
        break

print(cnt)