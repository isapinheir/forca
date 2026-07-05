import random

def jogar():
    abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
        
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(f"{letras_acertadas}\n")

    if(acertou):
        mensagem_vitoria()
    else:
        mensagem_derrota(palavra_secreta)

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    return palavras[numero].upper()

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    return input("Qual letra? ").strip().upper()

def marca_correto(chute, letras_acertadas, palavra_secreta):
    i = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[i] = letra
        i += 1

def abertura():
    print(r"")
    print(r"            Bem vindo(a) ao jogo de            ")
    print(r" /$$$$$$$$                                     ")
    print(r"| $$_____/                                     ")
    print(r"| $$     /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ ")
    print(r"| $$$$$ /$$__  $$ /$$__  $$ /$$_____/ |____  $$")
    print(r"| $$__/| $$  \ $$| $$  \__/| $$        /$$$$$$$")
    print(r"| $$   | $$  | $$| $$      | $$       /$$__  $$")
    print(r"| $$   |  $$$$$$/| $$      |  $$$$$$$|  $$$$$$$")
    print(r"|__/    \______/ |__/       \_______/ \_______/")
    print(r"")

def mensagem_vitoria():
    print(r"")
    print(r"/$$$$$$$                              /$$                                    ")
    print(r"| $$__  $$                            | $$                                    ")
    print(r"| $$  \ $$ /$$$$$$   /$$$$$$  /$$$$$$ | $$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$$")
    print(r"| $$$$$$$/|____  $$ /$$__  $$|____  $$| $$__  $$ /$$__  $$| $$__  $$ /$$_____/")
    print(r"| $$____/  /$$$$$$$| $$  \__/ /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \ $$|  $$$$$$ ")
    print(r"| $$      /$$__  $$| $$      /$$__  $$| $$  | $$| $$_____/| $$  | $$ \____  $$")
    print(r"| $$     |  $$$$$$$| $$     |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$  | $$ /$$$$$$$/")
    print(r"|__/      \_______/|__/      \_______/|_______/  \_______/|__/  |__/|_______/")
    print(r"")
    print(r"Você ganhou o jogo!")

def mensagem_derrota(palavra):
    print(r"")
    print(r" /$$$$$$$                                            /$$              ")
    print(r"| $$__  $$                                          | $$              ")
    print(r"| $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$ ")
    print(r"| $$  | $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$|_  $$_/   |____  $$")
    print(r"| $$  | $$| $$$$$$$$| $$  \__/| $$  \__/| $$  \ $$  | $$      /$$$$$$$")
    print(r"| $$  | $$| $$_____/| $$      | $$      | $$  | $$  | $$ /$$ /$$__  $$")
    print(r"| $$$$$$$/|  $$$$$$$| $$      | $$      |  $$$$$$/  |  $$$$/|  $$$$$$$")
    print(r"|_______/  \_______/|__/      |__/       \______/    \___/   \_______/")
    print(r"")
    print(f"A palavra correta era {palavra}")

if(__name__ == "__main__"):
        jogar()
