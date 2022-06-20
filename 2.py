c = 5
d = 2 * c - 2
for e in range(0, c):
    for f in range(0, d):
        print(' ', end='')
    d -= 2
    for f in range(0, e + 1):
        print('* ', end='')
    print('')