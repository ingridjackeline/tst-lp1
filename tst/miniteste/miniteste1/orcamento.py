# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o orçamento de uma peça 

nome = input("Nome? ")
valor = float(input("Valor da letra (R$)? "))

letras = len(nome)
orcamento = valor * letras 

print(f"Preço final: R$ {orcamento:.2f}")
