# 사회자가 임의의 염소가 담긴 문을 열어준다는 전제를 삭제한 경우
# 항상 1번문(0번 index)를 처음으로 선택하고, 나머지 문에 염소만 있다고 가정했을 때 사회자가 2번문만 열어주는 경우

from random import choice
from random import shuffle

def conversion(result, times):
    return round(result/times, 2) * 100

list = ['G1', 'G2', 'C']

success = 0        # 성공을 카운팅

times = 12500
count = times

for i in range(times):
    shuffle(list)
    if list[1] == 'C':
        count -= 1
        continue
    # 2번문 안에 C가 있을 시 염소를 공개한다는 대전제를 위반하므로, 이 케이스는 아예 빼버리기

    if list[0] == 'C':
        # 첫 번째로 C를 선택했다면, 남은 두 문중 반드시 2번문(1번 인덱스)은 소거
        choosen = choice([0, 2])
        # 그러므로 남은 선택지는 1, 3번 문 밖에 없기에, 둘 중 하나를 무작위 선택
        if list[choosen] == 'C':
            success += 1
    else:
        choosen = choice([0, list.index('C')])
        # 첫 번째로 G를 선택했다면 자기자신과 C가 들어있는 문 중 선택
        if list[choosen] == 'C':
            success += 1

print(f"승률: {round(success/count * 100, 2)}%")