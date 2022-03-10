#########
# 1이 될 때까지 p.100
#########
import time


n, k = map(int, input().split())

start_time = time.time()

condition = False

if 2 <= n <= 100000 and 2 <= k <= 100000 and n >= k:
    condition = True

result = 0

if condition:
    # n이 k 이상이라면 k로 계속 나누기
    while n >= k:
        # n이 k로 나누어 떨어지지않으면 n에서 1씩 빼기
        while n % k != 0:
            n -= 1
            result += 1
            print(n)

        n //= k
        result += 1
        print(n)

    while n > 1:
        n -= 1
        result += 1
        print(n)

    print('time : ', time.time() - start_time)
    print('result : ', result)
