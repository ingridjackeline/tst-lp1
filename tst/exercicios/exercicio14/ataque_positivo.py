# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que identifica o(s) ataque(s) mais positivo(s) de um campeonato

num_times = int(input())

nome_times = []
gols_times = []
total_gols = 0
maior_ataque = 0

if num_times > 2:
	for i in range(num_times):
		nome = input()
		gols = int(input())
		nome_times.append(nome)
		gols_times.append(gols)
		total_gols += gols
		
		if gols > maior_ataque:
			maior_ataque = gols
			
	media_gols = total_gols / num_times		

	print(f"Time(s) com melhor ataque ({maior_ataque} gol(s)):")

	for i in range(num_times):
		if gols_times[i] == maior_ataque:
			print(nome_times[i])
					
	print()
	print(f"Média de gols marcados: {media_gols:.1f}")
