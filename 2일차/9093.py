# 단어 뒤집기
# https://www.acmicpc.net/problem/9093

# 교훈)
# 1. 스택을 사용하여 푸는 방식을 터득하자.
# 2. 파이썬을 좀 더 공부하자.

# 내가 구현한 코드 (스택을 사용하지 않음ㅋㅋ)
import sys
input = sys.stdin.readline # 시간초과 방지

t = int(input())

for _ in range(t):
    sentence = input().split()
    for word in sentence:
        out = "".join(list(reversed(word)))
        print(out, end=' ')
    print()


# 백준이 구현한 코드
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input()
    stack = []
    for ch in s:
        if ch == ' ' or ch == '\n': 
            print(''.join(stack[::-1]), end='')
            stack.clear()
            print(ch, end='')
        else:
            stack.append(ch)