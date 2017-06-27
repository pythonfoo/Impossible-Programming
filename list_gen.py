#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 18:22:15 2017

@author: gabrielkuell
"""

def lines_from_file(filename):
    """
    executes file.readlines() and creates a list with the lines of the file as its elements.
    filename: exact name of the file.
    returns lines
    """
    file = open(filename, encoding='utf-8')
    lines = file.readlines()
    file.close()
    
    return lines

def choose_at_random():
    pass
