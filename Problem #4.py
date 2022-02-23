x = int(input('Masukkan Angka X ='))
y = int(input('Masukkan Angka Y ='))
def fun3(x, y):
    if x > y:
        return -1
    elif x == y:
        return 1
    else:
        return x * fun3(x + 1, y)

print('Hasil Recursion Dari X =', x ,'dan Y =', y ,'Adalah', fun3(x, y))