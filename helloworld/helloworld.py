resposta = int(input('Digite um numero: '))
resultado = 5*resposta

if resultado < 10:
    print('Resultado é menor que 10')
elif resultado == 10:
    print('Resultado é 10')
elif resultado > 10:
    print('Resultado é maior que 10')

for i in range(resultado):
    print('iteracao',i)

def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)
