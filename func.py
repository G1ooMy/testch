import random

def diceroll(cnt, max):
    total = 0
    num_list = []
    for i in range(0, cnt):
        # �����_����1����T�C�R���̖ʐ��܂ł̘a���擾�����X�g�ɓ����
        num = random.randint(1, max)
        num_list.append(num)
    # ��������̖ڂ̑��a���v�Z�����X�g�ɓ����
    total = sum(num_list)
    num_list.append(total)
    return num_list