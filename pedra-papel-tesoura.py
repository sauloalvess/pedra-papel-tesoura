import random

def play():
    jogador = input("O que voce vai jogar? 'p' para Pedra, 'a' para Papel e 't' para Tesoura\n")
    computador = random.choice(['p','a','t'])

    if jogador == computador:
        return 'Empate!'

    if venceu(jogador, computador):
        return 'PA-RA-BEINX! VOCE VENCEU!'

    return 'Voce perdeu :('

# Pedra > Tesoura, Tesoura > pApel, pApel > Pedra  
def venceu(jogador, computador): # Retorna True se o jogador vencer
    if (jogador == 'p' and computador == 't') or (jogador == 't' and computador == 'a') or (jogador == 'a' and computador == 'p'):
        return True

# Mantém a jogatina acontecendo :)
jogador = False

while jogador == False:
    print(play())
    jogador == False