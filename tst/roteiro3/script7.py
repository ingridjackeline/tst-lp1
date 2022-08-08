# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que converte temperaturas Celsius para Fahrenheit e Kelvin

celsius = float(input("Temperatura em Celsius (°C): "))

fahrenheit = (9 * celsius + 160) / 5
kelvin = celsius + 273 

print(f"Temperatura em Fahrenheit: {fahrenheit:.1f}°F")
print(f"Temperatura em Kelvin: {kelvin:.1f}K") 

