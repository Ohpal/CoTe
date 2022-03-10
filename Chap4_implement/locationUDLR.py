#########
# 상하좌우 좌표 찾기 p.112
#########

# 정사각형 좌표 크기 입력
size = int(input())

# 초기 좌표 설정
x, y = 1, 1


# 이동 계획(U D L R)
plans = input().split()

# U D L R에 따른 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['U', 'D', 'L', 'R']

print(x, y)

# 이동 계획 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            print(nx, ny)
    # 공간을 벗어나는 경우는 무시
    if nx < 1 or ny < 1 or nx > size or ny > size:
        continue
    # 이동 수행
    x, y = nx, ny
    print('real>>', x, y)
print('final>>', x, y)
