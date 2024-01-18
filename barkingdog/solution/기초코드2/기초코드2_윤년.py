year = int(input())
cnt = 0
if year % 4 == 0:
    cnt += 1

if year % 100 == 0:
    cnt -= 1

if year % 400 == 0:
    cnt += 1

print(cnt)
