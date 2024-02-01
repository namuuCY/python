N = int(input().rstrip())
board = [[0] * N for _ in range(N)]
K = int(input().rstrip())
for _ in range(K):
    i, j = map(int, input().split())
    board[i][j] = 2
L = int(input().rstrip())
order = {}
for _ in range(L):                  # 시간 따라서 어떻게 구현하는지 팁없냐
    X, C = map(str, input().split()) 
    x = int(X)
    c = 1 if C == 'D' else -1
    order[x] = c

dx = [0, 1, 0, -1]  # 0이 동쪽 dir증가하면 오른쪽 90도 감소하면 왼쪽 90도
dy = [1, 0, -1, 0]
posx, posy = 0, 0
dir = 0
board[posx][posy] = 1
time = 0
is_exit = False

while not is_exit:
