# 두 번째 선택을 반드시 바꾼다는 가정

from random import randrange
from random import choice

def conversion(result, times):
    return round(result/times, 2) * 100

list = ['G1', 'G2', 'C']

choose_car = 0               # 첫 번째로 C를 고르는 경우
choose_goat_change_s = 0     # 첫 번째로 G를 고르고, 바꿨을 때 승리하는 경우 
choose_goat_change_d = 0     # 첫 번째로 G를 고르고, 바꿨을 때 패배승리하는 경우
choose_goat_unchange_s = 0   # 첫 번째로 G를 고르고, 바꾸지 않았을 때 승리하는 경우
choose_goat_unchange_d = 0   # 첫 번째로 G를 고르고, 바꾸지 않았을 때 패배하는 경우

times = 12500

for i in range(times):
    choosen = randrange(0,3)
    if list[choosen] == 'C':
        choose_car += 1
    # 앞과 마찬가지로, C를 고르는 즉시 패배

    else:
        choosen_2 = choice([choosen, list.index('C')])  # 자기 자신이거나, C의 번호 둘 중 하나를 랜덤으로 선택
        if choosen != choosen_2:                        # 선택을 바꿨을 때 (앞의 선택과 뒤의 선택이 다를 때)
            if list[choosen_2] == 'C':
                choose_goat_change_s += 1
            else:
                choose_goat_change_d += 1
        else:                                           # 선택을 바꾸지 않았을 때 (앞의 선택과 뒤의 선택이 같을 때)
            if list[choosen_2] == 'C':
                choose_goat_unchange_s += 1
            else:
                choose_goat_unchange_d += 1

print(f"차 선택 횟수: {choose_car}")
print(f"첫 번째 선택에서 차를 고른 경우: {conversion(choose_car, times)}%")
print(f"첫 번째 선택에서 염소를 고르고, 선택을 바꿔 승리한 경우: {conversion(choose_goat_change_s, times)}%")
print(f"첫 번째 선택에서 염소를 고르고, 선택을 바꿔 패배한 경우: {conversion(choose_goat_change_d, times)}%")
print(f"첫 번째 선택에서 염소를 고르고, 선택을 바꾸지 않아 승리한 경우: {conversion(choose_goat_unchange_s, times)}%")
print(f"첫 번째 선택에서 염소를 고르고, 선택을 바꾸지 않아 패배한 경우: {conversion(choose_goat_unchange_d, times)}%\n")

print(f"첫 번째 선택에서 염소를 골랐을 때, 선택을 바꾼다면 승리할 확률: {choose_goat_change_s/(choose_goat_change_d + choose_goat_change_s) * 100}%")