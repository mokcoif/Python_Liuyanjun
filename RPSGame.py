from random import randint

#available weapons => store this in an array
choices = ["Rock", "Paper", "Scissors"]
player = False

#make the computer pick one item at random
computer_choice = choices[randint(0, 2)]

#show the computer's choices in the terminal window
print("computer chooses: ", computer_choice)

while player == False:
    player = input("Rock, Paper or Scissors?\n")
    print("player choose:", player)

    #check to see if you picked the same thing
    if (player == computer):
        print("Tie!Live to shoot another day")

    elif player == "Rock":
        if computer == "Paper":
            #computer won
            print("You lose", computer, "covers", player)
        else:
            print("You win!", computer, "smashes", computer)

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computer, "cuts", player)
        else:
            print("You win!", computer, "covers", computer)

    elif player == "Scissors":
        if computer == "Rock":
            #computer won
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", computer, "cuts", computer)

        else:
            print("Not a valid option. Check again, and check your spelling!\n")

        player = False
        computer = choices[randiant(0.2)]