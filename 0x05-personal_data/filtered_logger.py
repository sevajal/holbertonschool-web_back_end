#!/usr/bin/env python3
""" Filtered logger"""
from typing import List
import re


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    '''function that returns the log message obfuscated'''
    for string in fields:
        message = re.sub("(?<={:s}=)(.*?)(?={:s})".format(string, separator),
                         redaction, message)
    return message
