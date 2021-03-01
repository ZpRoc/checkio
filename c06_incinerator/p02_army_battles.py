# ---------------------------------------------------------------- #

# Army Battles
#   This mission will be unlocked after solving The Warriors mission
#   (Games, oop, series)

# ---------------------------------------------------------------- #

# In the previous mission - Warriors - you've learned how to make a duel 
# between 2 warriors happen. Great job! But let's move to something that 
# feels a little more epic - the armies! In this mission your task is to 
# add new classes and functions to the existing ones. The new class should 
# be the Army and have the method add_units() - for adding the chosen amount 
# of units to the army. The first unit added will be the first to go to 
# fight, the second will be the second, ...
# Also you need to create a Battle() class with a fight() function, which 
# will determine the strongest army.

# The battles occur according to the following principles:
#   - at first, there is a duel between the first warrior of the first army 
#     and the first warrior of the second army. As soon as one of them 
#     dies - the next warrior from the army that lost the fighter enters the duel, 
#     and the surviving warrior continues to fight with his current health. This 
#     continues until all the soldiers of one of the armies die. In this case, the 
#     fight() function should return True , if the first army won, or False , if 
#     the second one was stronger.
#   - Note that army 1 have the advantage to start every fight!

# Input: The warriors and armies.
# Output: The result of the battle (True or False).
# Precondition:
#           2 types of units
#           For all battles, each army is obviously not empty at the beginning.


# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #
# ---------------------------------------------------------------- #

class Warrior:
    health = 50
    attack = 5

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    move = 1
    while unit_1.is_alive and unit_2.is_alive:
        if move == 1:
            unit_2.health -= unit_1.attack
            move = 2
        elif move == 2:
            unit_1.health -= unit_2.attack
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

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    #battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)
    
    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

