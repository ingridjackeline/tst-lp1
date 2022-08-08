# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula dados referentes ao salário de um usuário 

salario_bruto = float(input())
horas_trabalho = int(input())

hora_bruta = salario_bruto / horas_trabalho 

ir = 0.11 * salario_bruto 
inss = 0.08 * salario_bruto 
sindicato = 0.05 * salario_bruto 
descontos = ir + inss + sindicato

salario_liquido = salario_bruto - descontos 
hora_liquida = salario_liquido / horas_trabalho 

print(f"Salário Bruto = {salario_bruto:.2f}")
print(f"Hora Bruta = {hora_bruta:.2f}")
print(f"Desconto IR = {ir:.2f}")
print(f"Desconto INSS = {inss:.2f}")
print(f"Desconto Sindicato = {sindicato:.2f}")
print(f"Salário Líquido = {salario_liquido:.2f}")
print(f"Hora Líquida = {hora_liquida:.2f}")


