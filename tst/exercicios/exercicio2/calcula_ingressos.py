# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o valor total a ser pago pelos ingressos do cinema 

adultos = int(input())
criancas = int(input())
ingresso = float(input())

valor_total = (adultos * ingresso) + (criancas * ingresso / 2)

print(f"Total: R$ {valor_total:.2f}")

