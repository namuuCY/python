import sys

# split()은 공백 문자(스페이스), 탭(\t), 개행 문자(\n)를 
# 포함한 모든 공백 문자를 기준으로 문자열을 분리
# read는 EOF가 뜰때까지 모든 입력값을 한줄의 str으로 반환, 개행문자 포함
# readline은 한줄만읽고 str으로반환, 개행문자포함
# readlines는 모든 줄 읽고 list로 반환, 이때 list의 원소들은 모두 str, 개행문자포함

print(*sorted([int(number[::-1]) for number in sys.stdin.read().split()[1:]]), sep = '\n')