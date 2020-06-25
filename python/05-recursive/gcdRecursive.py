# 遞迴求最大公因數 gcd(a,b)

def gcd(a, b):
    return a if b==0 else gcd(b, a%b)   # 三元運算子等於 return b==0 ? a : gcd(b,a%b)


def main():
    print('gcd(a,b)')
    a = int(input('a = '))
    b = int(input('b = '))
    G = gcd(a,b)
    print('result = ',G)

main()