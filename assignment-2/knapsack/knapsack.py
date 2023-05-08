import sys
import argparse


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
