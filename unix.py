#!/usr/bin/python3

import time
import logging
import datetime
import subprocess
import os


NA = ["vim", "man", "top", "htop", "cat", "nano", "vi"]
ROOT = ["sudo" , "su"]
PATH = os.path.dirname(os.path.realpath(__file__))

now = datetime.datetime.now()
logging.basicConfig(filename=("log/" + str(now.year) + str(now.month) + str(now.day) + ".log"),
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)



def terminal(text):
    command = text.split(" ")
    if command[0] in NA:
        return "'" + command[0] + "' is not supported!\n{}$ _".format(PATH)
    elif command[0] in ROOT:
        return "root access is not allowed!\n{}$ _".format(PATH)
    return console(command)

def console(command):
    try:
        if command[0] == "cd":
            os.chdir(command[1])
            PATH = os.getcwd()
            return PATH + "$ _"
        else:
            output = subprocess.run(command, stdout=subprocess.PIPE)
            return output.stdout.decode("utf-8")
    except Exception as e:
        print(e)
        return str(e)


    def man(command):
        return "`Send a shell command to run on LINUX Terminal emulator.`"
