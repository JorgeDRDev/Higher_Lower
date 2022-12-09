from gamedata import data
from art import logo_high_lo
from art import vs
# import clear
import random


def format_data(account):
    """Takes account information from dictionary data, separates it in variables, so it can return the information
    as a string"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def user_is_correct(guess, followers_a, followers_b):
    if followers_a > followers_b and guess == 'a':
        return True
    elif followers_a < followers_b and guess == 'b':
        return True
    else:
        return False


account_a = random.choice(data)
account_b = random.choice(data)

score = 0
compare = True
while compare:
    account_a = account_b
    if account_a == account_b:
        account_b = random.choice(data)
    print(logo_high_lo)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    followers_a = account_a['follower_count']
    followers_b = account_b['follower_count']
    if user_is_correct(guess, followers_a, followers_b):
        score += 1
        print(f"You're right! Current score: {score}.")
        # clear()
    else:
        compare = False
        print(f"Sorry, that's wrong. Final score: {score}")
