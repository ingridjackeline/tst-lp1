# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que informa o status do aluno em uma unidade de Programação I 

num_minitestes = int(input())

mensagem1 = "Aluno ainda não aprovado na unidade"
mensagem2 = "Aluno aprovado na unidade"

if 1 <= num_minitestes < 4:
	nota1 = float(input())
	if num_minitestes != 1:
		nota2 = float(input())
		if num_minitestes == 2:
			media = (nota1 + nota2) / num_minitestes
		else:
			nota3 = float(input())
			media = ((nota1 + nota2 + nota3) / num_minitestes) - 0.5
		print(f"{media:.1f}")	
		if media >= 6.0:
			print(mensagem2)
		else:
			print(mensagem1)	
			
	else:
		print(nota1)
		print(mensagem1)		
