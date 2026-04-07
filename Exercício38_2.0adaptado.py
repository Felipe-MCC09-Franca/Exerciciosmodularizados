import os

#Declaracao de variaveis
x: int = 0
dir_raiz: str = "/tmp/exercicios/"
arq_entrada: str = "exercício38"
arq_saida: str = "multiplos_de_5"
maior: int = 0
menor: int = 0

def maiormenor(cont):
    global x, maior, menor
    if cont == 1:
        maior = x
        menor = x
    else:
        if x > maior:
            maior = x
        if x < menor:
            menor = x

def grava(c, valor_ou_texto, final=False):
    global dir_raiz, arq_entrada
    arquivo = os.path.join(dir_raiz, arq_entrada)
    if os.path.exists(dir_raiz) and os.path.isdir(dir_raiz):
        tipo = "w" if c == 1 else "a"
        with open(arquivo, mode=tipo, encoding="utf-8") as file:
            if final:
                file.write("\n" + valor_ou_texto + "\n")
            else:
                file.write(f"Valor {c}: {valor_ou_texto}\n")

def multiplo_de_5(valor: int) -> bool:
    return valor % 5 == 0

def grava_multiplo(valor_str):
    caminho_saida = os.path.join(dir_raiz, arq_saida)
    with open(caminho_saida, mode="a", encoding="utf-8") as f:
        f.write(valor_str + "\n")

def processar_multiplos():
    caminho_entrada = os.path.join(dir_raiz, arq_entrada)
    caminho_saida = os.path.join(dir_raiz, arq_saida)
    
    if os.path.exists(caminho_saida):
        open(caminho_saida, 'w').close()

    if os.path.exists(caminho_entrada):
        with open(caminho_entrada, mode="r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                linha = linha.strip()
                if not linha or "Maior" in linha or "Menor" in linha:
                    continue
                try:
                    partes = linha.split(": ")
                    if len(partes) > 1:
                        num = int(float(partes[1]))
                        if multiplo_de_5(num):
                            grava_multiplo(str(num))
                except:
                    continue

def main():
    global x
    if not os.path.exists(dir_raiz):
        os.makedirs(dir_raiz, exist_ok=True)
    
    for i in range(1, 101):
        try:
            x = int(input(f"Digite o {i}º número: "))
            while x < 0:
                x = int(input("Apenas positivos: "))
            maiormenor(i)
            grava(i, x)
        except ValueError:
            continue

    resumo = f"O maior valor é: {maior}\nO menor valor é: {menor}"
    grava(i, resumo, final=True)
    
    processar_multiplos()

if __name__ == '__main__':
    main()
    
#Fim