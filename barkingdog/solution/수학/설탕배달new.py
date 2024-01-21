n = int(input())

limit = n // 5
found = False

for i in range(limit, -1, -1):
    if (n - 5 * i) % 3 == 0:
        print(i + (n - 5 * i) // 3)
        found = True
        break

if not found:
    print(-1)