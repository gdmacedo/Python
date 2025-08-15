"""
Projeto...: Explorando Sintaxe e Lógica em Python
Módulo....: Controle de Acesso Inteligente
Data......: 14 de agosto de 2025
Autor.....: Macedo, Glener Diniz
Descrição.: Um aplicativo de monitoramento de carros precisa verificar se um carro está apto para rodar
            com base no ano de fabricação e no ano atual. Um carro é considerado apto se tiver até 10 anos de uso. 
            Para resolver este desafio, você deve utilizar conceitos de Programação Orientada a Objetos (POO),
            como a definição de métodos estáticos, para realizar a verificação da aptidão do carro sem a necessidade
            de instanciar objetos. A aplicação de POO deve ser utilizada para organizar a lógica de verificação do 
            carro e para retornar o resultado da aptidão de forma estruturada.

Entrada...: A entrada deve conter:
            - O modelo do carro (String).
            - O ano de fabricação (int).
            - O ano atual (int).

Saída.....: Deverá retornar uma mensagem indicando se o carro está apto ou não.
            - Retorno em formato de mensagem.
"""
def verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual):
    idade_carro = ano_atual - ano_fabricacao

    # Verifica se o carro está apto com base na idade
    if idade_carro <= 10:
        return f"{modelo}: Apto"
    else:
        return f"{modelo}: Nao apto"


def main():
    modelo = input()
    ano_fabricacao = int(input())
    ano_atual = int(input())

    # Chama a função para verificar a aptidão do carro
    resultado = verificar_aptidao_carro(modelo, ano_fabricacao, ano_atual)

    print(resultado)


if __name__ == "__main__":
    main()