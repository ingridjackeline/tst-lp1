# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que representa números decimais na notação Excesso de 127 ou Complemento de 1 em tamanho de 8 bits

def excesso_127(numero):
	numero += 127
	num_binario = f"{numero:b}"
	
	while len(num_binario) < 8:
		num_binario = "0" + num_binario	
		
	return num_binario
		
		
def complemento1(numero):
	if numero >= 0:
		sinal = "positivo"
	else:
		sinal = "negativo"
		numero = abs(numero)
			
	num_binario = f"{numero:b}"

	while len(num_binario) < 8:
		num_binario = "0" + num_binario
			
	if sinal == "negativo":
		num_c1 = ""
		for binario in num_binario:
			if binario == "0":
				num_c1 += "1"
			else:
				num_c1 += "0"	
		num_binario = num_c1
				
	return num_binario
	
	
lista_binarios = []
		
while True:
	esquema = input().split()
	
	if esquema[0] == "***":
		break
	elif esquema[0] == "E127":
		num_e127 = excesso_127(int(esquema[1]))
		lista_binarios.append(num_e127)
	elif esquema[0] == "C1":
		num_c1 = complemento1(int(esquema[1]))
		lista_binarios.append(num_c1)
		
for binario in lista_binarios:
	print(binario)						
