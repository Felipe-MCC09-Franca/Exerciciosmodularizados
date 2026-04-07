import os

# Declaração de variáveis
x: int = 0
dir: str = "/tmp/exercicios/"
arq: str = "exercício38"
arquivo: str = ""
maior: int = 0
menor : int = 0

# Inicio

def maiormenor(cont):
    global maior
    global menor

    if cont == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x


def grava(c, valor_ou_texto, final = False):
    global dir
    global arq
    global arquivo
    tipo: str = ""
    enc: str = ""

    arquivo = dir + arq

    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = "w"
        enc = "utf-8"
        if(os.path.exists(arquivo)):
            tipo = "a"
        with open(arquivo, tipo, encoding = enc) as file:
            if final:
                file.write("\n" + valor_ou_texto + "\n")
            else:
                file.write(f"Valor {c}: {valor_ou_texto}\n")


def main():
    global x
    global maior
    global menor

    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok = True)
    os.chmod(dir, 0o744)

    for i in range(1, 100 + 1,1):
        x = int(input("Digite um número inteiro positivo: "))
        maiormenor(i)
        grava(i, x)
    resumo = f"O maior valor é: {maior}\nO menor valor é: {menor}"
    grava(i, resumo, final = True)


if __name__ == '__main__':
    main()

# Fim