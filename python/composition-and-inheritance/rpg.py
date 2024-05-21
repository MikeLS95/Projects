class Inventory:
    def __init__(self, gold=0, items=[]):
        self.gold = gold
        self.items = items

    def transfer(self, to_inv):
        # Move all items/gold from one inventory to another
        # 1. Add self.gold to to_inv.gold
        to_inv.gold += self.gold
        # 2. Set self.gold to 0
        self.gold = 0
        # 3. Add self.items to to_inv.items
        to_inv.items += self.items
        # 4. Set self.items to []
        self.items = []


class Character:
    def __init__(self, name: str, race: str, health: int, attack: int, gold=0, items=[]):
        """
        Represents a player character or NPC.

        Args:
            name str: 
                The name of a character.
            race str: 
                The race of a character.
            health int: 
                The health of a character.
            attack int: 
                The base attack strength of a character.  If this drops below 1, your character dies.
            gold int: 
                Initial gold for this character.
            items list, optional: 
                Initial items for this character.
        """
        self.name = name
        '''The name of a character.'''
        self.race = race
        '''The race of a character.'''
        self.health = health
        '''The health of a character.'''
        self.attack = attack
        '''The base attack strength of a character.'''
        self.inv = Inventory(gold, items) # Composition

    def get_inventory(self):
        return self.inv.__dict__
    
    def battle(self, other: 'Character'):
        """
        Perform combat between this character and another character.

        Args:
            other (Character): The character that this character will fight.
        """
        print(f'{self.name} attacks {other.name} for {self.attack} damage!')

class Druid(Character):
    def __init__(self, name: str, race: str, health: int, attack: int, gold=0, items=[]):
        super().__init__(name, race, health, attack, gold, items)
        self.rage = 100

    def transform(self):
        pass

    def battle(self, other: 'Character'):
        """
        Perform combat between this character and another character.

        This method overrides the one defined in the superclass.

        Args:
            other Character: The character that this character will fight.
        """
        print(f'{self.name} users his claws to hit {other.name} for {self.attack} damage with Maul!')
        self.rage -= 20

class Hunter(Character):
    def battle(self, other):
        print(f'{self.name} loads his crossbow to shoot {other.name} for {self.attack} piercing damage!')

class Warrior(Character):
    def battle(self, other):
        print(f'{self.name} charges up to {other.name} and hits them for {self.attack} damage with heroic strike!')

class DeathKnight(Character):
    def battle(self, other):
        print(f'{self.name} harnesses the might of the scourge to hit {other.name} for {self.attack} unholy damage with Deathstrike!')

class Chest:
    """
    Represents a lootable chest of items and/or gold.
    """
    def __init__(self, items=[], gold=0, locked=False):
        self.inv = Inventory(gold, items) # Composition
        self.locked = locked

    def get_inventory(self):
        return self.inv.__dict__
    
    def transfer(self, receiver):
        self.inv.transfer(receiver.inv) # Delegation