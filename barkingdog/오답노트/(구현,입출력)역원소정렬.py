import sys

data = list(map(str, sys.stdin.readline().split()))
n = int(data[0])
new_data = data[1:]
while True:
    input = sys.stdin.readline()
    if not input:
        break
    new_data += list(input.split())

def rev(arr):
    dummy = []
    for i in range(len(arr) - 1, -1, -1):
        dummy.append(arr[i])
    return int(''.join(dummy))

new_data.sort(key= lambda x: rev(x))
for i in new_data:
    print(rev(i))