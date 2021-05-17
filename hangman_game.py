import os
import random

#Ayuda a pasaar de vocales con tilde a vocales sin tilde
def normalize(s):
        replacements = (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
        for a, b in replacements:
            s = s.replace(a, b).replace(a.upper(), b.upper())
        return s

#Pasando las palabras del archivo data.txt a una lista y de ahi se escoge una palabra al azar la cual se normaliza 
def get_data():
    with open('./archivos/data.txt', 'r', encoding="utf-8") as f:
        words = [line for line in f]
        guess_word = normalize(random.choice(words).strip().lower())
        # guess_word_list = list(guess_word)
    return guess_word

#Escenario del juego
def scenary(tries):
    stages = [  # head + torso + two arms + two legs + open trap
                """
                    @--------
                    |       |
                    0       |
                   \|/      |
                    |       |
                   / \      |
                      >------
                    /       |
                """,
                # head + torso + two arms + two legs
                """
                   @--------
                   |       |
                   0       |
                  \|/      |
                   |       |
                  / \      |
                  --->------
                           |
                """,
                # head + torso + two arms + left leg
                """
                   @--------
                   |       |
                   0       |
                  \|/      |
                   |       |
                  /        |
                  --->------
                           |
                """,
                # head + torso + two arms
                """
                   @--------
                   |       |
                   0       |
                  \|/      |
                   |       |
                           |
                  --->------
                           |
                """,
                # head + left arm + torso
                """
                   @--------
                   |       |
                   0       |
                  \|       |
                   |       |
                           |
                  --->------
                           |
                """,
                # head + left arm
                """
                   @--------
                   |       |
                   0       |
                  \        |
                           |
                           |
                  --->------
                           |
                """,
                # head
                """
                   @--------
                   |       |
                   0       |
                           |
                           |
                           |
                  --->------
                           |
                """,
                 # initial empty state
                """
                   @--------
                   |       |
                           |
                           |
                           |
                           |
                  --->------
                           |
                """
    ]
    return stages[tries]

# Inicio del juego
def game():
    main_word = get_data()
    main_word_underscore = ['_'] * len(main_word) # Se ponen _ en cada posicion de la palabra
    win = False
    written_letters = []
    written_words = []
    tries = 7
    print('''
    ADIVINA LA PALABRA...
    ''')
    print(scenary(tries))

    for element in main_word_underscore:    # Se deja en blanco cada una de las letras que forman la palabra, excepto el _
        print(element + ' ', end='')
    print('\n')

    while not win and tries > 0:
        letter = normalize(input('Ingrese una letra: ').strip().lower()) # Se normaliza la entrada de teclado como una letra sin tildes y en minuscula
        if len(letter) == 1 and letter.isalpha():   # Se comprueba que se haya escruto un elemento y que este sea de caracter alfabetico
            if letter in written_letters:   # Se verifica que la letra escrita no se haya dilingnciado anteriormente
                print('''
                Ya escribió la letra''',letter)
                print('\n')
            elif letter not in main_word:   # Se verifica que la letra escrita no pertenezca a la palabra a adivinar
                print('''
                Palabra incorrecta!
                ''')
                tries -= 1
                written_letters.append(letter)
                print('Palabras esritas', written_letters)
            else:       # La letra escrita corresponde a una lentra de la palabra seleccionada
                print('''
                Palabra correcta''', letter)
                written_letters.append(letter)
                word_list = list(main_word_underscore)
                indxs = [index for index, lttr in enumerate(main_word) if lttr == letter] #Se recorre la letra escogida de forma aleatoria para obtener su indice y letra correspondiente siempre y cuando la letra escrita sea igual en posicion y carcater a una o varias letras de la palabra
                for indx in indxs:
                    word_list[indx] = letter
                main_word_underscore = ''.join(word_list)
                if '_' not in main_word_underscore: # Si ya no quedan _ por llenar en la palbra escogida
                    win = True
        elif len(letter) == len(main_word) and letter.isalpha():    # Se verifica el tamaño de la la enrtada con el tamaño de la palabra selesccionada y con que esta entra de la entrda del teclado sea de caracater alfabetico
            if letter in written_words:
                print('''
                EXCELENTE, ha ADIVINADO la palabra''', letter, '\n')
            elif letter != main_word:
                print(letter, '''No es la palabra
                ''')
                tries -= 1
                written_words.append(letter)
            else:       # Si la palabra corresponden a la palabra seleccionada, se cambia el falg win por True y se desbloquea la palabra
                win = True
                main_word_underscore = main_word
        else:
            print('Palabra no valida...')
        
        print(scenary(tries))
        print(main_word_underscore, '\n')
    
    if win: 
        print('''
        EXCENTENTE, has GANADO, la palabra es:''', main_word, '\n')
    else:
        print('''
        Has PERDIDO el juego. La palabra es:''', main_word, '\n')

  

def menu():
    os.system('clear')
    print('''
    ---------------------------------------------------------------------
    |   AA    HH  HH    OOO    RRRRR   CCCCCC    AA    DDDD       OOO   |
    | AA  AA  HH  HH  OO   OO  RR  RR  CC  CC  AA  AA  DD  DD   OO   OO |
    | AAAAAA  HHHHHH  OO   OO  RRRRR   CC      AAAAAA  DD   DD  OO   OO |
    | AA  AA  HH  HH  OO   OO  RR  RR  CC  CC  AA  AA  DD  DD   OO   OO |
    | AA  AA  HH  HH    OOO    RR  RR  CCCCCC  AA  AA  DDDDD      OOO   |
    ---------------------------------------------------------------------
    [1]. Jugar
    [2]. Salir
    ''')
    option = input('Ingrese una de las opciones: ')
    try:
        if int(option) == 1:
            game()
        elif int(option) == 2:
            os.system('clear')
            print('''
            Hasta una proxima
            ''')
            exit()
        else:
            print(ValueError)
    except ValueError as ve:
        print(ve)
    
#Codigo principal
if __name__ == "__main__":
    menu()