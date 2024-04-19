# Jogo da Forca

# Importação da biblioteca
import random
from os import system, name

# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows
    if name == 'nt':
        _ = system('cls')

    # Mac ou Linux
    else:
        _ = system('clear')

# Função que desenha a forca na tela
def display_hangman(chances):

    # Lista de estágios da forca
    stages = [  # estágio 6 (final)
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # estágio 5
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        # estágio 4
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,
        # estágio 3
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        # estágio 2
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        # estágio 1
        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,
        # estágio 0
        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return stages[chances]


# Função
def game():

    limpa_tela()
    print('\nBem-vindo(a) ao jogo da forca!')
    print('Advinhe a palavra abaixo')
   
    # Lista de palavras para o jogo
    lista_de_palavras = ['banana', 'cereja', 'tangerina', 'pera', 'uva', 'framboesa', 'caju']

    # Seleção randomica da palavra
    palavra = random.choice(lista_de_palavras)

    # Criação dos underscores
    tabuleiro = ['_'] * len(palavra)

    # Definição do número de chances
    chances = 6

    # Lista para as letras digitadas
    letras_erradas = []

    # Loop para o número de chances
    while chances > 0:
        
        print(display_hangman(chances))
        print(' '.join(tabuleiro))
        print('\nChances restantes:', chances)
        print('Letras erradas:', ' '.join(letras_erradas))

        # Tentativa
        while True:
            tentativa = input('\nDigite uma letra: ').lower()

            if len(tentativa) == 1 and tentativa.isalpha():

                if tentativa in letras_erradas:
                    print('Esta letra já selecionada. Por favor, escolha outra!')
                
                elif tentativa in tabuleiro:
                    print('Esta letra pertence à palavra, mas já foi selecionada antes. Por favor, escolha outra!')

                else:
                    break
            else:
                print('Você digitou mais de 1 letra ou digitou um caractere inválido. Digite apenas 1 letra!')
                continue

        # Condicional
        if tentativa in palavra:
            index = 0
            for letra in palavra:
                if tentativa == letra:
                    tabuleiro[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        # Condicional da Vitória
        if '_' not in tabuleiro:
            print('\nVocê venceu, a palavra era:', palavra)
            break

    # Condicional da Derrota
    if '_' in tabuleiro:
        print(display_hangman(chances))
        print('\nVocê perdeu, a palavra era:', palavra)

# Bloco main
if __name__ == "__main__":
    game()
    print('\nProjeto de Conclusão do curso introdutório a Python da DSA')
