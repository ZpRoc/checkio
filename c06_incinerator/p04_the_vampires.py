# ---------------------------------------------------------------- #

# The Vampires
#   This mission will be unlocked after solving The Defenders mission
#   (Games, oop, series)

# ---------------------------------------------------------------- #

# So we have 3 types of units: the Warrior, Knight and Defender. Let's 
# make the battles even more epic and add another type - the Vampire!

# Vampire should be the subclass of the Warrior class and have the additional 
# vampirism parameter, which helps him to heal himself. When the Vampire hits 
# the other unit, he restores his health by +50% of the dealt damage (enemy 
# defense makes the dealt damage value lower).

# The basic parameters of the Vampire:
#       health = 40
#       attack = 4
#       vampirism = 50%

# You should store vampirism attribute as an integer (50 for 50%). It will 
# be needed to make this solution evolutes to fit one of the next challenges 
# of this saga.

# Input: The warriors and armies.
# Output: The result of the battle (True or False).
# Precondition: 4 types of units


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

class Warrior:
    health    = 50
    attack    = 5
    defense   = 0
    vampirism = 0

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


def fight(unit_1, unit_2):
    move = 1
    while unit_1.is_alive and unit_2.is_alive:
        if move == 1:
            unit_2.health -= max((unit_1.attack - unit_2.defense), 0)
            unit_1.health += max((unit_1.attack - unit_2.defense) * unit_1.vampirism, 0)
            move = 2
        elif move == 2:
            unit_1.health -= max((unit_2.attack - unit_1.defense), 0)
            unit_2.health += max((unit_2.attack - unit_1.defense) * unit_2.vampirism, 0)
            move = 1
    return unit_1.is_alive


class Army:
    def __init__(self):
        self.army = []

    def add_units(self, type, num):
        self.army.extend([type() for _ in range(num)])


class Battle:
    def fight(self, army1, army2):
        flg = 1
        while army1.army and army2.army:
            if flg == 1:
                res = fight(army1.army[0], army2.army[0])
                if res:
                    army2.army.pop(0)
                else:
                    army1.army.pop(0)
            elif flg == 2:
                res = fight(army2.army[0], army1.army[0])
                if res:
                    army1.army.pop(0)
                else:
                    army2.army.pop(0)
        return bool(army1.army)


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

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 4)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

