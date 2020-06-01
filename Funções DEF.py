def funcao(a, b):#função simples, com 2 parametros
    print('{} + {} = {}'.format(a, b, a + b))


def funcao2(*parametro):# função que tem como paramentro indefinido, podendo ser setado quando chamada a função (tuple)
    print(type(parametro))
    print(parametro)


def funcao3(**parametro):# função que tem como paramentro indefinido, mas podendo atribuir um valor ao parametro quando chamado
    print(type(parametro))
    print(parametro['c'])


def fatorial(a):# função recursiva (que chama ela mesmo)...
    if a == 1:  # Exemplo com Fatorial (numero N que é multiplicado pelos antecesores dele mesmo até 1 ex.. 4*3, *4*2, 4*1
        return 1
    else:
        return a * fatorial(a - 1)


funcao(10, 5)

funcao2(5, 10, 'carro', 5.5)

funcao3(a=5, b=5.5, c='Oi...')

print(fatorial(5))
