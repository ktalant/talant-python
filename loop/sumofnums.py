# 1/30 + 2/29 + 3/28 + ... + 30/1
sum = 0

for i in range(1,31):
    print(i, '/',30-i+1,'+', sep='', end='')
    sum += i / (30-i+1)
print()
print('sum is', format(sum, ',.2f'))
