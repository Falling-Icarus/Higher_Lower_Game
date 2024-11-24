import random
import art
from candidates import data

game = True


score = 0
print(art.logo)

primary_choice = random.choice(data)
second_choice = random.choice(data)

while game == True:

    while primary_choice == second_choice:
        second_choice = random.choice(data)


    if score >= 1 and choice == "A".upper():
        second_choice = random.choice(data)
    elif score >= 1 and choice == "B".upper():
        primary_choice = second_choice
        second_choice = random.choice(data)

    print(primary_choice['name'], primary_choice['description'], primary_choice['country'])
    print(art.vs)

    print(second_choice['name'], second_choice['description'], second_choice['country'])
    choice = input(f"Who has more followers? Type A or B: ").upper()

    if choice == "A".upper() and primary_choice['follower_count'] > second_choice['follower_count']:
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}")

    elif choice == "B".upper() and primary_choice['follower_count'] < second_choice['follower_count']:
        score += 1
        print(art.logo)
        print(f"You're right! Current score: {score}")

    else:
        print(art.logo)
        print(f"Sorry, that's wrong. Final Score: {score}")
        game = False