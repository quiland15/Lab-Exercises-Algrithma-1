x = input('Masukkan Data =')
def hitung(x):
    if len(x) == 0 :
        return 0
    elif x[0] == 'a':
        return 1 + hitung(x[1:])
    else:
        return hitung(x[1:])

print('Jumlah Huruf A dalam kata', x ,'=', hitung(x))