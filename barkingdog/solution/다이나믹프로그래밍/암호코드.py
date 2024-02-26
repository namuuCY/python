import sys
code = sys.stdin.readline().strip()
N = len(code)
DP = [0] * (N + 1)
if code[0] == '0':
    print(0)
else:
    DP[0] = 1
    DP[1] = 1
    if N >= 2:
        for i in range(1, N + 1):
            if code[i - 1] == '0' and not (code[i - 2] == '1' or code[i - 2] == '2'):
                print(0)
                exit(0)
            elif code[i - 1] == '0' and (code[i - 2] == '1' or code[i - 2] == '2'):
                DP[i] = DP[i - 2]
            elif 11 <= int(code[i - 2]) * 10 + int(code[i - 1]) <= 19 or 21 <= int(code[i - 2]) * 10 + int(code[i - 1]) <= 26:
                DP[i] = (DP[i - 1] + DP[i - 2]) % 1000000
            else: DP[i] = DP[i - 1]
    print(DP[N])


