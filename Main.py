# -*- coding: utf-8 -*-
from graphics import *
from random import randint
import math

# win = GraphWin("Learner",500,300)

# init pop
def create_person():
    num = randint(0,4)
    return num

def _init(pop_size, dna_size):
    poputation = []

    for i in range(pop_size):
        new_dna = []
        for j in range(dna_size):
            new_person = create_person()
            new_dna.append(new_person)
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

        return (score/len(goal) * 100)
    else:
        return -1

# select the better ones
# population => best maybe (parents)

def add_or_not(fitness, maxFitness):
    num = randint(0,maxFitness)
    return num <= fitness

def compute_fitnesses(population, goal):
    best_fitness = 0
    population_with_fitness = []

    for person in population:
        count = 0.0
        for i in range(len(person)):
            if person[i] == goal[i]: 
                count = count+1
        fitness = math.floor(count/len(goal) * 100)
        population_with_fitness.append([person,fitness])
        if best_fitness < fitness:
            best_fitness = fitness
    return population_with_fitness,best_fitness

def _selection(population_with_fitness, maxFitness):
    next_parents =  []

    for person in population_with_fitness:
        fit = person[1]
        if add_or_not(fit, maxFitness):
            next_parents.append(person[0])

    return next_parents

# crossover 
# parents => offsprings
def _crossover(parents): 
    next_generation = []

    for index in range(len(parents)/2):
        parent1  = parents[index] 
        parent2  = parents[-index-1] 
        new_child1 = []
        new_child2 = []
        for i in range(len(parent1)):
            if i%2 == 0: 
                new_child1.append(parent1[i])
                new_child2.append(parent2[i])
            else: 
                new_child1.append(parent2[i])
                new_child2.append(parent1[i])
        next_generation.append(new_child1)
        next_generation.append(new_child2)
        if len(next_generation) >= len(parents):
            return next_generation

    return next_generation

# mutate new population


def mutate(person, mutation_rate):
    mutated = 0
    mutant = []
    for i in person: 
        if randint(0,100) < mutation_rate:
            mutated = mutated + 1
            mutant.append(create_person())
        else:
            mutant.append(i)

    if mutated != 0:        
        print "Mutation: ", person , "-->", mutant
    return mutant

def _mutate_all(offsprings, rate):
    mutants = []
    
    for offspring in offsprings:
        mutants.append(mutate(offspring, rate))

    return mutants
    
# --> repeat

#win.getMouse()
#win.close()

## START
GOAL = [1,2,3,4]
MUTATION_RATE = 0.1

poputation = _init(6,(len(GOAL)))
max_fitness = 0
counter = 0
while max_fitness <= 70:
    counter = counter + 1

    print 
    print "Generation ", counter ,"->",poputation

    population_with_fitness , max_fitness = compute_fitnesses(poputation, GOAL)

    print "Max fitness : " , max_fitness

    selected = _selection(population_with_fitness, max_fitness)

    print "Selected - - > ",selected

    offsprings = _crossover(selected)

    print "OffSpring" ,offsprings

    mutants = _mutate_all(offsprings, MUTATION_RATE)

    new_population = selected + mutants

    poputation = new_population

print "Done"

for person in population_with_fitness:
    if person[1] == max_fitness:
        print "Fittest: -> " ,  person[0]