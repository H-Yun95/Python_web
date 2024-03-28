# 완전히 무작위로 선택

from random import randrange
from random import choice

def conversion(result, times):
    return round(result/times, 2) * 100

list = ['G1', 'G2', 'C']

success = 0     # 성공을 카운팅

times = 12500

for i in range(times):
    choosen = randrange(0,3)
    # 3개의 선택지(0, 1, 2) 중 하나를 선택
    choosen_2 = choice([choosen, list.index('C')])
    # 사화자가 G 중 하나를 소거해 주므로, 두 번째 선택은 자기 자신과 C의 인덱스 중 무작위 선택
    # 아마 딜레마가 일어나는 지점으로 예상
    if list[choosen_2] == 'C':
        success += 1

print(f"승률: {round(success/times * 100, 2)}%")