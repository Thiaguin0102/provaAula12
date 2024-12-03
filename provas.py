class Veiculo:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def movimentar(self):
        print("O veículo está em movimento.")

class Carro(Veiculo):
    def movimentar(self):
        print("O carro esta dirigindo.")

class Moto(Veiculo):
    def movimentar(self):
        print("A moto está acelerando.")


carro1 = Carro("Toyota", "Corolla", 2022, "Prata")
moto1 = Moto("Honda", "CBR", 2023, "Vermelha")
carro1.movimentar()
moto1.movimentar()