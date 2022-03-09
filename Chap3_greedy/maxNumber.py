#########
# 큰수의 법칙 p.93
#########

# n, m, k으로 입력 자연수 공백으로 구분
n, m, k = map(int, input('첫째줄').split())
data = list(map(int, input('둘째줄').split()))     # data의 list 수는 n개

data.sort()  # 입력받은 수 정렬
first = data[n - 1]  # 가장 큰 수
second = data[n - 2]  # 두번째로 큰 수
print('first', first)
print('second', second)

result = 0

while True:
    for i in range(k):      # 가장 큰 수 K번 더하기
        if m == 0:      # m이 0이면 for문 탈출
            break
        result += first
        print('1', result, end=' ')
        m -= 1  # 더할때마다 1 빼기
    if m == 0:      # m이 0이면 while문 탈출
        break
    result += second    # 두번쨰로 큰수를 한번 더하기
    print('2', result)
    m -= 1

print(result)



