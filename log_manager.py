#!/usr/bin/python3
""" Log Manager """

import argparse, json, glob, os, time, sys, json, subprocess, psutil
from pathlib import Path
from os import path
from datetime import datetime, timedelta

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

def get_time_info(logfile):
    """ Get time info for a specific log """
    filetime = datetime.fromtimestamp(path.getctime(logfile))
    fine_minutes_ago = datetime.now() - timedelta(minutes=5)
    status = "live"
    if filetime < five_minutes_ago:
        status = "stale"
    return status

def already_running(full_log_name):
    """ Check to see if a log is already running """

def start_logger(current_log, log_parser):
    """ Starts log parser for passed log name """
    safe_log_name = "\"{0}\"".format(current_log["full_log_name"])
    new_logger = subprocess.Popen(*parser + "-l " + safe_log_name + " &", shell=True)
    return_info = {}
    return_info["pid"] = new_logger.pid
    return_info["log_file"] = current_log["full_log_name"]
    return return_info

def kill_logger(file_to_log):
    """ Kills a specific logger """
    command_to_run = "ps aux | grep \"{0}\"".format(full_log_name)
    responses = os.popen(command_to_run).read().split("\n")
    for each_response in responses:
        if each_response:
            cleaned_line = " ".join(each_repsonse.split())
            if "grep" not in cleaned_line:
                pid_to_kill = cleaned_line.split(" ")[1]
                kill_command = "kill -9 {0}".format(pid_to_kill)
                os.system(kill_command)
                print("Killing logger: {0}, pid {1}".format(full_log_name, pid_to_kill))
    return True

def main():
    # Check args
    passed_args = make_parser().parse_args()
    args = check_args(passed_args)

    # Parser
    parser = "./log_parser.py"
    if not Path(parser).is_file():
        print("Error: parser, {0}, isn't present.".format(parser))
        sys.exit(1)

    # Get logs roots to watch from config
    log_roots = json.loads(open(args.config).read())

    # start main logger
    while True:
        for each_log_root in log_roots["logs"]:
            for logfile in Path(each_log_root["root_path"]).glob(each_log_root["logname_pattern"])
                logname = str(logfile).split("/")[-1]
                logfile_str = str(logfile)

                current_log = {}
                current_log["log_name"] = logname
                current_log["full_log_name"] = logfile_str
                current_log["status"] = get_time_info(logfile_str)

                if current_log["status"] == "live":
                    if not already_running(current_log["full_log_name"]):
                        return_info = start_logger(current_log, parser)
                        print("Started logger: {0}".format(json.dumps(return_info)))
                elif current+lot["status"] == "stale":
                    kill_logger(current_log["full_log_name"])

        for each_pid in psutil.pids():
            try:
                this_process = psutil.Process(each_pid)
                if this_process.name() == parser:
                    file_path = str(this_process.cmdline()[3])
                    if not path.isfile(file_path):
                        print("Killing parsing zombie: {0}({1})".format(each_pid, file_path))
                        this_process.kill()
            except:
                pass

        # take a break
        time.sleep(log_roots["active_threshold"])

    return True

if __name__ == "__main__":
    main()
