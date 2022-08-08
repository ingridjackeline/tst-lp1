# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o valor total a ser pago a um funcionário no mês natalino 

codigo = int(input())

if codigo == 1 or codigo == 2:
	if codigo == 1:
		print("Deverá receber em dezembro R$ 25000.00.")
		
	else:
		print("Deverá receber em dezembro R$ 15000.00.")
		
elif codigo == 3 or codigo == 4 or codigo == 5:
	faltas = int(input())
	if codigo == 3:
		if faltas == 0:
			print("Valor da gratificação R$ 500.00.")
			print("Deverá receber em dezembro R$ 8500.00.")
		else:
			gratificacao = (235 - faltas) * 2
			salario = 8000 + gratificacao 
			print(f"Valor da gratificação R$ {gratificacao:.2f}.")
			print(f"Deverá receber em dezembro R$ {salario:.2f}.")	
			
	elif codigo == 4:
		if faltas == 0:
			print("Valor da gratificação R$ 300.00.")
			print("Deverá receber em dezembro R$ 5300.00.")
		else:
			gratificacao = (235 - faltas) * 1
			salario = 5000 + gratificacao 
			print(f"Valor da gratificação R$ {gratificacao:.2f}.")
			print(f"Deverá receber em dezembro R$ {salario:.2f}.")	
			
	else:
		if faltas == 0:
			print("Valor da gratificação R$ 200.00.")
			print("Deverá receber em dezembro R$ 3000.00.")
		else:
			gratificacao = (235 - faltas) * 0.70
			salario = 2800 + gratificacao 
			print(f"Valor da gratificação R$ {gratificacao:.2f}.")
			print(f"Deverá receber em dezembro R$ {salario:.2f}.")			
