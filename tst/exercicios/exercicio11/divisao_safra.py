# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula a divisão da safra entre os clientes do fazendeiro 

safra = int(input())
clientes_a = int(input())
clientes_v = int(input())

quantidade_a = safra // clientes_a
quantidade_v = safra % clientes_a / clientes_v

print(f"Clientes no atacado = {quantidade_a}kg cada.")
print(f"Clientes no varejo = {quantidade_v:.2f}kg cada.")
