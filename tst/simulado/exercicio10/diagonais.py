# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o número de diagonais de um polígono 

lados = int(input())

diagonais = lados * (lados - 3) // 2 

print(f"{lados} lados => {diagonais} diagonais")
