def stat(n:int, x:int, y:int):
    if n == 1:
        board[x][y] = '*'
        return
    else:
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1:
                    continue
                stat(n // 3, x + n//3 *i, y + n//3 *j)


n = int(input())
board = [[' '] * n for _ in range(n)]   # [[' ' for _ in range(n)] for _ in range(n)]
stat(n, 0, 0)                                        # 이게 독립적인 객체를 가진애를 만드는법. mutable한걸루
for i in range(n):
    print(''.join(board[i]))