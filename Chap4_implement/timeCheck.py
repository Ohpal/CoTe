#########
# 시각 p.114
# 시각을 입력해서 3이 포함된 시, 분, 초의 개수를 구함
#########

# 하루 = 86,400 (24 * 60 * 60)

# 시간 입력 받기
h = int(input())

count = 0
for i in range(h + 1):          # 0 ~ 23
    for j in range(60):         # 0 ~ 59
        for k in range(60):     # 0 ~ 59
            # 매 시각 안에 '3'이 포함되어 있으면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                print(i, j, k)
                count += 1

print(count)
