# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa interativo que trata os dados recebidos de um termômetro digital

soma_temperaturas = 0
num_temperaturas = 0

while True:
	temperatura = float(input())
	
	soma_temperaturas += temperatura
	num_temperaturas += 1
	media_temperaturas = soma_temperaturas / num_temperaturas
	
	print(f"t = {temperatura:.1f} (média = {media_temperaturas:.1f})")
	
	if temperatura > 500:
		print("ALERTA: limite de temperatura atingido!")
		print(f"número de medições: {num_temperaturas}")
		break
