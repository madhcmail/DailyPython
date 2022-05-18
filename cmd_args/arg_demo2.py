# passing command line arguments to program 


import argparse

def string_concat(args):

    print(args.arg1+ ' '+ args.arg2+str(args.arg3))

def get_args():
    """
        Input: arg_demo2.py -arg1 'hello'
        output: hello world10
    """
    parser = argparse.ArgumentParser(description='A Simple argument parser',
    epilog="This is where you might put example usage")
    # required argument
    parser.add_argument('-arg1','--argument', action="store", required=True, help='Give any string for arg1')
    #optional argument
    parser.add_argument('-arg2', help='second string', default='world')
    # impose datatype
    parser.add_argument('-arg3',default=10, type=int)

    string_concat(parser.parse_args())

if __name__ == '__main__':
    get_args()