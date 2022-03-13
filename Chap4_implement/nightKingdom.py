#########
# 왕실의나이트 p.117
#########

# 현재 나이트 위치 입력받기(ex: a1, a3, c7)
night_location = input()
row = int(night_location[1])
column = int(ord(night_location[0])) - int(ord('a')) + 1

# 나이트가 이동할수있는 위치 리스트
steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, 1), (2, -1)]

# 이동 가능한 방향인지 확인
result = 0
for step in steps:
    # 이동하고자하는 위치 확인
    next_row = row + step[0]
    next_column = column + step[1]
    if 1 <= next_row <= 8 and 1 <= next_column <= 8:
        result += 1
        print(next_row, next_column)

print(result)
