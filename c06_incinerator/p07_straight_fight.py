# ---------------------------------------------------------------- #

# Straight Fight
#   This mission will be unlocked after solving The Healers mission
#   (Games, oop, series)

# ---------------------------------------------------------------- #

# A new unit type won't be added in this mission, but instead we'll 
# add a new tactic - straight_fight(army_1, army_2). It should be the 
# method of the Battle class and it should work as follows:
# at the beginning there will be a few duels between each pair of soldiers 
# from both armies (the first unit against the first, the second against 
# the second and so on). After that all dead soldiers will be removed and 
# the process repeats until all soldiers of one of the armies will be dead. 
# Armies might not have the same number of soldiers. If a warrior doesn't 
# have an opponent from the enemy army - we’ll automatically assume that 
# he's won a duel (for example - 9th and 10th units from the first army, 
# if the second has only 8 soldiers).

# Input: The warriors and armies.
# Output: The result of the battle (True or False).
# Precondition: 5 types of units, 2 types of battles


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

class Warrior:
    health    = 50
    attack    = 5
    defense   = 0
    vampirism = 0
    d_hit     = False

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    attack = 7


class Defender(Warrior):
    health  = 60
    attack  = 3
    defense = 2


class Vampire(Warrior):
    health    = 40
    attack    = 4
    vampirism = 0.5


class Lancer(Warrior):
    health = 50
    attack = 6
    d_hit  = True


class Healer(Warrior):
    health   = 60
    attack   = 0

    def heal(self, type):
        unit_0 = type.__class__()
        type.health = min(type.health + 2, unit_0.health)


class Army:
    def __init__(self):
        self.army = []

    def add_units(self, type, num):
        self.army.extend([type() for _ in range(num)])


class Battle:
    ### fight
    def fight(self, army1, army2):
        move = 1
        while army1.army and army2.army:
            if move == 1:
                # Attacker, defender, Vampire
                army2.army[0].health -= max((army1.army[0].attack - army2.army[0].defense), 0)
                army1.army[0].health += max((army1.army[0].attack - army2.army[0].defense) * army1.army[0].vampirism, 0)

                # Lancer
                if army1.army[0].d_hit and len(army2.army) > 1:
                    army2.army[1].health -= max((army1.army[0].attack - army2.army[1].defense) * 0.5, 0)
                    if not army2.army[1].is_alive:
                        army2.army.pop(1)

                # Healer
                if len(army1.army) > 1 and army1.army[1].__class__ == Healer:
                    army1.army[1].heal(army1.army[0])

                # Judge?
                if army2.army[0].is_alive:
                    move = 2
                else:
                    army2.army.pop(0)
            elif move == 2:
                # Attacker, defender, Vampire
                army1.army[0].health -= max((army2.army[0].attack - army1.army[0].defense), 0)
                army2.army[0].health += max((army2.army[0].attack - army1.army[0].defense) * army2.army[0].vampirism, 0)

                # Lancer
                if army2.army[0].d_hit and len(army1.army) > 1:
                    army1.army[1].health -= max((army2.army[0].attack - army1.army[1].defense) * 0.5, 0)
                    if not army1.army[1].is_alive:
                        army1.army.pop(1)

                # Healer
                if len(army2.army) > 1 and army2.army[1].__class__ == Healer:
                    army2.army[1].heal(army2.army[0])

                # Judge?
                if army1.army[0].is_alive:
                    move = 1
                else:
                    army1.army.pop(0)
                    move = 1        # 这里好不合理，每次都是左边的先进攻
        return bool(army1.army)

    ### straight_fight
    def straight_fight(self, army1, army2):
        while army1.army and army2.army:
            # Fight
            res = [True] * len(army1.army) if len(army1.army) > len(army2.army) else [False] * len(army2.army)
            for i in range(min(len(army1.army), len(army2.army))):
                res[i] = fight(army1.army[i], army2.army[i])

            # Remove
            army1.army = [army1.army[i] for i, x in enumerate(res) if x]
            army2.army = [army2.army[i] for i, x in enumerate(res) if not x]
        return bool(army1.army)


def fight(unit_1, unit_2):
    army1 = Army()
    army1.army = [unit_1]

    army2 = Army()
    army2.army = [unit_2]

    battle = Battle()
    return battle.fight(army1, army2)


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    
    #fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()
    bob = Defender()
    mike = Knight()
    rog = Warrior()
    lancelot = Defender()
    eric = Vampire()
    adam = Vampire()
    richard = Defender()
    ogre = Warrior()
    freelancer = Lancer()
    vampire = Vampire()
    priest = Healer()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True
    assert fight(freelancer, vampire) == True
    assert freelancer.is_alive == True
    assert freelancer.health == 14    
    priest.heal(freelancer)
    assert freelancer.health == 16

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 2)
    my_army.add_units(Healer, 1)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 4)
    enemy_army.add_units(Healer, 1)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)
    enemy_army.add_units(Healer, 1)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Healer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Healer, 1)
    army_4.add_units(Lancer, 2)

    army_5 = Army()
    army_5.add_units(Warrior, 10)

    army_6 = Army()
    army_6.add_units(Warrior, 6)
    army_6.add_units(Lancer, 5)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    assert battle.straight_fight(army_5, army_6) == False
    print("Coding complete? Let's try tests!")

