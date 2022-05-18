from argparse import ArgumentParser
import argparse

def num_add(args):
    return args.x+args.y


def get_args():

    parser = argparse.ArgumentParser(description="This is a sample arg parse",
    epilog="This is were you can write an example usage")

    parser.add_argument('-x',required=True,action="store",help='This argument is a Integer type', type=int)
    parser.add_argument('-y',required=True,default=30,type=int)

    print(parser.parse_args())

    return num_add(parser.parse_args())


print(get_args())