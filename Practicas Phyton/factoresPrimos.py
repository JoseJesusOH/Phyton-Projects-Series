
print('Este programa determina los factores primos de un numero entero')
print()

n = int(input('Dame un numero entero: '))
print()

print(f'Los factores primos de {n:d} son:')

divisor = 2
while n > 1:
    rdivisor = int(divisor ** 0.5)

    d = 2
    while d <= rdivisor:
        if not divisor % d:
            break
        d += 1

    if d <= rdivisor: 
        divisor += 1
        continue

    while not n % divisor:
        n //= divisor
        print(f'{divisor:d}, ', end='')
      
    divisor += 1

