# This file contains the core flow of the memorization project.


#Adjust import statements as needed. May not need to import everything. Want to keep to MVC standards.
from user_interface import *
from game_logic import *

gameON = True



def main():

    global gameON
    
    while gameON:
        printGreeting()
        playChoice = confirmPlay()

        if playChoice == True:
            promptNumberValue()
        else:
            memoryGameOver()
            print("user chose not to play")
            gameON = False














if __name__=="__main__":

    main()
    