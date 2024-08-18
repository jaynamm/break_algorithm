import sys

n = int(sys.stdin.readline())
t = []
p = []

for _ in range(n):
    time, pay = map(int, sys.stdin.readline().split())
    t.append(time)
    p.append(pay)

dp = [0] * (n + 1)

for i in range(n-1, -1, -1):
    # print(i+1, "일 : 기간 = ", t[i], " / 금액 = ", p[i])
    
    # 상담일이 초과되는 경우
    if i + t[i] > n:
        # 다음 날과 같은 금액을 받는다.
        dp[i] = dp[i+1]
        
        # print("상담일 초과 : ", i + t[i], ", 금액 : ", dp[i])
    # 상담일이 충분한 경우
    else:
        # 다음 날 받는 금액과 현재 받을 수 있는 금액을 비교한다.
        dp[i] = max(dp[i+1], p[i] + dp[i+t[i]])
        
        # print("상담일 충분 : ", dp[i])
        
print(dp[0])