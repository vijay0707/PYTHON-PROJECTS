# DICE ROLL STIMULATOR

#import Random module

import random

#range of values

min_val = 1
max_val = 6

# for looping through user input

roll_again = "yes"

#looping 

while (roll_again == "yes" or roll_again == "y"):
    print("rolling the dice....")
    print("the value is:")
  
#generating and printing 1st random integer from 1 to 6
   
    print(random.randint(min_val,max_val)) 

#generating and printing 2st random integer from 1 to 6

    print(random.randint(min_val,max_val))

 #asking user to roll the dice again. Any input other than yes or y will terminate the loop

    roll_again= input("Roll the dice again??")