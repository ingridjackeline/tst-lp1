# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que analisa uma sequência de números e identifica o ponto em que a média ultrapassa um certo limite

sequencia_elementos = []

while True:
	elemento = input()
	
	if elemento == "-": break
	
	sequencia_elementos.append(float(elemento))
	
media_limite = float(input())	

soma_elementos = sequencia_elementos[0]
quant_elementos = 1

while True:
	media = soma_elementos / quant_elementos
	
	if media > media_limite:
		print(f"media = {media:.1f}")
		print(f"num = {quant_elementos}")
		break
		
	if quant_elementos == len(sequencia_elementos): 
		print("limite não alcançado")
		break	
		
	soma_elementos += sequencia_elementos[quant_elementos]
	quant_elementos += 1
