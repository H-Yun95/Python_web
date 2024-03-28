# 두 번째 선택을 반드시 바꾼다는 가정

from random import randrange

list = ['G1', 'G2', 'C']
result = 0
times = 100000


for i in range(times):
    choice = randrange(0,3)
    # 경우의 수 0, 1, 2 중 하나를 무작위로 할당
    if list[choice] == 'C':
        continue
    # 첫 번째로 C를 골랐을 경우, G1이나 G2를 공개한다면 남아있는 문에는 반드시 G가 있으므로 게임 종료
    else:
        result += 1
    # 첫 번째로 G1, G2 중 하나를 골랐을 경우 사회자가 남은 두 선택지중 G를 소거해주므로 무조건 C로 바꿈.

print(f'{round(result/times, 2) * 100}%')
# "승리 결과 / 총 게임수"로 승리 확률 계산