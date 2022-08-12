# 괄호
# • 괄호 문자열이 주어졌을 때, 올바른 괄호 문자열인지 아닌지 알아보는 문제
# https://www.acmicpc.net/problem/9012

# 교훈)
# 이 문제는 스택에 직접 push, pop을 하지 않아도 해결할 수 있는 문제이다.
# 스택에는 어차피 여는괄호만 저장하고, 로직에서 직접 저장한 데이터를 사용하지 않기 때문에
# 스택의 개수만을 이용해서 해결가능.

# 내가 구현한 코드
import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    s = input()
    stack = []
    for ch in s:
        if ch == ')':
            if len(stack): 
                stack.pop() # 여는괄호가 스택에 있는 경우 (즉, 짝이 맞는 경우)
            else: # 여는괄호가 없는데 닫힌 괄호가 있는 경우로
                print('NO') # 짝이 맞을 수 없음, 그래서 NO
                break
        elif ch == '\n': # s의 끝 부분
            if len(stack): # 스택에 남은 여는괄호가 존재하면
                print('NO') # 짝이 맞지 않은 것이므로 NO
            else:
                print('YES') # 스택이 비어있으면 짝이 다 맞은 것. 그래서 YES
        else:
            stack.append(ch) # 여는괄호 이므로 push
    
# 백준이 구현한 코드
def valid(s):
    cnt = 0 # 스택에 저장된 수
    for ch in s:
        if ch == '(': 
            cnt += 1 # push
        else:
            cnt -= 1 # pop
        if cnt < 0: # ')'(닫는괄호)의 짝이 없어 음수가 된 경우
            return 'NO'
    if cnt == 0:
        return 'YES' # 모두 짝이 맞아 스택에 남은 '('(여는괄호)가 없음
    else:
        return 'NO' # 짝이 맞지 않아 '('(여는괄호)가 남은 경우
t = int(input())
for _ in range(t):
    print(valid(input()))