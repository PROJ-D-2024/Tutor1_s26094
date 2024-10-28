import argparse
import random

def main():
    parser = argparse.ArgumentParser(description="A simple random number generator")

    parser.add_argument('--min', type=int, help="Minimal value")
    parser.add_argument('--max', type=int, help="Maximal value")

    args = parser.parse_args()

    if args.min and args.max:
        print(random.randint(args.min, args.max))
    elif args.min:
        print(random.randint(args.min,10000))
    elif args.max:
        print(random.randint(0, args.max))
    else:
        print(random.randint(0,10000))

if __name__ == "__main__":
    main()