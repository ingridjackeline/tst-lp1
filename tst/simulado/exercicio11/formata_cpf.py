# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime CPFs formatados e a soma dos seus dois últimos dígitos 

cliente1 = int(input())
cliente2 = int(input())
cliente3 = int(input())

inteiro1 = cliente1 // 100
decimal1 = cliente1 % 100
soma1 = decimal1 // 10 + decimal1 % 10 

inteiro2 = cliente2 // 100
decimal2 = cliente2 % 100
soma2 = decimal2 // 10 + decimal2 % 10 

inteiro3 = cliente3 // 100
decimal3 = cliente3 % 100
soma3 = decimal3 // 10 + decimal3 % 10 

print(f"{inteiro1}-{decimal1}")
print(soma1)
print(f"{inteiro2}-{decimal2}")
print(soma2)
print(f"{inteiro3}-{decimal3}")
print(soma3)




