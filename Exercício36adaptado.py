import os

# Declaração de variáveis
x: float = 0.0
y: int = 0
dir: str = "/tmp/exercicios/"
arq: str = "exercicio36"
arquivo: str = ""

# Início
def fatorial(cont):
    fat: int = 1
    for i in range(1, cont + 1):
        fat = fat * i
    return fat

def divisao(f):
    return 1 / f

def grava(conteudo, c):
    global dir, arq, arquivo
    enc: str = "utf-8"
    arquivo = dir + arq
   
    if(os.path.exists(dir) and os.path.isdir(dir)):
        tipo = "w"
        enc = "utf-8"
        if(os.path.exists(arquivo)):
            tipo = "a"
        with open(arquivo, tipo, encoding=enc) as file:
            file.write(str(conteudo) + "\n")

def main():
    global x, y

    if not os.path.exists(dir):
        os.makedirs(dir, exist_ok=True)
    
    y = int(input("Digite um número inteiro: "))

    grava("Termo 0: 1", 0)

    for i in range(1, y + 1):
        fat_resultado = fatorial(i)
        termo = divisao(fat_resultado)
        x = x + termo
        grava(f"Termo {i}: {termo}", i)

    grava(f"Resultado Final: {x}", y + 1)

if __name__ == "__main__":
    main()

#Fim