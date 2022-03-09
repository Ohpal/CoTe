################
# 그리디 알고리즘 : 현재 상황에서 지금 당장 좋은것만 고르는 방법
# 거스름돈 p.90
################

try:
    money = int(input('금액을 입력하세요>>'))
except ValueError:
    money = 0
    print('숫자만 입력하세요')

count = [0, 0, 0, 0]

# 큰 단위 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

# for coin in coin_types:
for idx, coin in enumerate(coin_types):
    count[idx] += money // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수
    money %= coin   # 거슬러주고 남은 금액

print(count)
