# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o valor de uma passagem aérea e as alternativas de pagamento 

distancia = float(input())
aliquota = float(input())

passagem = distancia * aliquota + 51

vista = passagem - 0.25 * passagem
seis_parcelas = passagem - 0.05 * passagem 
parcela6 = seis_parcelas / 6 
parcela10 = passagem / 10 

print(f"Valor da passagem: R$ {passagem:.2f}")
print()
print("Pagamento:")
print(f"1. À vista. R$ {vista:.2f}")
print(f"2. Em 6 parcelas. Total: R$ {seis_parcelas:.2f}")
print(f"   6 x R$ {parcela6:.2f}")
print(f"3. Em 10 parcelas. Total: R$ {passagem:.2f}")
print(f"   10 x R$ {parcela10:.2f}")
