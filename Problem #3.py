x = input('Masukkan data =')
def str(x):
    if len(x) == 1:
        return x[0]
    else:
        return str(x[1:]) + x[0]
print(str(x))