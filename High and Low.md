#High Low Game
import random
"""
1.  Two numbers are generated from 1 to 100 
    (inclusive on both ends): one for you and one for a 
    computer, who will be your opponent. You get to see 
    your number, but not the computer's!
2.  You make a guess, saying your number is either higher
    than or lower than the computer's number.
3.  If your guess matches the truth 
    (ex. you guess your number is higher, and then 
    your number is actually higher than the computer's), 
    you get a point!
"""
#Constants
NUM_ROUNDS = 5

#Functions
def main():
    print('--------------------------------')
    start = input("Would you like to play a game of high or low? Yes or No: ")
    POINTS = 0
    while start == "yes" or start == "Yes" or start == "YES":
        print("Welcome to the High-Low Game!")
        comp_num, user_num = random_numbers()
        guess = input("Make a guess, High or Low? ")
        score = check_guess(guess, comp_num, user_num)
        POINTS = POINTS + score
        print(f'Your Points are {POINTS}.')
        start = input("Would you like to play a game of high or low? Yes or No: ")
    print(f"Thanks for playing, your total points were {POINTS}")

def check_guess(guess, comp_num, user_num):
    if (guess == "High" or guess == "high") and user_num>comp_num:
        SCORE = 1
        print(f"You were right! The computer's number was {comp_num}")
    elif (guess == "Low" or guess == "low") and user_num<comp_num:
        SCORE = 1
        print(f"You were right! The computer's number was {comp_num}")
    else:
        print(f"Aww, that's incorrect. The computer's number was {comp_num}")
        SCORE = 0
    return SCORE

def random_numbers():
    #generating random numbers
    comp_num = random.randint(1, 100)
    user_num = random.randint(1, 100)
    #You get to see your number, but not the computer's!
    print(f'Your number is {user_num}.')
    return comp_num, user_num

if __name__ == "__main__":
    main()