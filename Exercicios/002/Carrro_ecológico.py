class Carro:
    def __init__(self):
        self.pessoas = 0
        self.quilometragem = 0
        self.combustivel = 0

    def show(self):  # Exibe pessoas no carro, quilometragem e combustível
        print(f'pass: {self.pessoas}\ngas: {self.combustivel}\nkm: {self.quilometragem}\n')

    def enter(self):  # Insere uma pessoa no carro
        if self.pessoas < 2:
            self.pessoas += 1
        else:
            print('O carro está cheio')

    def leave(self):  # Retira uma pessoa do carro
        if self.pessoas:
            self.pessoas -= 1
        else:
            print('Não tem ninguém no carro')

    def fuel(self, quantidade):  # Abastece o carro com a quantidade fornecida pelo usuário
        if self.combustivel + quantidade <= 100:
            self.combustivel += quantidade
        else:
            self.combustivel = 100

    def drive(self, distancia):  # Faz o carro percorrer a distancia fornecida pelo usuário
        if not self.pessoas:
            print('Não há pessoas no carro')
        elif not self.combustivel:
            print('Carro sem combustível')
        else:
            if distancia > self.combustivel:
                print(f'Tanque vazio após andar {self.combustivel}km')
                self.quilometragem += self.combustivel
                self.combustivel = 0
            else:
                self.quilometragem += distancia
                self.combustivel -= distancia


car = Carro()  # Criação de um objeto -> car

manual = """OPÇÕES:\n
enter: insere uma pessoa no carro
leave: retira uma pessoa do carro
fuel + quantidade: abastece o carro com a quantidade fornecida
drive + distancia: faz o carro percorrer a distancia fornecida
show: exibe a quantidade de pessageiros, a quilometragem e o combustível no carro
exit: encerra o programa\n"""
print(manual)

while True:  # Interação com o usuário
    entrada = input('Digite um comando: ')

    if entrada.lower() == 'enter':
        car.enter()
    elif entrada.lower() == 'leave':
        car.leave()
    elif entrada.lower() == 'show':
        car.show()
    elif entrada.lower() == 'exit':
        break
    elif 'drive' in entrada.lower():
        car.drive(int(entrada[5:]))
    elif 'fuel' in entrada.lower():
        car.fuel(int(entrada[4:]))
    else:
        print('Comando inválido')
