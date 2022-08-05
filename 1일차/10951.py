# A+B - 4 
# 입력이 몇 개 주어지지 않은 경우에는
# 입력을 EOF(End Of File)까지 받으면 된다!

while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except: # EOF의 경우
        break