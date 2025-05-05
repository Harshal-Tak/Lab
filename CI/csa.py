import random

def fitness(x):
    return x ** 2  # Objective: maximize x^2

def mutate(x, mutation_range=3, min_val=0, max_val=1023):
    # Random small change
    x += random.randint(-mutation_range, mutation_range)
    return max(min_val, min(max_val, x))  # Keep in range

def clonal_selection(pop_size=5, generations=10):
    population = [random.randint(0, 1023) for _ in range(pop_size)]

    for gen in range(generations):
        population.sort(key=fitness, reverse=True)
        clones = []

        for i in range(len(population)):
            num_clones = pop_size - i  # More clones for better ones
            clones += [mutate(population[i]) for _ in range(num_clones)]

        clones.sort(key=fitness, reverse=True)
        population = clones[:pop_size]
        print(f"Gen {gen+1}: Best = {population[0]}, Fitness = {fitness(population[0])}")

    print(f"Final Best = {population[0]}, Fitness = {fitness(population[0])}")


clonal_selection()
