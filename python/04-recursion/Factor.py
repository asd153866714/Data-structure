# 用遞迴方式計算 N 階乘

def Factorial(n):
    if n == 1:
        return 1
    else:
        return n * Factorial(n-1)

def main():
    ch = ''
    n = 0

    print('-----Factorial counting Using Recursive-----')
    while True:
        # 防例外
        try:
            n = int(input('\nEnter a number to count n!: '))
        except ValueError:
            print('Not a correct number.')
            print('Try again\n')
           
        print("%d! = %d" % (n, Factorial(n)))

        ch = input('Continue (y/n) ?\n')
        if ch != 'y':
            break

main()