from graphics import *
from random import randint

# win = GraphWin("Learner",500,300)

# init pop
def _init(pop_size, dna_size):
    poputation = []

    for i in range(pop_size):
        new_dna = []
        for j in range(dna_size):
            new_dna.append(randint(0,4))
        poputation.append(new_dna)
    return poputation

# compute fitness
# dna,goal => fitness
def is_dna_valid(dna, goal):
    if len(dna) != len(goal):
        return False
    else :
        return True

def _fitness(dna, goal):
    if(is_dna_valid(dna, goal)):
        score = 0.0
        for i in range(len(goal)):
            if dna[i] == goal[i]:
                score = score + 1

        return (int) (score/len(goal) * 100)
    else:
        return -1

# select the better ones
# population => best maybe (parents)
def compute_probability(fitness):
    if 0 <= fitness & fitness < 10 :
        return 10
    if 10 <= fitness & fitness < 20 :
        return 20
    if 20 <= fitness & fitness < 30 :
        return 30
    if 30 <= fitness & fitness < 40 :
        return 40

def compute_random_probability(num):
    num = randint(0,100)

    if 0 <= num & num < 10 :
        return 10
    if 10 <= num & num < 80 :
        return 70
    if 80 <= num & num < 100 :
        return 20

def add_or_not(fitness):
    num = randint(0,100)

    random_prob= compute_random_probability(num)
    fitness_prob = compute_random_probability(fitness)

    return fitness_prob == random_prob

def _selection(population, goal):
    next_parents =  []
    
    for person in population:
        fit = _fitness(person,goal)
        if add_or_not(fit):
            next_parents.append(person)
        
    return next_parents

# crossover 
# parents => offsprings
def _crossover(parents): 
    next_generation = []

    for index in range(len(parents)):
        parent1  = parents[index] 
        parent2  = parents[-index-1] 
        new_child = []
        for i in range(len(parent1)):
            if i%2 == 0: new_child.append(parent1[i])
            else: new_child.append(parent2[i])

        next_generation.append(new_child)
    if len(next_generation) == len(parents):
        return next_generation

    return next_generation

# mutate new population
def mutation_rate(population_length):
    return (1/population_length) * 100

def genererate_mutant():
    return randint(0,4)

def _mutate(offsprings, rate):
    mutants = offsprings[:]
    
    for i in range(len(offsprings)):
        offspring = offsprings[i]

        for j in range(len(offspring)):
            chance = compute_probability(randint(0,100))
            # print("Chance ", chance)
            if chance == rate :
                mutants[i][j] = genererate_mutant()
                print("Mutated")
                print(offspring)                
                print(mutants[i])

    return mutants
    
# --> repeat

#win.getMouse()
#win.close()

## START
GOAL = [1,1,1,1,1,1,1,1,1,1,1,1]
MUTATION_RATE = 10 # 10-20-30 or 40 %

poputation = _init(10,(len(GOAL)))

for i in range(0,100) :
    print("Generation ",i)
    print("Population ->",poputation)

    selected = _selection(poputation, GOAL)

    print("Selected - - > ",selected)

    offsprings = _crossover(selected)

    mutants = _mutate(offsprings, MUTATION_RATE)

    new_population = selected + mutants

    #print(new_population)

    poputation = new_population