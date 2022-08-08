# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que cria senhas de acordo com o nível de segurança desejado

def cria_senha_fraca(palavra):
	senha_fraca = "((" + palavra + "))"
	
	return senha_fraca
	
	
def cria_senha_forte(palavra):
	senha_fraca = "((" + palavra + "))"
	senha_forte = ""
	
	for caractere in senha_fraca:
		if caractere == "o" or caractere == "O":
			senha_forte += "0"
		elif caractere == "i" or caractere == "I" or caractere == "L" or caractere == "l":
			senha_forte += "1"
		elif caractere == "e" or caractere == "E":	
			senha_forte += "3"
		elif caractere == "a" or caractere == "A":	
			senha_forte += "4"
		elif caractere == "b" or caractere == "B":	
			senha_forte += "6"
		elif caractere == "t" or caractere == "T":	
			senha_forte += "7"
		else:
			senha_forte += caractere	
			
	return senha_forte
			

lista_senhas = []

while True:
	palavra_nivel = input().split()
	
	if palavra_nivel[0] == "***": 
		break
	elif palavra_nivel[1] == "fraco":
		senha_fraca = cria_senha_fraca(palavra_nivel[0])
		lista_senhas.append(senha_fraca)
	elif palavra_nivel[1] == "forte":
		senha_forte = cria_senha_forte(palavra_nivel[0])	
		lista_senhas.append(senha_forte)
	
for senha in lista_senhas:
	print(senha)	
