from random import choice

palavras = 'arvore manga tutorial python jogo'.split()
palavra = choice(palavras)
palavraOcultada = []
letrasCertas = []
letrasAcertadas = []
letrasUsadas = []
vidas = 6

for letra in palavra:
    palavraOcultada.append('_ ')
    letrasCertas.append(letra)

print("".join(palavraOcultada))
while True:
    achou = False
    palpite = str(input('Digite uma letra: '))
    while True:
        if letrasUsadas.count(palpite[0]) == 1:
            if palpite == palavra:
                print('Parabéns, você venceu o jogo. Palavra:', palavra + '. Vidas restantes:', vidas)
                break
            print('Você já usou essa letra. Tente novamente: ')
            palpite = str(input('Digite uma letra: '))
        else:
            if palpite == palavra:
                print('Parabéns, você venceu o jogo. Palavra:', palavra + '. Vidas restantes:', vidas)
                break
            break
    if palpite == palavra:
        break
    letrasUsadas.append(palpite[0])
    i = 0
    for letra in letrasCertas:
        if palpite[0] == letra:
            letrasAcertadas.append(letra)
            palavraOcultada[i] = palpite[0]
            achou = True
        i = i + 1
    if achou == False:
        vidas = vidas - 1
    if "".join(palavraOcultada) == palavra:
        print('Parabéns, você encontrou a palavra:', palavra + '. Vidas restantes:', vidas)
        break
    print("".join(palavraOcultada))
    print('Letras usadas: {}'.format("".join(letrasUsadas)))
    if vidas <= 0:
        print('Você perdeu todas as vidas! A palavra era:', palavra)
        break
