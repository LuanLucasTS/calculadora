from calculadora import Calculadora

def main():
    calc = Calculadora()

    while True:
        print("\n--- Calculadora ---")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("5: Sair")

        opcao = input("Escolha uma operação: ")

        if opcao == "5":
            print("Encerrando o programa...")
            break

        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = calc.executar(opcao, num1, num2)
            print(f"Resultado: {resultado}")
        except ValueError:
            print("Erro: Por favor, insira números válidos.")

if __name__ == "__main__":
    main()
