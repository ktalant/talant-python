w1 = int(input('Enter the width of 1st rectangle: '))
h1 = int(input('Enter the heigth of 1st rectangle: '))

w2 = int(input('Enter the width of 2nd rectangle: '))
h2 = int(input('Enter the heigth of 2nd rectangle: '))

a1 = w1 * h1
a2 = w2 * h2 

if a1 > a2:
    print('1st rectangle\'s area is biggest')
elif a1 == a2:
    print('1st and 2nd rectangles has same area')
else:
    print('2nd rectangle\'s are is biggest')


    