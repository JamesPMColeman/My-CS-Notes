# Import argparser library
import argparse
import sys
import os

# Create parser
my_parser = argparse.ArgumentParser(prog='myCommandLineCode',
                                    usage='%(prog)s [options] path',
                                    description= 'List the content of a folder',
                                    epilog='This is the end, my only friend, the end')

# Add arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Call parse_args()
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    print(args)
    sys.exit()

print('\n'.join(os.listdir(input_path)))
