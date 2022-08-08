# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o IMC ideal do usuário, bem como o seu peso a ser perdido ou ganho 

peso = float(input())
altura = float(input())

imc = peso / altura ** 2

peso_ideal = 24.9 * altura ** 2
peso_final = peso_ideal - peso

print(f"IMC atual = {imc:.2f}")
print(f"Peso a ser ganho/perdido = {peso_final:.2f}")
