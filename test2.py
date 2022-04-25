def lesenka():
    n = int(input())
    num = 1
    for row in range(1, n+1):
        for i in range(1, row+1):
            print(num, end=' ')
            num += 1
        print()

def perebor():
    total = 0
    for n in range(0, 100):
        for k in range(0, 100):
            for m in range(0, 100):
                if 10 * n + 5 * k + 0.5 * m == 100:
                    if n + k + m == 100:
                        total += 1
                        print(f'n = {n}, k = {k}, m = {m}')
    print(f'Общее количество натуральных решений = {total}')

def treugolnik():
    n = int(input())
    for i in range(1, n+1):
        for j in range(1, i + 1):
            print(j, end='', sep='')
        for k in range(i, 1, -1):
            print(k-1, end='', sep='')
        print()
    
def deliteli():
    a, b = int(input()), int(input())

    counter = 0
    largest = 0
    for i in range(a, b + 1):
        total = 0
        for j in range(1, i + 1):
            if i % j == 0:
                total += j
                if total >= counter and i >= largest:
                    counter = total
                    largest = i
    print(largest, counter)

#deliteli()
#perebor()
#lesenka()
#treugolnik()