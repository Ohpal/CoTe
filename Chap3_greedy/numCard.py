#########
# 숫자 카드 게임 p.98
#########

n, m = map(int, input().split())  # n, m 행 렬

result = 0

# 한줄씩 입력받아 확인
for i in range(n):
    data = list(map(int, input().split()))
    # 현재 행에서 가장 작은 수 찾기
    min_value = min(data)
    result = max(result, min_value)     # 두수중 큰수를 저장

print(result)