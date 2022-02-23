def code(x):
    if x < 5 :
        return 3 * x
    else:
        return 2 * code(x - 5) + 7

print(code(4))

