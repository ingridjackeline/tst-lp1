# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o valor para emoldurar quadros 

comprimento = float(input())
largura = float(input())

tamanho_m = (2 * comprimento + 2 * largura) / 100
preco = tamanho_m * 120

print(f"R$ {preco:.1f}") 
