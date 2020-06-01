import random


class chute_o_numero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_maximo = 100
        self.valor_minimo = 0
        self.valor_chute = 0

    def iniciar(self):
        self.valor_aleatorio = self.gerar_valor_aleatorio()
        self.obter_valor_do_usuario()
        while self.valor_aleatorio != self.valor_chute:
            if self.valor_aleatorio > self.valor_chute:
                print('chute um valor maior !\n')
                self.obter_valor_do_usuario()
            elif self.valor_aleatorio < self.valor_chute:
                print('chute um valor menor !\n')
                self.obter_valor_do_usuario()
        print('vc acertou mizeravel')

    def obter_valor_do_usuario(self):
        try:
            self.valor_chute = int(
                input(f'chute um valor entre {self.valor_minimo} a {self.valor_maximo}: '))
        except ValueError:
            print('Digite apenas números !')
            self.obter_valor_do_usuario()

    def gerar_valor_aleatorio(self):
        return random.randint(self.valor_minimo, self.valor_maximo)


auto = chute_o_numero()
auto.iniciar()
