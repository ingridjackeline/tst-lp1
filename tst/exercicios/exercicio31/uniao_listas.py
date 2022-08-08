# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que calcula a união entre duas listas passadas como parâmetro

def uniao_listas(l1, l2):
	for i in range(len(l1) - 1, 0, -1):
		for p in range(i - 1, -1, -1):
			if l1[p] == l1[i]:
				l1.pop(i)
				break
				
	for num2 in l2:
		conta_nums = 0
		for num1 in l1:
			if num1 == num2: break
			conta_nums += 1
		if conta_nums == len(l1):
			l1.append(num2)	
			
l1 = [2,1,3,4]
l2 = [2]
assert uniao_listas(l1,l2) == None
assert l1 == [2,1,3,4]
assert l2 == [2]

l1 = [1,3,4]
l2 = [4]
assert uniao_listas(l1,l2) == None
assert l1 == [1,3,4]
assert l2 == [4]

l1 = [2,4,1]
l2 = [6,7,91]
uniao_listas(l1,l2)
assert l1 == [2,4,1,6,7,91]
assert l2 == [6,7,91]			
