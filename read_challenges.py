#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 11:52:07 2017

@author: gabrielkuell
"""
import random
import list_gen

projekt = list_gen.lines_from_file("Projektauswahl.txt")
sprache = list_gen.lines_from_file("Programmiersprachen.txt")
einschränkung = list_gen.lines_from_file("constraints.txt")

print("Schreibe",  random.choice(projekt) + "in", random.choice(sprache) + random.choice(einschränkung))
