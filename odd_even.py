    
def odd_even(m):
    import random as r
    for i in range(m):
        x = r.randrange(1,101)
        a = ''
        if x % 2 == 0:
            a = '1'
        else:
            a = '2'

        print('1. even number\n2. odd number')

        he = input()
        if he == a:
            print("your right")

        else:
            print("your wrong")

odd_even(3)



