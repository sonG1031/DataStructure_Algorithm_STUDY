# 스택 수열
# https://www.acmicpc.net/problem/1874

# 교훈)
# 문제를 제대로 이해하지 못했음(핑계임ㅋ)
# 이 문제는 간단하게 설명하면
# 1부터 n까지의 수를 스택에 넣었다가 pop함으로써, 하나의 수열을 만듬.
# 이때 이 수열을 만드는 과정에서 push, pop을 +,-로 기록하고 출력해야하며
# 이런 과정에서 수열이 안만들어지면 NO출력.

# 나중에 다시와서 곱씹어보자!

import sys
input = sys.stdin.readline
n = int(input())
a = [int(input()) for _ in range(n)] # 판단할 수열, 표현식임.. 잘은 모름
m = 0 # 스택에 넣어야할 수 (넣어야할 수가 아직 없으므로 0)
stack = [] # 스택에 pop된것들이 수열로 들어가야하는 수임(즉, 변수x의 값을 pop해주기 위한~~)
ans = '' 

for x in a:
    if x > m: # 입력받은 x가 m보다 크다면 m을 pop해 줘야하므로 m~x까지 스택에 추가한다
        while x > m:
            m += 1
            stack.append(m)
            ans += '+\n'
        stack.pop()
        ans += '-\n'
    else: # m > x , m == x 인 경우
        if stack[-1] != x: # m > x 인 경우(수열이 만들어질 수 없는 경우가 됨)
            print('NO')
            sys.exit(0)
        stack.pop() # m == x, stack[-1]이 x와 같음.
        ans += '-\n'
print(ans, end='')