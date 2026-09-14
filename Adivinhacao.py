from random import randint
computador = randint (0, 10) #importanto a biblioteca e declarando o número aleatório
print("Acabei de pensar em um número de 0 a 10.")
jogador = " "
somatentativas = 0
while jogador != computador: #enquanto o número for diferente 
    jogador = int(input("Qual seu palpite? ")) #input do palpite
    somatentativas += 1 #a cada ciclo do laço, soma-se uma tentativa a mais
    if jogador < computador: #se o num aleatorio for maior,
        print("Mais... Tente mais uma vez.")
    elif jogador > computador: #se o num aleatorio for menor,
        print("Menos... Tente mais uma vez.")
    elif jogador == computador: #se o jogador ACERTAR o num aleatorio,
        print(f"PARABÉNS, VOCÊ ACERTOU! Número {computador}!")
print(f"Você precisou de {somatentativas} chances para acertar.")
