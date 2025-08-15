"""
Projeto...: Explorando Sintaxe e Lógica em Python
Módulo....: Monitoramento de Bicicletas
Data......: 14 de agosto de 2025
Autor.....: Macedo, Glener Diniz
Descrição.: Um sistema de monitoramento de bicicletas compartilhadas precisa calcular a distância máxima que cada bicicleta
            pode percorrer, com base no nível atual de bateria. Cada 1% de bateria permite percorrer 0,5 km. Neste desafio, 
            você deve utilizar os conceitos de Programação Orientada a Objetos (POO) para modelar a bicicleta. 
            Crie uma classe que contenha os atributos necessários e um método para calcular a distância estimada.

Entrada...: A entrada deve conter:
            - O nome do modelo da bicicleta (String).
            - O nível de bateria (int).

Saída.....: Deverá retornar uma mensagem com o modelo da bicicleta e a distância máxima estimada, formatada com uma casa decimal.
            - Retorno em formato de mensagem.
"""
class BicicletaInterna:
    def __init__(self, modelo, nivel_bateria):
        self.modelo = modelo
        self.nivel_bateria = nivel_bateria

    def calcular_distancia(self):
        # Cada 1% de bateria permite percorrer 0.5 km
        return self.nivel_bateria * 0.5

    def obter_mensagem(self):
        # Retorna a mensagem formatada com uma casa decimal
        distancia = self.calcular_distancia()
        return f"{self.modelo}: Distancia estimada = {distancia:.1f} km"


def main():
    modelo = input()
    nivel_str = input()
    nivel_bateria = int(nivel_str)

    # Cria o objeto BicicletaInterna com os dados lidos
    bicicleta = BicicletaInterna(modelo, nivel_bateria)

    print(bicicleta.obter_mensagem())


if __name__ == "__main__":
    main()