import random

def user_choice():
    user=0
    while user not in range(1, 4):
        user=int(input("Enter your choice: 1 for Rock, 2 for Paper, and 3 for Scissors: "))
    return user

def computer_choice():
    return random.randint(1,3)

def winner(user,comp):
    if user==comp:
        return "1"
    elif user==1 and comp==3 or user==2 and comp==1 or user==3 and comp==2:
        return "2"
    else:
        return "3"

def display_choices(user, comp):
    game = {1: "Rock", 2: "Paper", 3: "Scissors"}
    print("Your choice: %s" % game[user])
    print("Computer's choice: %s" % game[comp])

def play_game():
    play=True
    while play:
        user=user_choice()
        comp=computer_choice()
        display_choices(user,comp)
        result=winner(user, comp)
        if result=="1":
            print("It's a draw!!!")
        elif result=="2":
            print("You win!!!")
        else:
            print("You lose!!!")
        temp=input("Want to play again? (y/n): ").lower()
        if temp == "n":
            play = False
            print("Thanks for playing...")

if __name__ == "__main__":
    play_game()
