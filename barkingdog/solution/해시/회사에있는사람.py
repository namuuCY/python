import sys

IOlog = set()
for _ in range(int(input())):
    name, method = map(str, sys.stdin.readline().split())
    if method == 'enter':
        IOlog.add(name)
    else:
        IOlog.remove(name)

sys.stdout.write('\n'.join(sorted(IOlog, reverse=True)))