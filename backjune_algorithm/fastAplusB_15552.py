import sys

# 개수 입력
iterNum = int(sys.stdin.readline().rstrip())

for i in range(iterNum):
    arguments =  sys.stdin.readline().rstrip().split(' ')
    print(sum ( [int(a) for a in arguments] ))