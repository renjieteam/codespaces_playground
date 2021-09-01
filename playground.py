def fib(n):
    if n <= 0:
        return -1
    elif n in (1, 2):
        return 1
    else:
        a = 1
        b = 1 
        for i in range(3, n+1):
            c = a+b
            a = b
            b = c
        return c

for i in range(10):
    print(i, 'fib:', fib(i))






