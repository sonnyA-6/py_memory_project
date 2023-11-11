greeting = """Hello, and welcome, this is a memory game designed to test knowledge of conversions! In this game, you will choose one of the following options: Binary, Decimal, or Hexadecimal. The 
option you choose will be the number you receive and must do the conversion for! For example, if you choose decimal and are prompted with the number 1 your answers would include the binary and hexadecimal versions.
"""
global user_Hex, user_Bin

def printGreeting():
    #This function prints the greeting. Works as intended.

    print(greeting, "\n")

def confirmPlay():
    
    #This function gathers the input from the user and returns a boolean for the core logic.

    value = input("If you are ready to play please type: Y or y. If not, type: N or n. : ")
    print("\n")

    if value == "Y" or value == "y":
        #print("User has indicated play.") Delete this later. Only here to confirm the choice was taken.
        return True
    else:
        return False

def promptNumberValue():

    numberWordComparison = ['hex','dec','bin']

    numberChoice = input("Choose which type of number to convert from: ")
    #Loop through the array and if the input is equal to any of the strings return it to be used in core logic.

    for i in numberWordComparison: 
        if numberChoice.lower()[:3] == i:
            return i
        
def outputTypeChosenByUser(value):
    print(value)
        
def getUserNumberConversion(conversion_type):
    if conversion_type.lower() == 'dec':
        numbers = input("Enter the hex and binary values (separated by a space): ")
        user_Hex, user_Bin = numbers.split()
        return user_Hex, user_Bin
    elif conversion_type.lower() == 'hex':
        numbers = input("Enter the decimal and binary values (separated by a space): ")
        user_Dec, user_Bin = numbers.split()
        return user_Dec, user_Bin
    elif conversion_type.lower() == 'bin':
        numbers = input("Enter the hex and decimal values (separated by a space): ")
        user_Hex, user_Dec = numbers.split()
        return user_Hex, user_Dec
    else:
        # Handle invalid conversion type
        print("Invalid conversion type. Please choose DEC, HEX, or BIN.")

def playAgain(value):

    #This function prompts the user for confirmation to play again after they have lost all lives.

    if value == "Y" or value == "y":
        return True     #This will launch another game
    else: 
        return False    #This will end the game
    

def verbalWrongAnswer():

    #This function will print that the user was wrong in their choice.

    wrong = "Your answer was incorrect, please try again."
    print(wrong)

def verbalCorrectAnswer():

    #This function print that the user was correct in their choice.

    correct = "You answer was correct! Keep going!"
    print(correct)

#--------------------------------------------------------------------------------------

#Move the testing functions to a testing file.

def test_promptNumberValue():
    assert promptNumberValue('hex') == 'hex'
    assert promptNumberValue('Decimal') == 'Decimal'
    assert promptNumberValue('Binary') == 'Binary'
    
    # Test cases where the input doesn't match any string in numberWordComparison
    assert promptNumberValue('Oct') is None
    assert promptNumberValue('random') is None

def test_confirmPlay(input_value):
    result = confirmPlay(input_value)
    print("Result:", result)


if __name__== "__main__":

    #ALL FUNCTIONS WORK AS INTENDED


    #Testing greeting function

    printGreeting()

    print('\n')
    print('\n')

    #Testing confirm play
    #Test with different input values
    test_confirmPlay("Y")  # Should print True
    test_confirmPlay("y")  # Should print True
    test_confirmPlay("N")  # Should print False
    test_confirmPlay("n")  # Should print False

    print('\n')
    print('\n')
    print('\n')

    #Test promptNumberValue
    test_promptNumberValue()


    print('\n')
    print('\n')
    print('\n')

    #Testing play again

    result5 = playAgain("Y")
    result6 = playAgain("y")
    result7 = playAgain("N")
    result8 = playAgain("n")

    print("Result 5:", result5)  # Should print True
    print("Result 6:", result6)  # Should print True
    print("Result 7:", result7)  # Should print False
    print("Result 8:", result8)  # Should print False

    #Testing Wrong and Correct Answer
    wrongAnswer()
    print('\n')
    correctAnswer()