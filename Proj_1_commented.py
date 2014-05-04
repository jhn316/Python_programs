# Rock-paper-scissors-lizard-Spock 


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

# converts name to number using if/elif/else and returns result
def name_to_number(name):
    if  name == "rock":
        number = 0
        return number
    elif name == "Spock":
        number = 1
        return number
    elif name == "paper":
        number = 2
        return number
    elif name == "lizard":
        number = 3
        return number
    elif name == "scissors":
        number = 4
        return number
    else:
        print "not a valid input"    
    
# converts number to name using if/elif/else and returns result
def number_to_name(number):
    if  number == 0:
        name = "rock"
        return name
    elif number == 1:
        name = "Spock"
        return name
    elif number == 2:
        name = "paper"
        return name
    elif number == 3:
        name = "lizard"
        return name
    elif number == 4:
        name = "scissors"
        return name
    else:
        print "not a valid input"  
    


def rpsls(player_choice):
    import random
    # print a blank line to separate consecutive games
    print ""
    # print out the message for the player's choice
    print "Player chooses",player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    print "Computer chooses",comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (player_number - comp_number)%5
    p = "Player wins!"
    c = "Computer wins!"
    # use if/elif/else to determine winner, print winner message
    if difference == 0:
        print "It's a tie!"
    elif difference == 1:
        print p
    elif difference == 2:
        print p
    elif difference == 3:
        print c
    elif difference == 4:
        print c
        
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


