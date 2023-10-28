#This file contains the core logic for the memory game

from user_interface import getUserNumberConversionFromDecimal

import random

#Generates a random number between 0 and 255 which is the limit of hex and binary.
rand_Number = random.randint(0,255)

user_Lives = 3

def decimal_to_hex_binary(value):

    #This function generates the numerical representations of the random number.

    hex_value = hex(rand_Number).upper()
    binary_value = bin(rand_Number)[2:]

    print("The Hex Value is: " + hex_value, ". The Binary Value is: " + binary_value + ". The decimal value is: " + str(value))

    return hex_value, binary_value


def logicCorrectAnswer():

    #This function checks with the decimal_to_hex_binary function to see if the users input is correct. Next I need to see if the lives are decrementing correctly if wrong answers are input.

    global rand_Number

    user_Hex, user_Bin = getUserNumberConversionFromDecimal(rand_Number)

    correct_Hex, correct_Bin = decimal_to_hex_binary(rand_Number)

    if user_Hex.upper() == correct_Hex and user_Bin == correct_Bin:
        #Print function is for testing
        print("correct!")
        return True
    else:
        #Print for testing
        print("Incorrect!")
        return False
        


def decrementLives():

    #If the player answers correctly, nothing happens to their lives. If they answer incorrectly, they lose a life.
    global user_Lives
    if not logicCorrectAnswer():
        user_Lives -= 1


def noLives():

    #If all lives are lost game is over.

    return user_Lives == 0

def memoryGameOver():


    return noLives()


if __name__== "__main__":

    #Testing decimal_to_hex_binary function

    decimal_to_hex_binary(rand_Number)

    print('\n')
    print('\n')
    print('\n')

    #Testing logicCorrectAnswer function
    logicCorrectAnswer()