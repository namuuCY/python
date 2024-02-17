import sys
str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()
lena = len(str1)
lenb = len(str2)
DP = [[0] * (lenb + 1) for _ in range(lena + 1)]    # [a][b] str1, str2

# DP[i + 1][j + 1] : i,j번째 문자가 같으면 추가함.

for i in range(0, lena):
    for j in range(0, lenb):
        if str1[i]==str2[j]:
            DP[i + 1][j + 1] = DP[i][j] + 1
        else:
            DP[i + 1][j + 1] = max(DP[i][j + 1], DP[i + 1][j])

print(DP[lena][lenb])