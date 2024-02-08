import sys; input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [tuple(map(int, input().split())) for _ in range(N)]
# 정보를 바꾸지 않는다면 tuple이 immutable이라 메모리측면과 속도측면에서 미세하게 빠름

DP = {0:0}

for w, val in stuff:
    tmp = {}
    for totw, totv in DP.items():   # .items() : key와 value의 순서쌍을 iterator
        if totw + w <= K and DP.get(totw + w, 0) < totv + val:  
            tmp[totw + w] = totv + val      # .get(key값, default) key값이 있으면 그에대한 value를,
    DP.update(tmp)                          # 없으면 default값을 반환함.
                # .update(tmp)  tmp라는 사전자료형을 DP 사전자료형에 업데이트함.
print(max(DP.values()))             
        # .values() 는 value값들을 iterator로 반환
        # .