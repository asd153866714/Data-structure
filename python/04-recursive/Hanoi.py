# 利用遞迴方式求河內塔問題之解

def HanoiTower(n, _from, _aux, _to):
    if n == 1:
        print('Move disk %d from %c --> %c' % (n, _from, _to))
    else:

        # 將A上n-1個盤子借助C移至B
        HanoiTower(n-1, _from, _to, _aux)
        print('Move disk %d from %c --> %c' % (n, _from, _to))

        # 將B上n-1個盤子借助A移至C
        HanoiTower(n-1, _aux, _from, _to)


def main(): # 主函數
    ch = ''
    n = 0
    A = 'A'
    B = 'B'
    C = 'C'

    print('-----Hanoi Tower Implementation-----')
    #輸入共有幾個盤子在A柱子中
    while True:
        try:
            n = int(input('How many disks in A ? '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')

        if n == 0:
            print('No disk to move')
        else:
            HanoiTower(n, A, B, C)

        ch = input('\nContinue (y/n) ? ')

        if ch != 'y':
            break

main()