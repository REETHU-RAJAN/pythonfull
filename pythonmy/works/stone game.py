""" stone papper scissor game"""
import random
user_action=input("enter a choice(rock,paper,scissor):")
posi_action=["rock","paper","scissor"]
bot_action=random.choice(posi_action)
print(f" your choice{user_action},bot choice{bot_action}")
def game(user_action):
    if user_action==bot_action:
        print(f"both are{user_action}.it's a tie! ")
    elif user_action=="rock":
        if bot_action=="scissor":
            print(f"rock smashes scissor! you win!")
        else:
            print(f"paper cover rock! you lose.")
    elif user_action=="paper":
        if bot_action=="rock":
            print(f"paper cover rock! you win!")
        else:
            print(f"scissor cut paper! you lose.")
    elif user_action=="scissor":
        if bot_action=="paper":
            print(f"scissor cut paper! you win!")
        else:
            print(f"rock smashes scissor! you lose.")
game(user_action)