# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula quantas caixas de cerâmica serão utilizadas para revestir o vão

capacidade_caixa = float(input("Capacidade de revestimento? "))

print()
print("== Dados do vão a revestir ==")

comprimento = float(input("Comprimento? "))
largura = float(input("Largura? "))
altura = float(input("Altura? "))

area_chao = comprimento * largura
area_paredes = (2 * comprimento * altura) + (2 * largura * altura) 
area_total = area_chao + area_paredes

num_caixas = area_total / capacidade_caixa

print()
print("== Resultados ==")
print(f"Área total a revestir: {area_total:.1f} m2")
print(f"Número de caixas: {num_caixas:.0f}")
