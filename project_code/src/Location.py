import random

class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def describe(self):
        print(f"You are at {self.name}. {self.description}")

    def explore(self):
        if not self.events:
            print("You don't find anything of interest.")
            return

        event = random.choice(self.events)
        print("As you explore, you encounter something:")
        event()

# Example Usage:

def monster_encounter():
    monsters = ["Paint Glob", "Inker", "Sponge Grunge", "Painters Mock"]
    monster = random.choice(monsters)
    print(f"A {monster} appears!")

def treasure_discovery():
    treasures = ["Eraser", "Magic Pencil", "Watercolor Potion", "Gemstone"]
    treasure = random.choice(treasures)
    print(f"You discover {treasure}!")

# Creating a location
cave = Location("Dark Cave", "A dark clay cave with jagged clay spikes.")

# Adding events to the location
cave.add_event(monster_encounter)
cave.add_event(treasure_discovery)

# Exploring the location
cave.describe()
cave.explore()
