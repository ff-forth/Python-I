"""Jag tog 8 timmar"""
import os
import random
os.system('clear')

def generate_code():
    """Funktionen generera en random lista"""
    code = []
    item = 0
    while item != 4:
        num = random.randint(0,5)
        item += 1
        code.append(num)
    return code

def right_position(guess,code):
    """Funktionen checkar gissningar
    parameter: lista, lista
    returvärde: antal rätt positioner i gisningen"""
    result = 0
    index = -1
    while index < 3:
        index += 1
        if guess[index] == code[index]:
            result += 1
    return result

def wrong_position(guess,code):
    """Funktionen checkar gissningar
    parameter: lista, lista
    returvärde: antal fel positioner i gisningen"""
    code_ = code[:]
    guess_ =  guess[:]
    result = 0
    index = -1
    while index < 3:
        index += 1
        if guess_[index] == code_[index]:
            guess_[index] = -1
            code_[index] = -1
    index = -1
    for item in code_:
        index += 1
        if item in guess_:
            if code_[index] != guess_[index]:
                index_ = guess_.index(code_[index])
                result += 1
                guess_[index_] = -1
    return result
