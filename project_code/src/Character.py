from project_code.src.Statistic import *


import random

class Character:
    def __init__(self, name: str = None):
        self.name = self._generate_name() if name is None else name
        self.strength = random.randint(1, 10)
        self.dexterity = random.randint(1, 10)
        self.constitution = random.randint(1, 10)
        self.vitality = random.randint(1, 10)
        self.endurance = random.randint(1, 10)
        self.intelligence = random.randint(1, 10)
        self.wisdom = random.randint(1, 10)
        self.knowledge = random.randint(1, 10)
        self.willpower = random.randint(1, 10)
        self.spirit = random.randint(1, 10)

    def _generate_name(self):
        return "Red"

# Generate 10 characters
characters = [Character(f"Character{i+1}") for i in range(10)]

# Print the details of each character
for idx, character in enumerate(characters, 1):
    print(f"Character {idx}:")
    print(f"Name: {character.name}")
    print(f"Strength: {character.strength}")
    print(f"Dexterity: {character.dexterity}")
    print(f"Constitution: {character.constitution}")
    print(f"Vitality: {character.vitality}")
    print(f"Endurance: {character.endurance}")
    print(f"Intelligence: {character.intelligence}")
    print(f"Wisdom: {character.wisdom}")
    print(f"Knowledge: {character.knowledge}")
    print(f"Willpower: {character.willpower}")
    print(f"Spirit: {character.spirit}")
    print()
