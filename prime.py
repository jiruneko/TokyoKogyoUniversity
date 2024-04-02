N = 10
for n in range(2, N+1):
    for a in range(2, n//2+1):
        if n % a == 0:
            print(n, '=', a, '*', n//a)
            break
    else:
        print(n, 'は素数')