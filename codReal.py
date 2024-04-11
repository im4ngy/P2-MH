import random
import math
from itertools import permutations

def evaluateSolution(data, solution):
    error = 0
    for x,y in data:
        yPredicted=0
        index=0
        for i in solution:
            yPredicted+=i*(x**index)
            index+=1
        error+=abs(yPredicted-y)
    return error/len(data)

def permutations_of_n(n):
    numbers = list(range(1, n + 1))
    
    # Generar todas las permutaciones de la lista de números
    all_permutations = permutations(numbers)
    
    # Convertir las permutaciones en una lista de listas
    permutaciones_list = [list(perm) for perm in all_permutations]
    
    return permutaciones_list

def selection1(population, nWinners):
    
    sorted_population = sorted(population, key=lambda x: x[1])
    print("\n", sorted_population)
    winners=sorted_population[:nWinners]
    return winners

"""
    This crossover is going to cut len(population)-1 times and takes 1 solution
"""
def simple_crossover(population):
    position=10
    cuts=[]
    cuts.append(0)
    for i in range(len(population)-1):
        while position in cuts:
            if(random.randint(1,2)%2==0):
                position=random.randint(1,position)
            else:
                position=random.randint(position,10)            
        cuts.append(position)
    cuts.sort()
    print("Los cortes a realizar son: ",cuts,"\n")

    differents_sons=math.factorial(len(population))

    permutations=permutations_of_n(len(population));
    childs=[]
    actual_child=[1,2,3,4,5,6,7,8,9,10]
    for i in range(len(permutations)):
        for j in range(len(cuts)):                        
            actual_permutation=permutations[i]
            print(actual_permutation[j]-1)
            father=population[actual_permutation[j]-1]
            if(j!=0):
                print(j)
                actual_child[cuts[j-1]:cuts[j]]=father[cuts[j-1]:cuts[j]]
            else:
                actual_child[:cuts[j]]=father[:cuts[j]]
        print(actual_child)
        childs.append(actual_child)
    
    

def applyGeneticOperators(population, k, cProb, mProb):

    newPopulation = []
    #Choose parents through a tournament selector (size k)
    newPopulation=selection1(population, 3)
    print("\n Se han seleccionado ", len(newPopulation), " ganadores")
    
    #Cross parents with a probability cProb
    #if random.randint(1,100) <= cProb:
    simple_crossover(newPopulation)
    #Mutate parents with a probability mProb
    #if random.randint(1,100) <= mProb:


    return newPopulation #Return the new population (without evaluating it)

def main():
    data = [
        [-3, 208],
        [-2, 3],
        [-1, 0],
        [0, 1],
        [1, 24],
        [2, 303],
        [3, 2008]
    ]
    nSolutions = 25 #Population size
    maxGenerations = 2 #Number of generations
    k = 3 #Tournament size to select parents
    cProb = 0.7 #Crossover probability
    mProb = 0.1 #Mutation probability
    minValue=-100
    maxValue=100
    l=10 #Function of the type y = ax^9+bx^8+cx^7+dx^6+ex^5+fx^4+gx^3+hx^2+ix+j

    ##We generate random solutions
    population = []
    for i in range(nSolutions):
        ##We generate nSolutions random solutions
        solution = []
        for j in range(l):
            variable = random.randint(minValue,maxValue)
            solution.append(variable)            
        population.append([solution,evaluateSolution(data, solution)])
    
    it=1
    while it < maxGenerations:    
        newPopulation = applyGeneticOperators(population,k,cProb,mProb)
        #Generational schema
        population = []
        for solution in newPopulation:
            population.append([solution[0],evaluateSolution(data,solution[0])])
        it+=1

if __name__ == "__main__":
    main()
