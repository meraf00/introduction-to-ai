import sys
import argparse
import random


def generate_items(
    filename,
    n_item_types: int = 10,
    capacity: float = 50,
    min_item_weight: float = None,
    max_item_weight: float = None,
    min_item_count: int = 1,
    max_item_count: int = 5,
):
    min_item_weight = min_item_weight or 1
    max_item_weight = max_item_weight or capacity

    if min_item_weight > max_item_weight:
        raise ValueError(
            "Min item weight must be greater than or equal to Max item weight."
        )

    if min(capacity, max_item_weight, min_item_weight) < 0:
        raise ValueError("Weight can't be negative.")


def load_knapsack_problem(filename):
    with open(filename) as f:
        lines = f.readlines()

        max_weight = int(lines[0].strip())

        items = {}

        for line in lines[2:]:
            item_name, weight, value, count = map(
                lambda string: string.strip(), line.split(",")
            )
            item = {
                "name": item_name,
                "weight": float(weight),
                "value": float(value),
                "count": int(count),
            }

            items[item_name] = item

    return max_weight, items


if __name__ == "__main__":
    parse = argparse.ArgumentParser(
        description="Solve knapsnack problem using Genetic Algorithm, Hill Climbing or Simulated Annealing"
    )

    parse.add_argument(
        "--algorithm",
        choices=["ga", "hc", "sa"],
        help="Choose from genetic algorithm (ga), hill climbing (hc) or simulated annealing (sa)",
        action="store",
        required=True,
    )
    parse.add_argument(
        "--file", help="Path to file containing items", action="store", required=True
    )

    args = parse.parse_args(sys.argv[1:])

    try:
        problem = load_knapsack_problem(args.file)
        print(problem)

    except FileNotFoundError:
        print(f"Can't find file '{args.file}'")

    except ValueError as e:
        print("Unexpected file content.")
