# ---------------------------------------------------------------- #

# The Weapons
#   This mission will be unlocked after solving Straight Fight mission
#   (Games, oop, series)

# ---------------------------------------------------------------- #

# In this mission you should create a new class Weapon(health, attack, defense, 
# vampirism, heal_power) which will equip your soldiers with weapons. 
# Every weapon's object will have the parameters that will show how the soldier's 
# characteristics change while he uses this weapon. Assume that if the soldier 
# doesn't have some of the characteristics (for example, defense or vampirism), 
# but the weapon have those, these parameters don't need to be added to the soldier.

# The parameters list:
#   health - add to the current health and the maximum health of the soldier this modificator;
#   attack - add to the soldier's attack this modificator;
#   defense - add to the soldier's defense this modificator;
#   vampirism - increase the soldier’s vampirism to this number (in %. So vampirism = 20 means +20%);
#   heal_power - increase the amount of health which the healer restore for the allied unit.

# All parameters could be positive or negative, so when a negative modificator is 
# being added to the soldier’s stats, they are decreasing, but none of them can 
# be less than 0.

# Let’s look at this example: vampire (basic parameters: health = 40, attack = 4, 
# vampirism = 50%) equip the Weapon(20, 5, 2, -60, -1). The vampire has the health 
# and the attack, so they will change - health will grow up to 60 (40 + 20), attack 
# will be 9 (4 + 5). The vampire doesn’t have defense or the heal_power, so these 
# weapon modificators will be ignored. The weapon's vampirism modificator -60% will 
# work as well. The standard vampirism value is only 50%, so we’ll get -10%. But, 
# as we said before, the parameters can’t be less than 0, so the vampirism after 
# all manipulations will be just 0%.

# Also you should create a few standard weapons classes, which should be the subclasses 
# of the Weapon. Here's their list:
#   Sword - health +5, attack +2
#   Shield - health +20, attack -1, defense +2
#   GreatAxe - health -15, attack +5, defense -2, vampirism +10%
#   Katana - health -20, attack +6, defense -5, vampirism +50%
#   MagicWand - health +30, attack +3, heal_power +3

# And finally, you should add an equip_weapon(weapon_name) method to all of the 
# soldiers classes. It should equip the chosen soldier with the chosen weapon.
# This method also should work for the units in the army. You should hold them 
# in the list and use it like this:
#   my_army.units[0].equip_weapon(Sword()) - equip the first soldier with the sword.

# Notes:
# - While healing (both vampirism and health restored by the healer), the health 
#   can't be greater than the maximum amount of health for this unit (with 
#   consideration of all of the weapon's modificators).
# - If the heal from vampirism is float (for example 3.6, 1.1, 2.945), round it 
#   down in any case. So 3.6 = 3, 1.1 = 1, 2.945 = 2.
# - Every soldier can be equipped with any number of weapons and get all their 
#   bonuses, but if he wears too much weapons with the negative health modificator 
#   and his health is lower or equal 0 - he is as good as dead, which is actually 
#   pretty dead in this case.

# Input: The warriors, armies and weapons.
# Output: The result of the battle (True or False).
# Precondition: 5 types of units, 2 types of battles


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
    
    ogre = Warrior()
    lancelot = Knight()
    richard = Defender()
    eric = Vampire()
    freelancer = Lancer()
    priest = Healer()

    sword = Sword()
    shield = Shield()
    axe = GreatAxe()
    katana = Katana()
    wand = MagicWand()
    super_weapon = Weapon(50, 10, 5, 150, 8)

    ogre.equip_weapon(sword)
    ogre.equip_weapon(shield)
    ogre.equip_weapon(super_weapon)
    lancelot.equip_weapon(super_weapon)
    richard.equip_weapon(shield)
    eric.equip_weapon(super_weapon)
    freelancer.equip_weapon(axe)
    freelancer.equip_weapon(katana)
    priest.equip_weapon(wand)
    priest.equip_weapon(shield)

    ogre.health == 125
    lancelot.attack == 17
    richard.defense == 4
    eric.vampirism == 200
    freelancer.health == 15
    priest.heal_power == 5

    assert fight(ogre, eric) == False
    assert fight(priest, richard) == False
    assert fight(lancelot, freelancer) == True

    my_army = Army()
    my_army.add_units(Knight, 1)
    my_army.add_units(Lancer, 1)

    enemy_army = Army()
    enemy_army.add_units(Vampire, 1)
    enemy_army.add_units(Healer, 1)

    my_army.units[0].equip_weapon(axe)
    my_army.units[1].equip_weapon(super_weapon)

    enemy_army.units[0].equip_weapon(katana)
    enemy_army.units[1].equip_weapon(wand)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    print("Coding complete? Let's try tests!")

    ### Test
    unit_1 = Defender()
    unit_2 = Vampire()
    weapon_1 = Shield()
    weapon_2 = MagicWand()
    weapon_3 = Shield()
    weapon_4 = Katana()
    unit_1.equip_weapon(weapon_1)
    unit_1.equip_weapon(weapon_2)
    unit_2.equip_weapon(weapon_3)
    unit_2.equip_weapon(weapon_4)
    assert fight(unit_1, unit_2) == False

