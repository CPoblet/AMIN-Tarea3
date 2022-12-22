import numpy as np
import pandas as pd
import sys
import csv

#py main.py 0 100000 1.4

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
    """ i = np.random.randint(0, n)
    solution[i] = 1 """
    return solution

def test_fitness(price, weight, solution):
    fitness = np.zeros_like(price, dtype=float)
    norm_p = np.full_like(price, price)
    norm_p = norm_p/(np.amax(price)+1)
    for i in range(len(solution)):
        carga_i = evaluation(solution, price, weight)
        if solution[i] == 1:
            solution[i] = 0
            fitness[i] = carga_i[1] + norm_p[i]
            solution[i] = 1
        else:
            solution[i] = 1
            fitness[i] = carga_i[0] + norm_p[i]
            solution[i] = 0
    return fitness


def sort_fitness(fitness):
    fitness_sorted = np.zeros((2, len(fitness)))
    min = np.amin(fitness)
    for i in range(fitness_sorted.shape[1]):
        max = np.amax(fitness)
        index = np.where(fitness == max)
        fitness[index] = min-1
        fitness_sorted[0][i] = index[0][0]
        fitness_sorted[1][i] = max
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
    input_file = argv[4]
    output_file = argv[5]
    print(argv)
    np.random.seed(seed=seed)
    np.set_printoptions(suppress=True)
    # price, weight
    # z,c
    params_data = pd.read_csv(input_file, skiprows=1, delim_whitespace=True, header=None, nrows=3, usecols=[1]).to_numpy()
    #print(data)
    #print(params_data)
    n = int(params_data[0])
    c = int(params_data[1])
    data = pd.read_csv(input_file, skiprows=5, delimiter=',', header=None, nrows=n, usecols=[1, 2, 3]).transpose().to_numpy()
    roulette = generate_roulette(t, n)
    #print(roulette)
    best_solution = random_solution(n)
    eva_best_solution = evaluation(best_solution, data[0], data[1])
    #print(solution)
    if eva_best_solution[1] > c:
        best_solution = np.zeros(n, dtype=int)
        eva_best_solution = evaluation(best_solution, data[0], data[1])

    count = -1
    #eva_best_solution[0] != 8373
    while count < iter:
        count += 1
        fitness = test_fitness(data[0], data[1], best_solution)
        fitness_sorted = sort_fitness(fitness)
        solution = np.empty_like(best_solution)
        solution[:] = best_solution
        r = np.random.rand()
        j = select_roulette(roulette)
        x = int(fitness_sorted[0][j])
        solution[x] = np.absolute(solution[x]-1)
        eva_solution = evaluation(solution, data[0], data[1])
        if eva_solution[1] <= c:
            best_solution = solution
            eva_best_solution = eva_solution
    print(best_solution)
    print(eva_best_solution)
    with open(output_file, newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open(output_file, 'w', newline='') as f:
        w = csv.writer(f)
        w.writerows(data)
        w.writerow([t, eva_best_solution[0]])

if __name__ == '__main__':
    main(sys.argv)