import random

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

def applyGeneticOperators(population, k, cProb, mProb):

    newPopulation = []
    #Choose parents through a tournament selector (size k)

    #Cross parents with a probability cProb
    #if random.randint(1,100) <= cProb:

    #Mutate parents with a probability mProb
    #if random.randint(1,100) <= mProb:


    return newPopulation #Return the new population (without evaluating it)

def main():
    data = [
        [-3,-329.24],
        [ -2.5,-18.696777],
        [-2,8.97],
        [-1.5,0.072636719],
        [-1,-2.86],
        [-0.5,-1.8504492],
        [0,0.25],
        [0.5,5.3464648],
        [1,27.12],
        [1.5,136.69088],
        [2,617.21],
        [2.5,2366.1753],
        [3,7788.22]
    ]    nSolutions = 25 #Population size
    maxGenerations = 1 #Number of generations
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
