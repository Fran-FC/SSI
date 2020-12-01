def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def main():
    n = int(input('Introduce un número para calcular su factorial: '))
    if n <= 0:
        print('No se puede calcular el factorial de {}'.format(n))
        return
        
    fN = factorial(n)
    print('El factorial de {0} es {1}'.format(n, fN))
    if fN % 2 == 1:
        print('{} es impar'.format(fN))
    else:
        print('{} es par'.format(fN))

if __name__ == "__main__":
    main()