import random

def main():
    total=0
    turn =0
    while total<20 and turn!=1:
        turn = random.randint(1,6)
        print('Roll: {}'.format(turn))
        if turn!=1:total+=turn
        else:total=0
    print('Turn total: {}'.format(total))
    
    
main()