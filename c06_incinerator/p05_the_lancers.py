# ---------------------------------------------------------------- #

# The Lancers
#   This mission will be unlocked after solving The Vampires mission
#   (Games, oop, series)

# ---------------------------------------------------------------- #

# It seems that the Warrior, Knight, Defender and Vampire are not enough 
# to win the battle. Let's add one more powerful unit type - the Lancer.
# Lancer should be the subclass of the Warrior class and should attack 
# in a specific way - when he hits the other unit, he also deals a 50% 
# of the deal damage to the enemy unit, standing behind the firstly assaulted 
# one (enemy defense makes the deal damage value lower - consider this).

# The basic parameters of the Lancer:
#       health = 50
#       attack = 6

# Input: The warriors and armies.
# Output: The result of the battle (True or False).
# Precondition: 5 types of units


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


class Army:
    def __init__(self):
        self.army = []

    def add_units(self, type, num):
        self.army.extend([type() for _ in range(num)])


class Battle:
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

                # Judge?
                if army1.army[0].is_alive:
                    move = 1
                else:
                    army1.army.pop(0)
                    move = 1        # 这里好不合理，每次都是左边的先进攻
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

    #battle tests
    my_army = Army()
    my_army.add_units(Defender, 2)
    my_army.add_units(Vampire, 2)
    my_army.add_units(Lancer, 4)
    my_army.add_units(Warrior, 1)
    
    enemy_army = Army()
    enemy_army.add_units(Warrior, 2)
    enemy_army.add_units(Lancer, 2)
    enemy_army.add_units(Defender, 2)
    enemy_army.add_units(Vampire, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 1)
    army_3.add_units(Lancer, 1)
    army_3.add_units(Defender, 2)

    army_4 = Army()
    army_4.add_units(Vampire, 3)
    army_4.add_units(Warrior, 1)
    army_4.add_units(Lancer, 2)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")

    ### Test
    army_1 = Army()
    army_2 = Army()
    army_1.add_units(Defender, 11)
    army_1.add_units(Vampire, 3)
    army_1.add_units(Warrior, 4)
    army_2.add_units(Warrior, 4)
    army_2.add_units(Defender, 4)
    army_2.add_units(Vampire, 13)

    battle = Battle()
    
    assert battle.fight(army_1, army_2) == True

