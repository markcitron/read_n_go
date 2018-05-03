#!/usr/bin/python3
""" Log Manager """

import argparse, json
import os.path

def make_parser():
    """ Parser for parsing arguments """
    p = argparse.ArgumentParser(description="")
    p.add_argument("--config", "-c", help="")
    return p

def check_args(args):
    """ Check / validate arguments """
    # config file
    if not args.config:
        args.config = "./log_watch_config.json"
    if not os.path.isfile(args.config):
        print("Error: {0} is not a valid configuration file".format(args.config))
    return args

def main():
    # Check args
    passed_args = make_parser().parse_args()
    args = check_args(passed_args)

    # Get logs roots to watch from config
    log_roots = json.loads(open(args.config).read())
    print(json.dumps(log_roots))

    # start main logger

    return True

if __name__ == "__main__":
    main()
