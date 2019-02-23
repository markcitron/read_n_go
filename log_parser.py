#!/usr/bin/python3
""" Log Parser - started by the log manager for each log to follow """

import tailer

def main():
    # Handle arguments
    passed_args = make_parser().parse_args()
    args = check_args(passed_args)
    
    return True

if __name__ == "__main__":
    main()