import random

def play_game():
    lucky_num = random.randint(1, 50)

    while True:
        user_num = int(input("Guess a number: "))
        if user_num == lucky_num:
            print("You win!")
            break
        elif user_num > lucky_num:
            print("Greater than lucky!")
        elif user_num < lucky_num:
            print("Less than Lucky!")

    print("Thank you for playing!")

play_game()