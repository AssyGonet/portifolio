'''
Criar um menu
Criar uma lista de operações
Criar um input do usuário
Criar funções de cálculo
Formatar retorno
Retornar de forma amigável ao usuário
Tratar excessões
'''

import soma
import subtrair
import multiplicar
import dividir
import validarSaidaDoUsuario

while True:
    try:
        print('Seja bem vindo à primeira calculadora de assi')
        print("opção 1: Soma")
        print("opção 2: Subtração")
        print("opção 3: Multiplicação")
        print("opção 4: Divisão")
        print("opção 0: Sair")

        opcao = int(input("Selecione uma opção de 1 a 4:"))

        match (opcao):
            case 0:
                print("Fim do programa")
                break
            case 1:
                while True:
                    valor1 = float(input("insira o primeiro valor: "))
                    valor2 = float(input("insira o segundo valor: "))
                    soma.somar_valores(valor1, valor2)
                    validate = validarSaidaDoUsuario.validar_saida_do_usuario()
                    if validate == False:
                        break
            case 2:
                while True:
                    valor1 = float(input("insira o primeiro valor: "))
                    valor2 = float(input("insira o segundo valor: "))
                    subtrair.subtrair_valores(valor1, valor2)
                    validate = validarSaidaDoUsuario.validar_saida_do_usuario()
                    if validate == False:
                        break

            case 3:
                while True:
                    valor1 = float(input("insira o primeiro valor: "))
                    valor2 = float(input("insira o segundo valor: "))
                    multiplicar.multiplicar_valores(valor1, valor2)
                    validate = validarSaidaDoUsuario.validar_saida_do_usuario()
                    if validate == False:
                        break
            case 4:
                while True:
                    valor1 = float(input("insira o primeiro valor: "))
                    valor2 = float(input("insira o segundo valor: "))
                    dividir.dividir_valores(valor1, valor2)
                    validate = validarSaidaDoUsuario.validar_saida_do_usuario()
                    if validate == False:
                        break
            case _:
                print('Ocorreu um erro inesperado!')
    except Exception:
        print("Ocorreu um erro inesperado!")
