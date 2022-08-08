# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula quantas caixas um container comporta 

capacidade = int(input())
peso_caixasp = int(input())

num_caixasg = capacidade // 120 
cap_livre = capacidade % 120 

num_caixasp = cap_livre // peso_caixasp 
cap_restante = cap_livre % peso_caixasp

print(f"O container comporta {num_caixasg} caixa(s) grande(s).")
print(f"O container comporta {num_caixasp} caixa(s) pequena(s).")
print(f"Há {cap_restante}kg de capacidade restante.")
