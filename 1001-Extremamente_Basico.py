# https://www.beecrowd.com.br/judge/pt/problems/view/1001

# Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável X. Imprima X conforme exemplo apresentado abaixo. Não apresente mensagem alguma além daquilo que está sendo especificado e não esqueça de imprimir o fim de linha após o resultado, caso contrário, você receberá "Presentation Error".

# Entrada
# A entrada contém 2 valores inteiros.

# Saída
# Imprima a mensagem "X = " (letra X maiúscula) seguido pelo valor da variável  X  e pelo final de linha. Cuide para que tenha um espaço antes e depois do sinal de igualdade, conforme o exemplo abaixo.

def main() -> None:
    A = int(input(""))
    B = int(input(""))
    X = A + B
    print(f"X = {X}")

if __name__ == "__main__":
    main()
