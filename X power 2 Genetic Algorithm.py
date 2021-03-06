import math as m
from random import *
"""
+++++++++++++++++++++++++++++++++
INITIALIZATION GENETIC ALGORITHM
+++++++++++++++++++++++++++++++++
"""
randBinList = lambda n: [randint(0,1) for b in range(1,n+1)] #generate random binary
GENERATION = 4 #how many GENERATION?
DNA_SIZE = 5
chromosomeT=[]
chromosomeA=[]


for i in range(GENERATION):#generate the random binary and store it in list
    chromosomeT.append(randBinList(DNA_SIZE))

#change the binary list to string list
for i in chromosomeT:
    string = ''.join(str(j) for j in i)
    chromosomeA.append(str(string))

"""
+++++++++++++++++++++++++++++++++
EVALUATION GENETIC ALGORITHM
+++++++++++++++++++++++++++++++++
"""
ans,anspower,high,count,total=[],[],0,0,0

#find the fitness values in the population, average value and maximum
for i in chromosomeA:
    ans.append(int(i,2))
    anspower.append(int(i,2) ** 2)

for i in range(len(chromosomeA)):
    total = total + anspower[i]
ave = total / len(chromosomeA)

#PRINT RESULT
print("::::::::::F(x) = x^2 EVALUATION::::::::::")
print("CURRENT INDIVIDUAL: {}".format(chromosomeA))
print("x Value: {}".format(ans))
print("Fitness f(x) = x2: {}".format(anspower))
print("Sum: {}".format(total))
print("Average: {}".format(ave))
print("Max: {} \r\r".format(max(anspower)))    


"""
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
SELECTION GENETIC ALGORITHM USING ROULETTE WHEEL
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
for i in range(GENERATION):
	relative_fitness = [f/total for f in anspower]
	probabilities = [sum(relative_fitness[:i+1]) for i in range(len(relative_fitness))]

chosen =[]
for n in range(GENERATION):
        r = random()#give random float number between (0,1.0)
        for i, individual in enumerate(chromosomeA):
            if r <= probabilities[i]:
                chosen.append(individual)
                break

print("::::::F(x) = x^2 CHOSEN INDIVIDUAL:::::::")
print("{} \r\r\r".format(chosen))

"""
+++++++++++++++++++++++++++
CROSSOVER GENETIC ALGORITHM
+++++++++++++++++++++++++++
"""
def crossover(dna1,dna2):
	pos = int(random()*DNA_SIZE)
	print("Point Number: {}".format(pos+1))
	return (dna1[:pos]+dna2[pos:],dna2[:pos]+dna1[pos:],pos,pos)

print(":::::F(x) = x^2 CROSSOVER::::::::: \r")
print("::++BEFORE CROSSOVER++::")
print("{}\r".format(chosen))
print(":::++AFTER CROSSOVER++:::")
reproduction = []
point=[]

for i,x in enumerate(chosen):
	c = choice(chosen)
	ind1,ind2,p1,p2 = crossover(x,c)
	print("Father: {}".format(x))
	print("Mother: {}".format(c))
	print("Child 1: {}".format(ind1))
	print("Child 2: {}\r".format(ind2))
	point.append(p1)
	point.append(p2)
	reproduction.append(ind1)
	reproduction.append(ind2)
	if(x == c):
		chosen.remove(c)
	else:	
		chosen.remove(c)
		chosen.remove(x)
	
ans.clear()
anspower.clear()

for i in reproduction:
	ans.append(int(i,2))
	anspower.append(int(i,2)**2)

print("Offspring after crossover: {}".format(reproduction))
print("x Value: {}".format(ans))
print("Fitness f(x)=x^2: {}".format(anspower))
print("Sum: {}".format(sum(anspower)))
print("Average: {}".format(sum(anspower)/len(chromosomeA)))
print("Max: {}\r\r".format(max(anspower)))

"""
++++++++++++++++++++++++++
MUTATION GENETIC ALGORITHM
++++++++++++++++++++++++++
"""

def mutate(dna1):
	get=[]
	for i in dna1:
		if i == '1':
			get.append('0')
		else:
			get.append('1')

	string = ''.join(str(j) for j in get)
	string = str(string)
	return string		



print("::::::::::MUTATION::::::::::")
mutation = []
mutation_chance = 100
score=0

for x in reproduction:
	check = int(random()*mutation_chance)
	if check >90:
		score = mutate(x)
		mutation.append(score)
	else:
		mutation.append(x)

ans.clear()
anspower.clear()		
for i in mutation:
	ans.append(int(i,2))
	anspower.append(int(i,2)**2)

print("Offspring after mutation: {}".format(mutation))
print("x Value: {}".format(ans))
print("Fitness f(x) = x2: {}".format(anspower))
print('Sum: {}'.format(sum(anspower)))
print('Average: {}'.format(sum(anspower)/len(mutation)))
print('Max: {}\r'.format(max(anspower)))

print("Fittest f(x) = x^2: {}".format(max(anspower)))

