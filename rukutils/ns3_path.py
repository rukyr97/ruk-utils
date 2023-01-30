# -*- coding: utf-8 -*-
'''
A snippet module that looks for the ns3 path in the file system. 
Useful when we want to launch simulations with a script in a different folder.
'''
import sys
import os
import logging
import coloredlogs

coloredlogs.install(fmt='%(asctime)s - %(filename)s:'
                    '%(funcName)s:%(lineno)s | '
                    '%(levelname)s | %(message)s')

def find(cwd):
    '''
    Finds the ns3 path and returns it.
    '''
    logging.debug("Starting working directory: %s", cwd)
    found = False
    curr_dir=cwd
    ns3_path=cwd
    while not found:
        for fname in os.listdir(curr_dir):
            if fname == "ns3":
                found = True
                ns3_path = os.path.join(curr_dir, fname)

            if fname == "ns-3-dev":
                found = True
                ns3_path = os.path.join(curr_dir, fname, "ns3")

        curr_dir= os.path.dirname(curr_dir)

        if str(curr_dir) == "/": #root
            logging.error("ns3 file not found. Exiting...")
            sys.exit()
    return ns3_path 