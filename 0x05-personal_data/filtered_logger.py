#!/usr/bin/env python3
""" Filtered logger"""
from typing import List
import logging
import re

PII_FIELDS = ('name', 'phone', 'ssn', 'password', 'email')


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''function that returns the log message obfuscated'''
    for string in fields:
        message = re.sub("(?<={:s}=)(.*?)(?={:s})".format(string, separator),
                         redaction, message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Init Redacting Formatter"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ Formats the class object"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    '''Returns a logger object'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    ch = logging.StreamHandler()
    logger.setFormatter(RedactingFormatter(PII_FIELDS))
    return logger
