from math import ceil

def ceil_square(a,b):
    return ceil(a*b)
a=float(input('1 сторона:'))
b=float(input('2 сторона:'))
print(f'Квадрат- {ceil_square(a,b)}')