class Event:
    pass
import random

class Dungeon:
    def __init__(self):
        self.monsters = ["Paint Glob", "Inker", "Sponge Grunge", "Painters Mock"]
        self.traps = ["Charcoal Dust", "Art Bag Claw", "Oil", "Art Block"]
        self.treasures = ["Eraser", "Magic Pencil", "Watercolor Potion", "Gemstone"]
        self.npcs = ["Orange Mantis", "Pink Vender", "Blue Soul", "Green Gardener"]
        self.hazards = ["Folding Paper", "Crumbling Clay", "Melting Paint", "Paint in your eye"]

    def event_encounter_monsters(self):
        monster = random.choice(self.monsters)
        print(f"You encounter {monster}s!")

    def event_trap_activation(self):
        trap = random.choice(self.traps)
        print(f"A {trap} is triggered!")

    def event_discovery_treasure(self):
        treasure = random.choice(self.treasures)
        print(f"You discover {treasure}!")

    def event_npc_interaction(self):
        npc = random.choice(self.npcs)
        print(f"You meet {npc}!")

    def event_environmental_hazard(self):
        hazard = random.choice(self.hazards)
        print(f"You face a {hazard}!")

# Create a dungeon instance
dungeon = Dungeon()

# Run five random events
events = [
    dungeon.event_encounter_monsters,
    dungeon.event_trap_activation,
    dungeon.event_discovery_treasure,
    dungeon.event_npc_interaction,
    dungeon.event_environmental_hazard
]

for _ in range(5):
    random_event = random.choice(events)
    random_event()
