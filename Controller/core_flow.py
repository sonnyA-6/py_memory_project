# This file contains the core flow of the memorization project.


#Adjust import statements as needed. May not need to import everything. Want to keep to MVC standards.
from py_memory_project.View.user_interface import *
from py_memory_project.Model.game_logic import *

gameON = True

def main():

    global gameON 
    
    while gameON:       #while true
        printGreeting()     #Welcome the player
        playChoice = confirmPlay() #Grab the players choice

        if playChoice == True:
            choice = promptNumberValue()     #If they choose to play then continue
            convChoice = numberForUser(choice)
            outputTypeChosenByUser(convChoice) #Outputs the type of choice by the user

            """ Need to do the comparison checking to ensure the number given to
            the user will match the conversion number that the user will give.
            """

            userAns1, user_Ans2 = getUserNumberConversion(choice)
            if logicCorrectAnswer(userAns1, user_Ans2) == False:
                decrementLives()
                if noLives() == True:
                    memoryGameOver()
                    gameON = playAgain()

        else:                       #Otherwise, end the game.
            memoryGameOver()
            print("user chose not to play")
            gameON = False


if __name__=="__main__":

    main()
    