#########
# 큰수의 법칙 p.95
#########

n, m, k = map(int, input('').split())
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

# 가장 큰수가 더해지는 횟수
count = int(m / (k+1)) * k
count += m%(k+1)

result = 0
result += count * first     # 가장 큰수 더하기
result += (m - count) * second      # 두번쨰로 큰수 더하기

print(result)
