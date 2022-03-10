# twoArray = [[1,2,3],[4,5,6],[7,8,9]]

size = int(input())

# 이동 계획(U D L R)
plans = input().split()

arr = []

for x in range(0, size):
    for y in range(0, size):
        twoArray = [0 for aa in range(size)]
    arr.append(twoArray)


# 초기 좌표 설정
x, y = 0, 0

# U D L R에 따른 이동 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['U', 'D', 'L', 'R']

# 이동 계획 확인
def print_arr():
    for n in range(len(arr)):
        print(arr[n])


for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            arr[x][y] = 0   # 이동하고난 자리는 0으로 초기화

    # 공간을 벗어나는 경우는 무시
    if nx < 0 or ny < 0 or nx > size-1 or ny > size-1:
        continue
    # 이동 수행
    x, y = nx, ny
    arr[x][y] = 1   # 이동 수행이되면 1로 초기화
    print_arr()
    print()