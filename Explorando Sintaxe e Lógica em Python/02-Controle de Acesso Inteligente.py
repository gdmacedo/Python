"""
Projeto...: Explorando Sintaxe e Lógica em Python
Módulo....: Controle de Acesso Inteligente
Data......: 14 de agosto de 2025
Autor.....: Macedo, Glener Diniz
Descrição.: Uma biblioteca está implementando um sistema automatizado para liberar o acesso à área de livros raros. 
            O sistema deve permitir a entrada apenas para visitantes autorizados e com idade mínima de 18 anos. 
            Para isso, é necessário utilizar operadores lógicos, estruturas condicionais (if, else, else if) e 
            conceitos básicos como tipos primitivos e palavras-chave. Desenvolva um programa que verifique se o 
            visitante pode acessar a sala especial.

Entrada...: O programa deve receber os seguintes valores:
            - Um valor booleano indicando se o visitante possui autorização (true ou false)
            - Um número inteiro representando a idade do visitante

Saída.....: Deverá retornar uma String com as mensagens:
            - "Acesso permitido" se o usuário tiver permissão e for maior ou igual a 18 anos.
            - "Acesso negado" se o usuário não tiver permissão.
            - "Idade insuficiente" se o usuário tiver permissão, mas for menor de idade.
"""
def main():
    # Entrada de dados do usuário
    has_permission = input().lower() == "true"  
    age = int(input()) 

    # Verifica as condições de acesso
    if age >= 18 and has_permission:
        print("Acesso permitido")
    elif not has_permission:
        print("Acesso negado")
    else:
        print("Idade insuficiente")
        
if __name__ == "__main__":
    main()
    