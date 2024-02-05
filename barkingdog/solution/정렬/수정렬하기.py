n = int(input().rstrip())
nums = []
for _ in range(n):
    nums.append(int(input().rstrip()))
nums.sort()

print(*nums, sep = '\n')