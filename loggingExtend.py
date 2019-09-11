#-*-coding:utf-8-*-
"""
This is to get loggrr
"""
import os
import logging
import time

class Logger(object):
    """
    This is get log class
    """
    def __init__(self, path, name, Flevel=logging.DEBUG):
        self.time = time.gmtime
        self.fileName = path + name + ".log"
        self.logger = logging.getLogger(self.fileName)
        self.logger.setLevel(Flevel) 
        fmt = logging.Formatter('%(asctime)s | %(threadName)s | %(levelname)s | %(message)s')
        fh = logging.FileHandler(self.fileName)
        fh.setFormatter(fmt)
        fh.setLevel(Flevel)
        self.logger.addHandler(fh)
    
    def debug(self, message):
        """
        This is debug
        """
        self.logger.debug(message)

    def info(self, *message):
        """
        This is info
        """
        msg = ' | '.join([message[0],message[1],message[2],message[3]])
        self.logger.info(msg)
    
    def warn(self, message):
        """
        This is warn
        """
        self.logger.warn(message)

    def error(self, *message):
        """
        This is error
        """
        msg = ' | '.join([message[0],message[1],message[2],message[3]])
        self.logger.error(msg)

    def critical(self, message):
        """
        This is critical
        """
        self.logger.critical(message)
