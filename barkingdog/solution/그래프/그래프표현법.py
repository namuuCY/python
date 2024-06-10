# 인접행렬을 이용하는 방법
# 어떤 두 간선이 연결되어있는지를 O(1)에 알수있고, O(V^2)의 공간을 필요로함
# 관례상 노드를 0이 아닌 1부터 표현함.
adj_maxtrix = [[0,0,0,0,0],
               [0,0,1,1,0],
               [1,0,0,0,1],
               [1,0,0,0,0],
               [0,1,0,1,0]]   # 방향그래프 : [1][3]=1 이라는건 
                              #             2번째노드에서 4번째 노드로 가는 간선이 1개 존재
 
adj_matrix2 = [[0,0,1,1,0],
               [0,0,1,1,0],
               [1,1,0,0,1],
               [1,1,0,0,1],
               [0,1,1,1,0]]   # 무방향그래프 얘는 대칭행렬임


# 인접 리스트를 이용하는 방법
# 정점이 많고 간선이 상대적으로 적을때 사용.
# 리스트가 V개 필요하고, 간선이 1개있을때마다 1개의 원소가 추가됨(방향이 없을시 2개).
# 방향
adj_list = 1