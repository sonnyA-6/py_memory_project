#This file contains the core logic for the memory game

from py_memory_project.View.user_interface import getUserNumberConversion

import random

#Generates a random number between 0 and 255 which is the limit of hex and binary.
rand_Number = random.randint(0,255)

user_Lives = 3


def numberForUser(value):

    global rand_Number
    user_choices = ['hex', 'dec', 'bin']        #list of choices

    hexChoice = hex(rand_Number)
    decChoice = rand_Number
    binChoice = bin(rand_Number)

    for choice in user_choices:      #Iterate through those choices looking for the match in the first letter
        if value[:3].lower()==choice:
            if choice[0] == 'h':
                return str(hexChoice)
            elif choice[0] == 'd':
                return str(decChoice) 
            elif choice[0] == 'b':
                return str(binChoice)
    print("No match was found please choose from hexadecimal, decimal, or binary.")


def decimal_to_hex_binary(value):

    #This function generates the numerical representations of the random number converting from dec -> hex & binary

    hex_value = hex(rand_Number).upper()
    binary_value = bin(rand_Number)[2:]

    print("The Hex Value is: " + hex_value, ". The Binary Value is: " + binary_value + ". The decimal value is: " + str(value))

    return hex_value, binary_value

def hex_to_dec_binary(value):

    #This function generates the numerical representations of the random number converting from hex -> dec & binary 

    dec_value = rand_Number
    binary_value = bin(rand_Number)[2:]

    print(" The Binary Value is: " + binary_value + ". The decimal value is: " + dec_value + ".")

    return dec_value, binary_value

def binary_to_hex_dec(value):

    #This function generates the numerical representations of the random number converting from binary -> hex & dec

    hex_value = hex(rand_Number).upper()
    dec_value = rand_Number

    print("The Hex Value is: " + hex_value + ". The decimal value is: " + dec_value)

    return hex_value, dec_value


def logicCorrectAnswer(value1, value2):

    #This function checks with the decimal_to_hex_binary function to see if the users input is correct. Next I need to see if the lives are decrementing correctly if wrong answers are input.

    global rand_Number

    correct_Hex, correct_Bin = decimal_to_hex_binary(rand_Number)

    if value1.upper() == correct_Hex and value2 == correct_Bin:
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
    #if not logicCorrectAnswer():
    user_Lives -= 1


def noLives():

    #If all lives are lost game is over.

    return user_Lives == 0

def memoryGameOver():


    return noLives()


def restartGame():

    #If the user is out of lives, restore the lives to 3.
    global user_Lives

    if user_Lives == 0:
        user_Lives = 3


def test_numberForUser():

    rand_Number = 10
    # Test case 1: Hexadecimal conversion
    assert numberForUser('hex') == hex(rand_Number)
    
    # Test case 2: Decimal conversion
    assert numberForUser('dec') == str(rand_Number)
    
    # Test case 3: Binary conversion
    assert numberForUser('bin') == bin(rand_Number)
    
    # Test case 4: Case-insensitive input
    assert numberForUser('HEX') == hex(rand_Number)
    
    # Test case 5: Invalid input
    assert numberForUser('oct') == "No match was found. Please choose from 'hex', 'dec', or 'bin'."
    
    # Add more test cases as needed





if __name__== "__main__":

    #Testing decimal_to_hex_binary function

    #decimal_to_hex_binary(rand_Number)

    print('\n')
    print('\n')
    print('\n')

    #Testing logicCorrectAnswer function
    #logicCorrectAnswer()


    # Run the test cases
    test_numberForUser()