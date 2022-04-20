"""
https://www.acmicpc.net/problem/7576
"""

import sys
from collections import deque
sys.stdin = open('input.txt', 'r')

def find_1(arr):
    res = []
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                res.append([r, c])
    return res


def BFS(arr, ripen):
    queue = deque()
    res = 0
    for ri in ripen:
        queue.append(ri)

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                arr[nr][nc] = arr[r][c] + 1
                if arr[nr][nc] - 1 > res:
                    res = arr[nr][nc] - 1
                queue.append([nr, nc])


    for r in arr:
        if 0 in r:
            return -1

    return res


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ripen = find_1(arr)
answer = BFS(arr, ripen)

print(answer)