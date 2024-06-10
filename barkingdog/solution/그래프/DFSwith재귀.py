# DFS와 재귀는 밀접하다.

# 스택메모리 제한이 작을 경우에는 재귀깊이가 클경우 메모리 초과될경우도 있음.

# 참고로 스택을 사용하면 FILO 이고 재귀는 들어오는것마다 하기 때문에 방문 순서가 달라진다.

# 일반적으로 우리가 상상하는 DFS의 방식은 재귀 DFS의 방식쪽임.

'''adj = [[1,2],[2],[3],[0,1,2]]
vis = [False] * 4

def DFS(cur):
    vis[cur] = True
    print(f'{cur}번 노드 방문')
    for nxt in adj[cur]:
        if vis[nxt]: continue
        DFS(nxt)

DFS(0)'''

'''참고로, 재귀와 같은 순서로 방문하게 하려면 
    
    기존 DFS에서처럼 push(append)할때 vis하는게 아닌
    pop 할때 vis하면 됨'''


from collections import deque
Q = deque()

adj = [[1,2],[2],[3],[0,1,2]]
vis = [False] * 4

def DFS(a):
    Q.append(a)
    while Q:
        cur = Q.pop()
        if vis[cur]: continue       # 여기가 제일 중요. 이거 없으면 무한루프 빠진다
        vis[cur] = True  
        print(f"Visited node {cur}")
        for nxt in adj[cur]:
            if vis[nxt]: continue
            Q.append(nxt)
              

DFS(0)