# 에디터
# https://www.acmicpc.net/problem/1406

# 백준형 해설: 커서를 기준으로 왼쪽 스택, 오른쪽 스택으로 나눠서 문제를 해결 (진짜 이런걸 어케 생각하는겨)

# 내가 쓴 거
import sys
input = sys.stdin.readline # 시간초과 때문에
s = input()
m = int(input())
left_stack = list(s[:-1]) # 첫시작 커서는 입력받은 문자열 제일 끝이기 때문.
right_stack = []

for _ in range(m):
    cmd = input().split()
    
    if cmd[0] == 'L': # 커서 왼쪽으로 이동
        if len(left_stack):
            right_stack.append(left_stack.pop())
    elif cmd[0] == 'D': # 커서 오른쪽으로 이동
        if len(right_stack):
            left_stack.append(right_stack.pop())
    elif cmd[0] == 'B': # 커서 왼쪽에 문자 삭제
        if len(left_stack):
            left_stack.pop()
    elif cmd[0] == 'P': # 커서 왼쪽에 문자 추가
        left_stack.append(cmd[1])
result = ''.join(left_stack) + ''.join(right_stack[::-1]) # right_stack[::-1]으로 하는 이유:
print(result)                                             # 스택에 뒤에것부터 쌓이기 떄문에
                                                          # 역순으로 해야 원래 문장과 같아짐.

# 백준이 쓴 코드            
import sys
input = sys.stdin.readline
left = list(input().strip())
right = []
m = int(input())
for _ in range(m):                 # strip()은 문자열의 시작과 끝에 있는 줄바꿈과 공백을 제거
    line = input().strip().split() # stirp()을 통해 \n을 지움.
    what = line[0]
    if what == 'L':
        if left: # 굳이 len을 사용할 필요가 없었다ㅎ
            right.append(left.pop())
    elif what == 'D':
        if right:
            left.append(right.pop())
    elif what == 'P':
        left.append(line[1])
    elif what == 'B':
        if left:
            left.pop()
left += right[::-1] # 리스트를 먼저 합치고
print(''.join(left)) # 한번만 join해도 됬었음ㅎ