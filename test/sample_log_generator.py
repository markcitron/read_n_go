#!/usr/bin/python3
""" Sample log generator
    
    This script will generate one or more sample log sources which
    will log into ./sample_logs.  These can be used to test or configure
    the read_n_go log_manager and parsers.
    """

import logging, argparse

def make_parser():
    """ Create a parser to parse arguments """
    p = argparse.ArgumentParser(description="")
    p.add_argument("--number_of_parsers", "-n", help="")
    p.add_argument("--log_to_dir", "-l", help="")
    return p

def check_args(args):
    """ eval and check arguments """
    if not args.number_of_parsers:
        args.number_of_parsers = 1
    if not args.log_to_dir:
        args.log_to_dir = "./sample_logs"
    return args

def main():
    """ Main function """
    # parse args
    passed_args = make_parser().parse_args()
    args = check_args(passed_args)

    # main loop
    for x in range (0, args.number_of_parsers):
        print(str(x))

if __name__ == "__main__":
    main()
