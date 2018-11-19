def numbers(n):
    total = (3 + 5**(1/2))**n
    stringtotal = str(total).split('.')
    if len(stringtotal[0]) < 3:
        return '0' + stringtotal[0]
    else:
        return stringtotal[0][-3:]

if __name__ == '__main__':
    n = int(input())
    for n_itr in range(n):
        print(numbers(int(input())))
        
# 5 = 935
# 2 = 027
