import random

def coin_toss():
    return random.choice(["human", "computer"])

def human_turn():
    skill = int(input("Choose your skill (1-3): "))
    if skill < 1 or skill > 3:
        print("Invalid skill choice. Please choose between 1 and 3.")
        return human_turn()
    return skill

def computer_turn():
    return random.randint(1, 3)


def calculate_damage(skill):
    if skill == 1:
        return random.randint(1, 15)
    elif skill == 2:
        return random.randint(16, 25)
    elif skill == 3:
        return random.randint(26, 50)


def main():
    human_hp = 100
    computer_hp = 100

    turn = coin_toss()
    print(turn.capitalize(), "goes first.")

    while human_hp > 0 and computer_hp > 0:
        if turn == "human":
            print("Your turn.")
            human_skill = human_turn()
            computer_skill = computer_turn()
            human_damage = calculate_damage(human_skill)
            print("You chose skill", human_skill, "and caused", human_damage, "damage to the computer.")
            computer_hp -= human_damage
            if computer_hp < 75:
                heal_amount = random.randint(15, 30)
                computer_hp = min(100, computer_hp + heal_amount)
                print("Computer healed for", heal_amount, "HP.")
            print("Computer's HP:", computer_hp)
            print()
            turn = "computer"
        else:
            print("Computer's turn.")
            computer_skill = computer_turn()
            human_skill = random.randint(1, 3)
            computer_damage = calculate_damage(computer_skill)
            print("The computer chose skill", computer_skill, "and caused", computer_damage, "damage to you.")
            human_hp -= computer_damage
            if human_hp < 75:
                heal_amount = random.randint(15, 30)
                human_hp = min(100, human_hp + heal_amount)
                print("You healed for", heal_amount, "HP.")
            print("Your HP:", human_hp)
            print()
            turn = "human"

    if human_hp <= 0:
        print("Game over! You lost.")
    else:
        print("Congratulations! You defeated the computer!")

if __name__ == "__main__":
    main()
