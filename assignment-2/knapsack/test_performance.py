from knapsack import *
from generate_item_list import generate_items

import time
import numpy as np


def test_hill_climbing(problem, max_capacity, n_iters=10):
    best_solution = None
    best_solution_score = float("-inf")

    average_runtime = 0

    for _ in range(n_iters):
        start_time = time.perf_counter()

        init_state = np.random.randint(2, size=len(problem["names"])).tolist()

        solution = hill_climbing(init_state, problem, max_capacity)

        end_time = time.perf_counter()

        average_runtime += end_time - start_time

        solution_score = calculate_fitness(
            solution, problem["prices"], problem["weights"], max_capacity
        )
        if solution_score > best_solution_score:
            best_solution = solution
            best_solution_score = solution_score

    average_runtime /= n_iters

    return average_runtime, best_solution, best_solution_score


def test_simulated_annealing(problem, max_capacity, n_iters=10):
    best_solution = None
    best_solution_score = float("-inf")

    average_runtime = 0

    for _ in range(n_iters):
        start_time = time.perf_counter()

        init_state = np.random.randint(2, size=len(problem["names"])).tolist()

        solution = simulated_annealing(init_state, problem, max_capacity)

        end_time = time.perf_counter()

        average_runtime += end_time - start_time

        solution_score = calculate_fitness(
            solution, problem["prices"], problem["weights"], max_capacity
        )
        if solution_score > best_solution_score:
            best_solution = solution
            best_solution_score = solution_score

    average_runtime /= n_iters

    return average_runtime, best_solution, best_solution_score


def test_genetic_algorithm(problem, max_capacity, n_iters=10):
    best_solution = None
    best_solution_score = float("-inf")

    average_runtime = 0

    for _ in range(n_iters):
        start_time = time.perf_counter()

        initial_population = generate_population(problem["counts"], population_size=200)

        solution = genetic_algorithm(problem, initial_population, max_capacity)

        end_time = time.perf_counter()

        average_runtime += end_time - start_time

        solution_score = calculate_fitness(
            solution, problem["prices"], problem["weights"], max_capacity
        )
        if solution_score > best_solution_score:
            best_solution = solution
            best_solution_score = solution_score

    average_runtime /= n_iters

    return average_runtime, best_solution, best_solution_score


def test():
    filenames = ["10_items.txt", "15_items.txt", "20_items.txt"]

    generate_items(filenames[0], n_item_types=10)
    generate_items(filenames[1], n_item_types=15)
    generate_items(filenames[2], n_item_types=20)

    for filename in filenames:
        print(f"Running test on {filename}")

        max_capacity, problem = load_knapsack_problem(filename)

        hc_time, _, hc_score = test_hill_climbing(problem, max_capacity)
        sa_time, _, sa_score = test_simulated_annealing(problem, max_capacity)
        ga_time, _, ga_score = test_genetic_algorithm(problem, max_capacity)

        print(hc_time, hc_score)
        print(sa_time, sa_score)
        print(ga_time, ga_score)
        print()


if __name__ == "__main__":
    test()
