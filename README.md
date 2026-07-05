# 🎮 Jogo da Forca

O jogo tradicional da forca em Python 3, criado para praticar conceitos de **programação estrutural e modular**.
O fluxo principal é controlado por funções dedicadas. O sistema também realiza a leitura dinâmica de palavras a partir de um arquivo de texto externo.

## Conceitos e Recursos Aplicados

Este projeto consolida os seguintes conceitos da linguagem:

### 1. Modularização e Funções (`def`)
* O código é totalmente dividido em funções com responsabilidades únicas, uma prática que facilita a manutenção e legibilidade.

### 2. Manipulação de Arquivos (I/O)
* Uso do método integrado `open()` para ler um arquivo onde estão as possíveis palavras para entrar no jogo. Isso é feito de forma randômica com o uso do método `random.randrange()`.
* Tratamento de strings com `.strip()` para remover quebras de linha (`\n`) e espaçamentos indesejados durante a leitura.

### 3. Estruturas de Dados e Compreensão de Listas
* **Listas (Arrays):** Utilizadas para armazenar o dicionário de palavras e rastrear as letras acertadas.
* **List Comprehension:** Utilizada em `["_" for letra in palavra]` para inicializar a máscara da palavra secreta de forma performática e elegante.

### 4. Controle de Fluxo e Loops
* **Loop `while`:** Controla a partida dinamicamente até que uma das condições de parada de jogo seja atingida.
* **Loop `for`:** Utilizado para iterar sobre as linhas do arquivo e para varrer a palavra secreta verificando a posição do chute do jogador.

### 6. Ponto de Entrada Padrão Python
* Implementação do bloco `if __name__ == "__main__":`, garantindo que o jogo possa ser executado diretamente pelo terminal como um script principal.

## Como Executar o Projeto

### Pré-requisitos
* Ter o **Python 3** instalado na sua máquina.

### Passo a Passo

1. Clone o repositório:
   ```bash
   git clone https://github.com/isapinheir/forca
   ```
2. Execute através do terminal:
    ```bash
    python3 forca.py
    ```
