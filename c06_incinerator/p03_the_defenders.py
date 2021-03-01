# ---------------------------------------------------------------- #

# The Defenders
#   This mission will be unlocked after solving Army Battles mission
#   (Games, oop, series)

# ---------------------------------------------------------------- #

# In the previous mission - Army battles, you've learned how to make a 
# battle between 2 armies. But we have only 2 types of units - the Warriors 
# and Knights. Let's add another one - the Defender. It should be the 
# subclass of the Warrior class and have an additional defense parameter, 
# which helps him to survive longer. When another unit hits the defender, 
# he loses a certain amount of his health according to the next formula: 
# enemy attack - self defense (if enemy attack > self defense). Otherwise, 
# the defender doesn't lose his health.

# The basic parameters of the Defender:
#       health  = 60
#       attack  = 3
#       defense = 2

# Input: The warriors and armies.
# Output: The result of the battle (True or False).
# Precondition: 3 types of units

# class Rookie(Warrior):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.health = 50
#         self.attack = 1


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

class Warrior:
    health  = 50
    attack  = 5
    defense = 0

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    attack = 7


class Defender(Warrior):
    health  = 60
    attack  = 3
    defense = 2


def fight(unit_1, unit_2):
    move = 1
    while unit_1.is_alive and unit_2.is_alive:
        if move == 1:
            unit_2.health -= max((unit_1.attack - unit_2.defense), 0)
            move = 2
        elif move == 2:
            unit_1.health -= max((unit_2.attack - unit_1.defense), 0)
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

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Defender, 1)

    army_4 = Army()
    army_4.add_units(Warrior, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    print("Coding complete? Let's try tests!")

