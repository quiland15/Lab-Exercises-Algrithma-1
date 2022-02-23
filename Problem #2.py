n = int(input('masukkan Nilai ='))
def rec(n):
    if n == 1:
        return 2
    else:
        return 2 * n + rec(n - 1)
    
print(rec(n))