import sys

input()

numdict = {}
for num in map(int, sys.stdin.readline().split()):
    val = numdict.get(num, 0)
    numdict[num] = val + 1

input()


answer = []             # 이게 좀 더 빠르다.
for ans in map(int, sys.stdin.readline().split()):
    answer.append(numdict.get(ans, 0))

print(*answer, sep='\n')

'''이 버전의 코드가 더 빠를 수 있는 이유는 여러 가지 요소에 기인합니다:

출력 처리의 효율성: 마지막 버전에서는 print 함수를 반복문 내에서 여러 번 호출하는 대신, 결과를 리스트에 저장하고 한 번에 출력합니다. 이 방식은 출력 버퍼링을 효율적으로 관리하여 출력 호출의 오버헤드를 줄일 수 있습니다.

입출력 최적화: 표준 출력을 사용할 때, 각각의 print 호출은 시스템 호출을 발생시키며, 이는 상대적으로 비용이 많이 드는 작업입니다. 결과를 한 번에 출력함으로써 시스템 호출의 수를 줄이고 전체 실행 시간을 단축할 수 있습니다.

메모리 관리: 리스트에 결과를 저장하는 방식은 메모리 사용을 조금 더 많이 하지만, 이는 대량의 데이터를 빠르게 처리할 때 일반적으로 더 효율적입니다.

결과적으로, 이러한 최적화들은 특히 큰 데이터 세트를 처리할 때 더 빠른 성능을 제공할 수 있습니다. 각 요소별로 발생할 수 있는 지연을 줄이는 것이 전체적인 성능 향상에 기여합니다.
'''

'''for ans in map(int, sys.stdin.readline().split()):
    print(numdict.get(ans, 0))'''
