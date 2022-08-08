# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que cria uma estrela no turtle 

import turtle 

turtle.left(216)
turtle.color("yellow", "yellow")
turtle.begin_fill()

for i in range(5):
	turtle.right(144)
	turtle.forward(100)
	turtle.left(72)
	turtle.forward(100)
		
turtle.end_fill()
