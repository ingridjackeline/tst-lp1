# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que determina qual o espaço em disco ocupado pelos usuários

usuario1 = input()
bytes1 = int(input())
usuario2 = input()
bytes2 = int(input())
usuario3 = input()
bytes3 = int(input())

mbytes1 = bytes1 / 1048576
mbytes2 = bytes2 / 1048576
mbytes3 = bytes3 / 1048576

espaco_total = mbytes1 + mbytes2 + mbytes3 
espaco_medio = espaco_total / 3

print("SPLab - Espaço utilizado pelos usuários")
print("---------------------------------------------")
print("Nr., Usuário, Espaço Utilizado")
print()
print(f"1, {usuario1}, {mbytes1:.2f} MB")
print(f"2, {usuario2}, {mbytes2:.2f} MB")
print(f"3, {usuario3}, {mbytes3:.2f} MB")
print()
print(f"Espaço total ocupado: {espaco_total:.2f} MB")
print(f"Espaço médio ocupado: {espaco_medio:.2f} MB")
