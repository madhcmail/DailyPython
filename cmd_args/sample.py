import argparse
#parser = argparse.ArgumentParser(description='A simple program usage',
#epilog='This is where you pass the arguments')

#parser.print_help()



def get_args():
    """"""
    parser = argparse.ArgumentParser(
        description="A simple argument parser",
        epilog="This is where you might put example usage"
    )
    return parser.parse_args()

if __name__ == '__main__':
    get_args()