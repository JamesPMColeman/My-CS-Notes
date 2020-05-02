import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--input',
                    action='store',
                    type= int,
                    required=True)
parser.add_argument('--id',
                    action='store',
                    type=int)

args = parser.parse_args()

print(args.input)

