#!/usr/bin/python3
""" Sample log generator
    
    This script will generate one or more sample log sources which
    will log into ./sample_logs.  These can be used to test or configure
    the read_n_go log_manager and parsers.
    """

import logging, argparse, time

def make_parser():
    """ Create a parser to parse arguments """
    p = argparse.ArgumentParser(description="")
    p.add_argument("--logname", "-l", help="")
    return p

def check_args(args):
    """ eval and check arguments """
    if not args.logname:
        args.logname= "./jaberwocky.log"
    return args

def log_text(pointer):
    """ sample text to log -- love this poem """
    lt = [ 
        "’Twas brillig, and the slithy toves ", 
        "    Did gyre and gimble in the wabe: ", 
        "All mimsy were the borogoves, ", 
        "    And the mome raths outgrabe. ", 
        "", 
        "“Beware the Jabberwock, my son! " ,
        "    The jaws that bite, the claws that catch! " ,
        "Beware the Jubjub bird, and shun " ,
        "    The frumious Bandersnatch!” " ,
        "" 
        "He took his vorpal sword in hand; " ,
        "    Long time the manxome foe he sought— " ,
        "So rested he by the Tumtum tree " ,
        "    And stood awhile in thought. " ,
        "", 
        "And, as in uffish thought he stood, " ,
        "    The Jabberwock, with eyes of flame, " ,
        "Came whiffling through the tulgey wood, " ,
        "    And burbled as it came! " ,
        "", 
        "One, two! One, two! And through and through " ,
        "    The vorpal blade went snicker-snack! " ,
        "He left it dead, and with its head " ,
        "    He went galumphing back. " ,
        "", 
        "“And hast thou slain the Jabberwock? ",
        "    Come to my arms, my beamish boy! ", 
        "O frabjous day! Callooh! Callay!” ",
        "    He chortled in his joy. ",
        "", 
        "’Twas brillig, and the slithy toves ", 
        "    Did gyre and gimble in the wabe: ",
        "All mimsy were the borogoves, ",
        "    And the mome raths outgrabe."
    ] 
    return lt[pointer]

def main():
    """ Main function """
    # parse args
    passed_args = make_parser().parse_args()
    args = check_args(passed_args)

    # start logging
    logname = args.logname
    logging.basicConfig(filename=logname, level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s')
    logging.info("Started sample log: {0}".format(args.logname))

    lc = 0
    while True:
        try:
            next_line = log_text(lc)
            logging.info(next_line)
            lc = lc + 1
        except Exception as e:
            logging.error("expected: {0}".format(str(e)))
            lc = 0
        time.sleep(1)


if __name__ == "__main__":
    main()