from rpg import Character, Chest, Druid, Hunter, Warrior, DeathKnight

retnuh = Hunter(name="Retnuh", race="Dwarf", health=120, attack=70)
skaleaf = Druid(name="Skaleaf", race="Elf", health=200, attack=50, gold=50, items=['Idol'])
wraelas = Warrior(name="Wraelas", race="Human", health=100, attack=80)
arthus = DeathKnight(name="Arthus", race="Human", health=500, attack=50)

chest = Chest(items=['longsword', 'iron helm'], gold=25, locked=True)

arthus.battle(skaleaf)
print(skaleaf.__dict__)

skaleaf.battle(arthus)
print(arthus.__dict__)

# print(chest.get_inventory())
# print(skaleaf.get_inventory())

# chest.transfer(skaleaf)

# print(chest.get_inventory())
# print(skaleaf.get_inventory())



