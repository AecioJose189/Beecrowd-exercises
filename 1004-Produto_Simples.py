# https://www.beecrowd.com.br/judge/pt/problems/view/1004

# Leia dois valores inteiros. A seguir, calcule o produto entre estes dois valores e atribua esta operação à variável PROD. A seguir mostre a variável PROD com mensagem correspondente.

# Entrada
# O arquivo de entrada contém 2 valores inteiros.

# Saída
# Imprima a mensagem "PROD" e a variável PROD conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade. Não esqueça de imprimir o fim de linha após o produto, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

def main() -> None:
    num_1 = int(input("Digite o primeiro valor inteiro: "))
    num_2 = int(input("Digite o segundo valor inteiro: "))
    produto = num_1*num_2
    print(f"O produto entre os dois números é: {produto}")
if __name__ == "__main__":
    main()
