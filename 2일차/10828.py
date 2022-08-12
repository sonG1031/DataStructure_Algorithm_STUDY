# 스택 구현하기
# https://www.acmicpc.net/problem/10828

# 교훈)
# • 코드를 더 간결하고 효율적으로 쓰는 방식을 점검해보자.
# • 파이썬의 문법을 최대한 활용해보자!

# 내가 구현한 스택 (문제점을 확인하고 고쳐보자!)
# 문제점)
# 1. 다른 언어에서 사용할 법한 코드 구조를 사용함.
# ▶︎ 좀 더 파이써닉한 코드를 작성하자!

import sys # 시간초과 떄문에

stack = []
s = 0

def push(num):
    global stack
    global s
    stack.append(num)
    s += 1

def pop():
    global stack
    global s
    if s == 0:
        print(-1)
    else:
        print(stack[s-1])
        del stack[s-1]
        s -= 1

def size():
    global s
    print(s)

def empty():
    global s
    if s == 0:
        print(1)
    else:
        print(0)

def top():
    global stack
    global s
    if s == 0:
        print(-1)
    else:
        print(stack[s-1])

# n = int(input()) # 명령의 수 
n = int(sys.stdin.readline()) # 시간초과 때문에

for i in range(n):
    # calc = input().split()
    calc = sys.stdin.readline().split() # 시간초과 때문에
    if calc[0] == 'push':
        push(int(calc[1]))
    elif calc[0] == 'pop':
        pop()
    elif calc[0] == 'size':
        size()
    elif calc[0] == 'empty':
        empty()
    elif calc[0] == 'top':
        top()

# 백준이 구현한 스택
import sys
input = sys.stdin.readline # 아마 채점과정에서 시간초과를 피하기 위해서..
n = int(input())
stack = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    if cmd == 'push':
        num = int(s[1])
        stack.append(num)
    elif cmd == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        print(0 if stack else 1) # 조건부 표현식
    elif cmd == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)