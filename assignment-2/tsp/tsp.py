import sys
import argparse


def load_romania(filename):
    ...


if __name__ == "__main__":
    parse = argparse.ArgumentParser(
        description="Solve traving salesperson problem using Genetic Algorithm, Hill Climbing or Simulated Annealing"
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
        problem = load_romania(args.file)
        print(problem)

    except FileNotFoundError:
        print(f"Can't find file '{args.file}'")

    except ValueError as e:
        print("Unexpected file content.")
