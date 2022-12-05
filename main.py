import numpy as np
import pandas as pd
import sys

def generate_roulette(t, n):
    probability = np.arange(1, n+1)
    probability = np.power(probability, -t)

    sum = np.sum(probability)

    proportion = np.zeros(n)
    for i in range(len(proportion)):
        p = probability[i]
        proportion[i] = p/sum

    roullete = np.zeros(n)
    roullete[0] = proportion[0]
    for i in range(1, len(proportion)):
        roullete[i] = roullete[i-1] + proportion[i]

    ##print(probability)
    ##print(proportion)
    ##print(roullete)
    return roullete

def random_solution(n):
    solution = np.zeros(n, dtype=int)
    for i in range(0, len(solution)):
        r = np.random.choice([0, 1])
        solution[i] = r
    return solution

def generate_fitness(price, weight):
    fitness = np.zeros_like(price, dtype=float)
    for i in range(len(fitness)):
        fitness[i] = price[i]/weight[i]
    return fitness

def sort_fitness(fitness):
    fitness_sorted = np.zeros((2, len(fitness)))
    max = np.amax(fitness)
    for i in range(fitness_sorted.shape[1]):
        min = np.amin(fitness)
        index = np.where(fitness == min)
        fitness[index] = max+1
        fitness_sorted[0][i] = index[0]
        fitness_sorted[1][i] = min
    return fitness_sorted

def evaluation(solution, price, weight):
    c = 0
    z = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            c = c + price[i]
            z = z + weight[i]
    return c, z

def select_roulette(roulette):
    r = np.random.rand()
    for i in range(len(roulette)):
        if r <= roulette[i]:
            return i

def main(argv):
    seed = int(argv[1])
    iter = int(argv[2])
    t = float(argv[3])
    print(argv)
    np.random.seed(seed=seed)
    np.set_printoptions(suppress=True)
    # price, weight
    # z,c
    data = pd.read_csv('knapPI_1_50_1000.csv', skiprows=5, delimiter=',', header=None, nrows=50, usecols=[1, 2, 3]).transpose().to_numpy()
    params_data = pd.read_csv('knapPI_1_50_1000.csv', skiprows=1, delim_whitespace=True, header=None, nrows=3, usecols=[1]).to_numpy()
    #print(data)
    #print(params_data)
    n = params_data[0]
    roulette = generate_roulette(t, n)
    #print(roulette)
    best_solution = random_solution(n)
    eva_best_solution = evaluation(best_solution, data[0], data[1])
    #print(solution)

    fitness = generate_fitness(data[0], data[1])
    #print(fitness)
    fitness_sorted = sort_fitness(fitness)
    #print(fitness_sorted)

    for i in range(iter):
        solution = best_solution
        r = np.random.rand()
        j = select_roulette(roulette)
        x = int(fitness_sorted[0][j])
        solution[x] = np.absolute(solution[x]-1)
        eva_solution = evaluation(solution, data[0], data[1])
        if eva_solution[0] >= eva_best_solution[0] and eva_solution[1] <= eva_best_solution[1]:
            best_solution = solution
            eva_best_solution = eva_solution
    print(best_solution)
    print(eva_best_solution)

if __name__ == '__main__':
    main(sys.argv)