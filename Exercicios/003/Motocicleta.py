class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Motocicleta:
    def __init__(self):
        self.potencia = 1
        self.tempo = 0
        self.pessoa = None

    def enter(self, valor):  # Insere uma pessoa na motocicleta, recebendo como parâmetro um objeto da classe Pessoa
        self.pessoa = valor

    def show(self):  # Exibe o tempo, potencia e a pessoa na motocicleta
        if self.pessoa:
            print(f'power: {self.potencia}\ntime: {self.tempo}\nperson: {self.pessoa.nome}, {self.pessoa.idade} anos')
        else:
            print(f'power: {self.potencia}\ntime: {self.tempo}\nperson: ')

    def leave(self):  # Retira uma pessoa da motocicleta
        if self.pessoa:
            self.pessoa = None
        else:
            print('Não há ninguém para descer')

    def buy(self, quantidade):  # Compra tempo para a motocicleta igual à quantidade recebida como parâmetro
        self.tempo += quantidade
        print(f'Você comprou {quantidade} minutos')

    def drive(self, quantidade):  # Faz a motocicleta andar, se houver uma pessoa dentro da idade permitida e com
        # tempo disponível
        if self.pessoa.idade > 10:
            print('Você é velho demais para dirigir a motocicleta\n idade máxima: 10 anos')
        elif self.tempo == 0:
            print('Você não tem tempo disponível para dirigir')
        else:
            if self.tempo >= quantidade:
                self.tempo -= quantidade
                print(f'Você andou durante {quantidade} minutos com sucesso')
            else:
                print(f'Você andou por {self.tempo} minutos e seu tempo acabou')

    def honk(self):  # Faz a motocicleta buzinar
        buzinar = 'p' + 'e' * self.potencia + 'm'
        print(buzinar)

    def aumenta_potencia(self, valor):  # Aumenta a potencia da motocicleta igual ao valor recebido como parâmetro
        self.potencia = valor


moto = Motocicleta()

opcoes = """OPÇÕES:
enter + nome + idade: insere uma pessoa na motocicleta
leave: retira a pessoa da motocicleta
buy + valor: compra quantidade de tempo
drive + valor: dirige pela quantidade de tempo fornecida
honk: buzina
potencia + valor: define a potencia da motocicleta
show: exibe os valores de tempo disponível, potencia e a pessoa na moto
exit: encerra o programa
menu: exibe o menu novamente
"""
print(opcoes, end='')

# Interação com o usuário
while True:
    entrada = input('\nDigite um comando: ')
    entrada = entrada.lower()

    if 'enter' in entrada.lower():
        entrada = entrada.replace(' ', '', 1)
        entrada = entrada.replace('enter', '').split(' ')
        moto.enter(Pessoa(entrada[0], int(entrada[1])))
        print(f'{moto.pessoa.nome} subiu na moto')

    elif entrada == 'show':
        moto.show()

    elif entrada == 'honk':
        moto.honk()

    elif entrada == 'exit':
        break

    elif entrada == 'leave':
        moto.leave()
        try:
            print(f'{moto.pessoa.nome} desceu da moto')
        except AttributeError:
            pass

    elif 'buy' in entrada:
        entrada = entrada.replace(' ', '')
        entrada = entrada.replace('buy', '')
        moto.buy(int(entrada))

    elif 'potencia' in entrada:
        entrada = entrada.replace(' ', '')
        entrada = entrada.replace('potencia', '')
        moto.aumenta_potencia(int(entrada))

    elif 'drive' in entrada:
        entrada = entrada.replace(' ', '')
        entrada = entrada.replace('drive', '')
        try:
            moto.drive(int(entrada))
        except AttributeError:
            print('Error! Talvez você não tenha inserido ninguém na moto antes de tentar dirigir')

    elif entrada == 'menu':
        print(opcoes, end='')

    else:
        print('Comando inválido, tente novamente')
