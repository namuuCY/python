import sys

# 백준 https://www.acmicpc.net/problem/1991

N = int(input())
data = sys.stdin.read().split()

def preDFS(root):
    
    if 


tree = set()
prelist = []
inlist = []
postlist = []

for i in range(N):
    tree[data[3 * i]] = (data[3 * i + 1], data[3 * i + 2])
# '.' 이면 continue인거, 해당값이 
