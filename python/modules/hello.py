import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-n', '--name', type=str, required=True)
parser.add_argument('-a', '--age', type=str)

args = parser.parse_args()

print(f'Hello {args.name}!' + (f' You are {args.age} years old!' if args.age else ''))
