#!/usr/bin/env python

# Author: Hezekiah Watson
# Last Edit: March 8, 2025

# A program that checks whether your game character has picked up all the items needed
# to perform certain tasks and checks against any status debuffs. Confirm checks with print
# statements.



# Define the Character class
class Character:
    # Constructor to initialize nickname, weapons, and weaknesses
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    # Getter methods 
    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

# Create a character (player1) and set their properties
player1 = Character('', [], [])  # Empty lists at creation
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

# Display player1's inventory and weaknesses
print(f"{player1.nickname}'s Inventory and Status:")
for item in player1.weapons:
    print("Item:", item)
for debuff in player1.weaknesses:
    print("Debuff:", debuff)

# Function to check if player1 can perform certain tasks
def check_tasks(character):
    # Task requirements
    tasks = {
        "Climb a mountain": {
            "required_items": {'rope', 'coat', 'first aid kit'},
            "forbidden_debuffs": {'slow'}
        },
        "Cook a meal": {
            "required_items": {'pan', 'groceries'},
            "forbidden_debuffs": {'small'}
        },
        "Write a book": {
            "required_items": {'pen', 'paper', 'idea'},
            "forbidden_debuffs": {'confusion'}
        }
    }

    # Convert player’s inventory and weaknesses to sets for easy comparison
    player_items = set(character.weapons)
    player_debuffs = set(character.weaknesses)

    # Check each task's requirements
    for task, requirements in tasks.items():
        required_items = requirements["required_items"]
        forbidden_debuffs = requirements["forbidden_debuffs"]

        print(f"\nChecking requirements for: {task}")
        if required_items.issubset(player_items) and not forbidden_debuffs.intersection(player_debuffs):
            print(f" {character.nickname} can complete '{task}'!")
        else:
            print(f" {character.nickname} cannot complete '{task}'.")
            missing_items = required_items - player_items
            if missing_items:
                print(f"  Missing items: {', '.join(missing_items)}")
            forbidden_present = forbidden_debuffs.intersection(player_debuffs)
            if forbidden_present:
                print(f"  Forbidden debuff(s) present: {', '.join(forbidden_present)}")

# Run the check_tasks function for player1
check_tasks(player1)

