# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime a hipotenusa de um triângulo retângulo 

cateto1 = float(input("Medida do Cateto 1? "))
cateto2 = float(input("Medida do Cateto 2? "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** 0.5

print(f"Medida da Hipotenusa: {hipotenusa:.2f}")
