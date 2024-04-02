'''
CREDITS + SPECIAL THANKS

100 Days of Coding Bootcamp
Instructor : Angela Yu  

'''

import random

# Elements 

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("\nHey Kid! Wanna play Rock Paper Scissors? Let's Settle this once in for all !!\n\npress 0 for rock ,1 for Scissors and 2 for Papern\n\n")

elements = [rock, paper, scissors]

comp_choice = random.choice(elements)

flag = True

while(flag):
    user_choice = int(input("Go ahead Kid!: "))

    # declaring the functions
    def Result():
        if (user_choice ==0 and comp_choice == rock) or (user_choice ==1 and comp_choice == paper) or (user_choice ==2 and comp_choice == scissors):
            print("That's a draw\n")
        elif (user_choice ==0 and comp_choice == paper):
            print("Try again next time Little Prick! Haha...\n")
        elif (user_choice ==1 and comp_choice == scissors):
            print("Try again next time Little Prick! Haha...\n")
        elif (user_choice ==2 and comp_choice == rock):
            print("Try again next time, Little Prick! Haha...\n")
        else:
            if user_choice != 0 and user_choice != 1 and user_choice != 2:
                print("Punk! Gonna Play it right? or.....\n")
            else:
                print("You Got luckey My Boy...\n")
    def Elements_to_print():
        if user_choice == 0:
            print(rock)
        elif user_choice == 1:
            print(paper)
        elif user_choice == 2:
            print(scissors)
        else:
            print("\n__No Choice__\n")

    # Printing User Choice and Computer Choice 
    print("Your Choice: ")
    Elements_to_print()

    print("Computer's Choice: ")
    print(comp_choice)

    #Printing the Outcome
    Result()

    wanna_continue = input("GO for another round? [y/n]: ")
    if wanna_continue == 'n':
        flag = False
