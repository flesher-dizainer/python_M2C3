# zadanie 1
try:
    print('zadanie 1')
    a = int(input('Enter range value 1..100: '))
    if ( a > 0 ) and ( a < 101 ):
        if (a % 3 == 0) and (a % 5 == 0):
            print('Fizz Buzz')
        elif a % 3 == 0:
            print('Fizz')
        elif a % 5 == 0:
            print('Buzz')
        else:
            print(a)
    else:
        print('Input value out of range')
        
except ValueError:
    print('Input value error')
    
# zadanie 2
try:
    print('zadanie 2')
    a = int(input('Enter the number to raise to the power: '))
    b = int(input('Enter to what power to raise the number 0..7: '))
    if (b >= 0) and (b < 8):
        print(a**b)
    else:
        print('Error degree of')
except ValueError:
    print('Input value error')

# zadanie 3
try:
    print('zadanie 3')
    a = float(input('Enter call cost: '))
    b = int(input('select operators 1..4:\n1. megafor - megafon\n2. megafon - mts\n3. mts - megafon\n4. mts-mts\n '))
    if ( b < 1 ) or ( b > 4 ):
        print('Error select operators')
    else:
        if b == 1:
            print('price calls = '+str(a * 1.1))
        elif b == 2:
            print('price calls = '+str(a * 2))
        elif b == 3:
            print('price calls = '+str(a * 1.8))
        elif b == 4:
            print('price calls = '+str(a * 1.2))
except ValueError:
    print('Input value error')

# zadanie 4
try:
    print('zadanie 4')
    a = float(input('Enter sales manager 1: '))
    b = float(input('Enter sales manager 2: '))
    c = float(input('Enter sales manager 3: '))
    if a < 500:
       m1 = 3
    elif a < 1000:
        m1 = 5
    elif a >= 1000:
        m1 = 8
    else:
        m1 = 0
        
    if b < 500:
       m2 = 3
    elif b < 1000:
        m2 = 5
    elif b >= 1000:
        m2 = 8
    else:
        m2 = 0
        
    if c < 500:
       m3 = 3
    elif c < 1000:
        m3 = 5
    elif c >= 1000:
        m3 = 8
    else:
        m3 = 0

    a += a*m1/100
    b += b*m2/100
    c += c*m3/100
    if (a > b) and (a > c):
        print('manager 1 TOP MANAGER')
    elif (b > a) and (b > c):
        print('manager 2 TOP MANAGER')
    elif (c > a) and (c > b):
        print('manager 3 TOP MANAGER')
    print('Manager 1 salary = '+str(a)+'$\n'+'Manager 2 salary = '+str(b)+'$\n'+'Manager 3 salary = '+str(c)+'$\n')
except ValueError:
    print('Input value error')
