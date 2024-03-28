from random import shuffle
from random import choice

print("=============================================================================================")
print("몬티홀 게임에 참여하신 것을 환영합니다!")
print("지금부터 사회자는 참여자분께 3개의 문을 선택지로 드릴 예정입니다.")
print("세 문 중, 하나의 문 뒤에는 차가, 나머지 두 개의 문 뒤에는 염소가 들어있으며")
print("제가 드린 기회를 이용하여 문 뒤의 차를 찾으면 승리하게 됩니다!")
print("확률이 3분의 1밖에 안되는 게임이라구요? 걱정하지 마세요!")
print("참가자분이 하나의 문을 선택하신 뒤, 저는 나머지 두 개의 문 중")
print("반드시 염소가 들어있는 문 하나를 제시해드릴 것입니다.")
print("그 때, 또 한번의 선택의 기회를 드리게된다면 참여자분은 문을 바꾸는 것이 유리할까요?")
print("=============================================================================================")

list_1 = ['G1', 'G2', 'C']
shuffle(list_1)
print(list_1)

choosen = int(input('1, 2, 3번 중 단 하나의 문을 선택해주세요! : ')) - 1

num_list = [list_1.index(x) for x in list_1 if x != 'C' or list_1.index(x) != choosen]
goat_1 = choice(num_list)
print(num_list)
print(goat_1)

print(f"\n참가자분께서 골라주신 {choosen+1}번 문의 결과를 확인하기 전에,")
print(f"먼저 {goat_1+1}번의 문에 염소가 한 마리 있다는 것을 알려드리겠습니다.")

choide_result = input(f"그렇다면 참가자분께서는, 처음 선택하신 {choosen+1}번 문을 그대로 다시 선택하시겠습니까? (y/n): ")
print("=============================================================================================")

if choide_result == 'y':
    pass
else:
    list_2 = [0, 1, 2]
    list_2.remove(choosen)
    list_2.remove(goat_1)
    choosen = list_2[0]

if list_1[choosen] == 'C':
    print('승리!')
else:
    print('패배!')