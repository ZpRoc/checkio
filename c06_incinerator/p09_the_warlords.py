# ---------------------------------------------------------------- #

# The Warlords
#   This mission will be unlocked after solving The Weapons mission
#   (Games, oop, series)

# ---------------------------------------------------------------- #

# In this mission you should add a new class Warlord(), which should 
# be the subclass of the Warrior class and have the next characteristics:
#   health = 100
#   attack = 4
#   defense = 2

# Also, when the Warlord is included in any of the armies, that particular 
# army gets the new move_units() method which allows to rearrange the units 
# of that army for the better battle result. The rearrangement is done not 
# only before the battle, but during the battle too, each time the allied 
# units die. The rules for the rearrangement are as follow:
# - If there are Lancers in the army, they should be placed in front of 
#   everyone else.
# - If there is a Healer in the army, he should be placed right after the 
#   first soldier to heal him during the fight. If the number of Healers 
#   is > 1, all of them should be placed right behind the first Healer.
# - If there are no more Lancers in the army, but there are other soldiers 
#   who can deal damage, they also should be placed in first position, and 
#   the Healer should stay in the 2nd row (if army still has Healers).
# - Warlord should always stay way in the back to look over the battle 
#   and rearrange the soldiers when it's needed.
# - Every army can have no more than 1 Warlord.
# - If the army doesn't have a Warlord, it can’t use the move_units() method.

# Input: The warriors, armies and weapons.
# Output: The result of the battle (True or False).
# Precondition: 6 types of units, 2 types of battles


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

# --------------------------- Weapons ---------------------------- #

class Weapon:
    health     = 0
    attack     = 0
    defense    = 0
    vampirism  = 0
    heal_power = 0

    def __init__(self, health, attack, defense, vampirism, heal_power):
        self.health     = health
        self.attack     = attack
        self.defense    = defense
        self.vampirism  = vampirism
        self.heal_power = heal_power
      

### health +5, attack +2
class Sword(Weapon):
    health     = 5
    attack     = 2
    defense    = 0
    vampirism  = 0
    heal_power = 0

    def __init__(self):
        pass

### health +20, attack -1, defense +2
class Shield(Weapon):
    health     = 20
    attack     = -1
    defense    = 2
    vampirism  = 0
    heal_power = 0

    def __init__(self):
        pass

### health -15, attack +5, defense -2, vampirism +10%
class GreatAxe(Weapon):
    health     = -15
    attack     = 5
    defense    = -2
    vampirism  = 10
    heal_power = 0

    def __init__(self):
        pass

### health -20, attack +6, defense -5, vampirism +50%
class Katana(Weapon):
    health     = -20
    attack     = 6
    defense    = -5
    vampirism  = 50
    heal_power = 0

    def __init__(self):
        pass

### health +30, attack +3, heal_power +3
class MagicWand(Weapon):
    health     = 30
    attack     = 3
    defense    = 0
    vampirism  = 0
    heal_power = 3

    def __init__(self):
        pass


# --------------------------- Soilders --------------------------- #

class Warrior:
    health     = 50
    attack     = 5
    defense    = 0
    vampirism  = 0
    heal_power = 0
    d_hit      = False

    @property
    def is_alive(self):
        return self.health > 0

    def equip_weapon(self, weapon):
        self.health     = max(self.health + weapon.health, 0)
        self.attack     = max(self.attack + weapon.attack, 0)
        self.defense    = max(self.defense + weapon.defense, 0)
        self.vampirism  = max(int(self.vampirism * (1 + 0.01 * weapon.vampirism)), 0)
        self.heal_power = max(self.heal_power + weapon.heal_power, 0)


class Knight(Warrior):
    attack = 7


class Defender(Warrior):
    health  = 60
    attack  = 3
    defense = 2


class Vampire(Warrior):
    health    = 40
    attack    = 4
    vampirism = 50


class Lancer(Warrior):
    health = 50
    attack = 6
    d_hit  = True


class Healer(Warrior):
    health     = 60
    attack     = 0
    heal_power = 2

    def heal(self, type):
        unit_0 = type.__class__()
        type.health = min(type.health + self.heal_power, unit_0.health)


class Army:
    def __init__(self):
        self.units = []

    def add_units(self, type, num):
        self.units.extend([type() for _ in range(num)])


# ---------------------------- Battle ---------------------------- #

class Battle:
    ### fight
    def fight(self, army1, army2):
        move = 1
        while army1.units and army2.units:
            # Cannot judge
            if army1.units[0].attack - army2.units[0].defense <= 0 and army2.units[0].attack - army1.units[0].defense <= 0:
                return False

            # Fight
            if move == 1:
                # Attacker, defender, Vampire
                army2.units[0].health -= max((army1.units[0].attack - army2.units[0].defense), 0)
                army1.units[0].health += max((army1.units[0].attack - army2.units[0].defense) * army1.units[0].vampirism * 0.01, 0)

                # Lancer
                if army1.units[0].d_hit and len(army2.units) > 1:
                    army2.units[1].health -= max((army1.units[0].attack - army2.units[1].defense) * 0.5, 0)
                    if not army2.units[1].is_alive:
                        army2.units.pop(1)

                # Healer
                if len(army1.units) > 1 and army1.units[1].__class__ == Healer:
                    army1.units[1].heal(army1.units[0])

                # Judge?
                if army2.units[0].is_alive:
                    move = 2
                else:
                    army2.units.pop(0)
            elif move == 2:
                # Attacker, defender, Vampire
                army1.units[0].health -= max((army2.units[0].attack - army1.units[0].defense), 0)
                army2.units[0].health += max((army2.units[0].attack - army1.units[0].defense) * army2.units[0].vampirism * 0.01, 0)

                # Lancer
                if army2.units[0].d_hit and len(army1.units) > 1:
                    army1.units[1].health -= max((army2.units[0].attack - army1.units[1].defense) * 0.5, 0)
                    if not army1.units[1].is_alive:
                        army1.units.pop(1)

                # Healer
                if len(army2.units) > 1 and army2.units[1].__class__ == Healer:
                    army2.units[1].heal(army2.units[0])

                # Judge?
                if army1.units[0].is_alive:
                    move = 1
                else:
                    army1.units.pop(0)
                    move = 1        # 这里好不合理，每次都是左边的先进攻
        return bool(army1.units)


    ### straight_fight
    def straight_fight(self, army1, army2):
        while army1.units and army2.units:
            # Fight
            res = [True] * len(army1.units) if len(army1.units) > len(army2.units) else [False] * len(army2.units)
            for i in range(min(len(army1.units), len(army2.units))):
                res[i] = fight(army1.units[i], army2.units[i])

            # Remove
            army1.units = [army1.units[i] for i, x in enumerate(res) if x]
            army2.units = [army2.units[i] for i, x in enumerate(res) if not x]
        return bool(army1.units)


def fight(unit_1, unit_2):
    army1 = Army()
    army1.units = [unit_1]

    army2 = Army()
    army2.units = [unit_2]

    battle = Battle()
    return battle.fight(army1, army2)


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    ronald = Warlord()
    heimdall = Knight()

    assert fight(heimdall, ronald) == False

    my_army = Army()
    my_army.add_units(Warlord, 1)
    my_army.add_units(Warrior, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 2)

    enemy_army = Army()
    enemy_army.add_units(Warlord, 3)
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 2)
    enemy_army.add_units(Knight, 2)

    my_army.move_units()
    enemy_army.move_units()

    assert type(my_army.units[0]) == Lancer
    assert type(my_army.units[1]) == Healer
    assert type(my_army.units[-1]) == Warlord

    assert type(enemy_army.units[0]) == Vampire
    assert type(enemy_army.units[-1]) == Warlord
    assert type(enemy_army.units[-2]) == Knight

    #6, not 8, because only 1 Warlord per army could be
    assert len(enemy_army.units) == 6

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    print("Coding complete? Let's try tests!")

