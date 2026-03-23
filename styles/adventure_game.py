# Author
#chinwe Blessing Muokwe.
# This program adventure program is based on my own original story idea about choosing between a Bible and Money
# Title "hidden blessings"
# For additional creativity, I added three levels,a three choice scenarios, and multiple endings to make the game more intresting and creative.
# I also shared the game ideas to few person and improved it to make the choices clearer.

print("Welcome to the Hidden Blessing Adventure Game!")
print("Your father gives you a choice: BIBLE or MONEY or WALK-AWAY.")
# LEVEL 1
choice1 = input ("Which do you choose? (BIBLE or MONEY or WALK-AWAY): ")
choice1 = choice1.lower()

if choice1 == "bible":
    print("You choose the Bible.")
    print("Inside the Bible, you find a LETTER and some CASH: ")
    # LEVEL 2 
    choice2 = input("Which do you chose? (LETTER, CASH or SHARE): ")
    choice2 = choice2.lower()
    if choice2 == "cash":
        print("You spend it and it finishes. ")

    elif choice2 == "letter":
        print("choose the letter.")
        print("The letter contains hidden directions to hidden blessings")
    # Level 3
        choice3 = input("Do you FOLLOW or IGNORE or PRAY? (FOLLOW, IGNORE, PRAY):")
        choice3 = choice3.lower()
        if choice3 == "follow":
            print("You followed the directions.")
            print("It leads you to a hidden mansion prepared for you.")

        elif choice3 == "ignore":
            print("You ignored the letter.")
            print("You missed the hidden blessings.")

        elif choice3 == "pray":
            print("You chose to pray.")
            print("You receive wisdom")
        else:
            print("Invalid choice! please FOLLOW or IGNORE or PRAY")

    elif choice2== "share":
     print("You choose to share what you found with others.")
     print("Your kindness leads to greater and unexpected blessings.")

    else:
     print("Invalid choice! please choose LETTER, CASH or SHARE")
        

elif choice1 == "money":
    print("You choose money.")
    print("You spend and enjoy it for a short time.")

elif choice1 == "walk-away":
   print("You decide to walk away.")
   print("Later, you realize that you may have missed a life-changing blessing")

else:
    print("Invalid choice! please chose BIBLE or MONEY.")

        

