# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que contabiliza o número de palavras iniciadas por consoante 

quantidade = int(input())

palavras = []
inicial_consoante = 0

for num in range(quantidade):
	palavra = input()
	palavras.append(palavra)
	
for palavra in palavras:
	if palavra[0] not in "aeiouAEIOU":
		inicial_consoante += 1	
		
porcentagem = inicial_consoante * 100 / quantidade
		
print(f"total de palavras: {quantidade}")
print(f"iniciadas por consoantes: {inicial_consoante} ({porcentagem:.2f}%)")
