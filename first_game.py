import random
import time
import sys

answer = input("Would you like to play? (Yes/No): ").lower().strip()
jobs = ["knight", "mage", "hunter", "druid"]
world_actions = ["reflect", "move", "item"]
combat_actions = ["attack", "item", "run"]
grid = [["0-0", "1-0", "2-0", "3-0", "4-0", "5-0", "6-0", "7-0", "8-0", "9-0"],
        ["0-1", "1-1", "2-1", "3-1", "4-1", "5-1", "6-1", "7-1", "8-1", "9-1"],
        ["0-2", "1-2", "2-2", "3-2", "4-2", "5-2", "6-2", "7-2", "8-2", "9-2"],
        ["0-3", "1-3", "2-3", "3-3", "4-3", "5-3", "6-3", "7-3", "8-3", "9-3"],
        ["0-4", "1-4", "2-4", "3-4", "4-4", "5-4", "6-4", "7-4", "8-4", "9-4"],
        ["0-5", "1-5", "2-5", "3-5", "4-5", "5-5", "6-5", "7-5", "8-5", "9-5"],
        ["0-6", "1-6", "2-6", "3-6", "4-6", "5-6", "6-6", "7-6", "8-6", "9-6"],
        ["0-7", "1-7", "2-7", "3-7", "4-7", "5-7", "6-7", "7-7", "8-7", "9-7"],
        ["0-8", "1-8", "2-8", "3-8", "4-8", "5-8", "6-8", "7-8", "8-8", "9-8"],
        ["0-9", "1-9", "2-9", "3-9", "4-9", "5-9", "6-9", "7-9", "8-9", "9-9"]]




def type_print(text, delay=0.03):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(delay)
    print()

class Player:
    def __init__(self, name, job, hp, max_hp, mp, max_mp, atk, defs, lvl, exp, need_exp, attacks, items, x = 4, y = 4, grid = grid):
        self.name = name
        self.job = job
        self.hp = hp
        self.max_hp = max_hp
        self.mp = mp
        self.max_mp = max_mp
        self.atk = atk
        self.defs = defs
        self.lvl = lvl
        self.exp = exp
        self.need_exp = need_exp
        self.attacks = attacks
        self.items = items
        self.x = x
        self.y = y
        self.grid = grid
        self.update_location()
    def update_location(self):
        self.location = self.grid[self.y][self.x]
    def move(self, direction):
        direction = input("Which direction would you like to move? (N/S/E/W): ")
        if direction.lower() == "n":
            if self.y != 0:
                self.y -= 1
                type_print("You travel north.")
            else:
                type_print("You see an ocean stretching out over the horizon.\n You can't continue north\n")
        elif direction.lower() == "s":
            if self.y != 9:
                self.y += 1
                print("You travel south.")
            else:
                type_print("You look over a cliff at an expansive ravine. \n You cannot continue south\n")
        elif direction.lower() == "e":
            if self.x != 9:
                self.x += 1
                print("You travel east.")
            else:
                type_print("You face a desert stretching as far as you can see. \n You are not prepared for this kind of quest. \n")
        elif direction.lower() == "w":
            if self.x != 0:
                self.x -= 1
                type_print("You travel west.")
            else:
                type_print("You stand before mountains that reach well beyond the clouds above. \nYou decide not to go any further.\n")
        self.update_location()
        print(self.location)

    def lvl_up():
        if my_player.exp >= my_player.need_exp:
            hp_gain = random.randint(3, 7)
            my_player.hp += hp_gain
            my_player.max_hp += hp_gain
            mp_gain = random.randint(2, 5)
            my_player.mp += mp_gain
            my_player.max_mp += mp_gain
            my_player.lvl += 1
            atk_gain = round(random.uniform(0.1, 0.4), 2)
            my_player.atk += atk_gain
            defs_gain = round(random.uniform(0.01, 0.1), 2)
            my_player.defs += defs_gain
            my_player.exp -= my_player.need_exp
            my_player.need_exp = my_player.need_exp * 1.3
            my_player.mp += round(my_player.max_mp * .25)
            type_print(f"You've levelled up! \nYou are now level {my_player.lvl}!")
            type_print(f"HP +{hp_gain}")
            type_print(f"MP +{mp_gain}")
            type_print(f"Atk + {atk_gain}")
        if my_player.lvl  % 4 == 0:
            type_print("A ray of light comes down on your head.  You feel knowledge passed down from another world")
            attack_chosen = False
            while attack_chosen == False:
                for attack in all_attacks:
                    if attack not in my_player.attacks:
                        type_print(f"-{attack.name}")
                selected_skill = input("Enter skill you wish to attain: ")
                chosen_skill = None
                for attack in all_attacks:
                    if selected_skill.lower() == attack.name.lower():
                        chosen_skill = attack
                        break
                if chosen_skill:
                    my_player.attacks.append(chosen_skill)
                    type_print(f"You attain the skill {chosen_skill.name}! ")
                    attack_chosen = True
                else:
                    type_print("Invalid skill")

class Enemy:
    def __init__(self, name, hp, max_hp, attacks, exp):
        self.name = name
        self.hp = hp
        self.max_hp = max_hp
        self.attacks = attacks
        self.exp = exp

class Attack:
    def __init__(self, name, base_damage, mp_cost, def_mod, atk_mod, hp_cost):
        self.name = name
        self.base_damage = base_damage
        self.mp_cost = mp_cost
        self.def_mod = def_mod
        self.atk_mod = atk_mod
        self.hp_cost = hp_cost


class Job:
    def __init__(self, hp, mp, atk, defs, attacks):
        self.hp = hp
        self.mp = mp
        self. atk = atk
        self. defs = defs
        self.attacks = attacks

class Item:
    def __init__(self, name, hp_restore, mp_restore, atk_mod, def_mod, hp_mod, mp_mod):
        self.name = name
        self.hp_restore = hp_restore
        self.mp_restore = mp_restore
        self.atk_mod = atk_mod
        self.def_mod = def_mod
        self.hp_mod = hp_mod
        self.mp_mod = mp_mod

class GameState:
    def __init__(self):
        self.priest_event_triggered = False
        self.alter1_triggered = False
        self.alter2_triggered = False
        self.alter3_triggered = False
        self.alter4_triggered = False
        self.dragonkey_triggered = False
        self.worldbreaker_triggered = False #This and above are needed for game end
        self.pendant_triggered = False #This and below are optional
        self.tortoise_triggered = False
        self.elf_triggered = False
game_state = GameState()
game_state.priest_event_triggered = False
game_state.alter1_triggered = False
game_state.alter2_triggered = False
game_state.alter3_triggered = False
game_state.alter4_triggered = False
game_state.dragonkey_triggered = False
game_state.worldbreaker_triggered = False
game_state.pendant_triggered = False
game_state.tortoise_triggered = False
game_state.elf_triggered = False

#Story progressing Events:
def priest_event():
    if game_state.priest_event_triggered == False:
        type_print("You come across the Serpent Priest")
        type_print('"Find the altars and silence the one destroying these lands."')
        type_print("The Serpent Priest disappears walking into the ocean ahead of you.")
        game_state.priest_event_triggered = True
def alter1_event():
    if game_state.alter1_triggered == False:
        type_print("You come across an elevated stone altar")
        type_print("At the top of the altar lies a golden plate")
        type_print("You take the golden plate. \nAs you leave, the altar sinks into the ground.")
        key_items.append("Sun Disk 1")
        game_state.alter1_triggered = True
def alter2_event():
    if game_state.alter2_triggered == False:
        type_print("You come across an elevated stone altar")
        type_print("At the top of the altar lies a golden plate")
        type_print("You take the golden plate. \nAs you leave, the altar sinks into the ground.")
        key_items.append("Sun Disk 2")
        game_state.alter2_triggered = True
def alter3_event():
    if game_state.alter3_triggered == False:
        type_print("You come across an elevated stone altar")
        type_print("At the top of the altar lies a golden plate")
        type_print("You take the golden plate. \nAs you leave, the altar sinks into the ground.")
        key_items.append("Sun Disk 3")
        game_state.alter3_triggered = True
def alter4_event():
    if game_state.alter4_triggered == False:
        type_print("You come across an elevated stone altar")
        type_print("At the top of the altar lies a golden plate")
        type_print("You take the golden plate. \nAs you leave, the altar sinks into the ground.")
        key_items.append("Sun Disk 4")
        game_state.alter4_triggered = True
def dragonkey_event():
    altars = [
        game_state.alter1_triggered,
        game_state.alter2_triggered,
        game_state.alter3_triggered,
        game_state.alter4_triggered
    ]
    if all(altars) and game_state.dragonkey_triggered == False:
        type_print("After defeating the dragon you notice a lone scale on its body reflecting light")
        type_print("You pry the scale off, revealing a ranbow glimmer and familiar shape")
        type_print("You've acquired the Dragon-Scale Key")
        key_items.append("Dragon-Scale Key")
        time.sleep(1)
        type_print("You hear a distant rumbling. In the direction of where your quest began")
        game_state.dragonkey_triggered = True
def worldbreaker_event():
    events = [
        game_state.alter1_triggered,
        game_state.alter2_triggered,
        game_state.alter3_triggered,
        game_state.alter4_triggered,
        game_state.dragonkey_triggered
        ]
    if all(events):
        type_print("You've climbed to Sky Peak")
        type_print("You can't see the ground below the pyramid, only a sea of clouds")
        type_print("You notice an altar with four indentations")
        type_print("You insert your four Sun-Disks")
        type_print("The sky dims, revealing the stars and planet-like celestial bodies")
        type_print("One of the bodies is rapidly approaching your location!")
        type_print("A giant humanoid with glowing purple and blue tattoes running down every part of its body")
        type_print('-"I am the Worldbreaker and I declare these lands ready to rejoin the cosmic origins"')
        game_state.worldbreaker_triggered = True
def worldbreaker_defeated():
    type_print(f"You have defeated The Worldbreaker.")
    type_print(f"You watch as it turns into small glittery stars and fades into nothing.")
    type_print("As you look around, you can see the blue sky come back back into view.")
    type_print("At your feet, you find something left behind by your final foe..")
    type_print("You wade your hand in a cosmic puddle.")
    type_print("You feel a positive energy enter your body and you can see the truths of the world with a clarity previously impossible.")
    type_print("You've obtained the Cosmic Right and now have the power to restore the world to cosmic origins or allow for it to continue.")
    type_print("(Cosmic Origins or Existence)?")
    choice = input("Enter your choice: ")
    ending_done = False
    while ending_done == False:
        if choice.lower() == "cosmic origins":
            type_print("The sky turns dark again, with overhead celestial bodies becoming clearly visible")
            type_print("Tremors accompanied by loud noise fill the environment.")
            type_print("Suddenly you see the celestial bodies turn into smears across the sky, as the planet you stand on flies through the cosmos.")
            type_print("As your planet flies through space, you see the terrain around you peeling off the ground, breaking apart, atomizing")
            type_print("Soon you are standing on nothing, your planet and everything on it are totally gone")
            type_print("You alone float in dark space, but around you now have the power to reshape all the cosmic dust around you.")
            type_print("You now hold the power to reshape your world and create a new one in your image")
        elif choice.lower() == "existence":
            type_print("You take a deep breath before casting aside the Cosmic Right.  It disappears.")
            type_print("You look around at your environment from Sky Peak and take in the beauty of your surrounding.")
            type_print("You feel the world has changed because of you.  A warm feeling fills your chest after taking in the view of the area you've journeyed through.")
            type_print("After a moment you walk back down the pyramid to enjoy the new peace you've earned for the world.")
            if game_state.pendant_triggered:
                type_print("You see the older woman from the town you explored.")
                type_print("-'Look at you. I had a feeling you were gonna help bring peace back.'")
                type_print("-'After that giant pyramid popped up, I figured I'd check out what was happening before the world ends.'")
                type_print("-'I was pretty surprised on the way here, seeing that there weren't any monsters to make the trip as annoying as usual.'")
                type_print("-'I'm so grateful for what you've done. Thanks for soothing the soul of these lands.'")
            if game_state.elf_triggered:
                type_print("You see the elf from the forest.")
                type_print("-'I had a feeling you'd be caught up in the middle of all this trouble'")
                type_print("-'It is really such a relief to see you in one piece after all that's happened'")
                type_print("-'I must say, I'm rather happy that my friend has come back.")
                type_print("-'You and I must catch up. I'm sure you've got the most interesting stories to tell by now.")
                type_print("The elf laughs with a big smile on his face.  The first you've smile you've seen from him.")
            if game_state.tortoise_triggered:
                type_print("You see the tortoise from the plains.")
                type_print("-'Look at you tough guy! You seem to have been pretty important huh?'")
                type_print("-'When all the commotion started, I ran over as fast as I could.")
                type_print("-'I know what you're probably thinking, but I'm surprisingly fast!'")
                type_print("-'If dragons didn't have those wings, I swear I could take one in a race'")
                type_print("-'Hahaha! Well I'm just happy to see you alright.  We've got to celebrate our good health.")
                type_print("-'You know any places that have ale?  I haven't had a drink in ages.'")
            if game_state.pendant_triggered and game_state.elf_triggered and game_state.tortoise_triggered:
                type_print("You and your friends walk together to a nearby forest.")
                type_print("You start a fire, set up camp, and party with your friends.")
                type_print("Stories, laughs, and dances are shared.")
                type_print("You're so happy that everything turned out well...")

        else:
            "Invalid choice"

#Optional Events:
def pendant_event():
    print("----------")
    type_print("You come across a small town.")
    type_print("Walking down the main street of the town, you come across an older woman.")
    type_print("You see she holds a peculiar gold pendant with a vibrant green liquid in it.")
    type_print("You have the opportunity to easily steal her pendant")
    type_print("Do you take advantage of the chance to take this peculiar item?")
    type_print("Steal(S) or Pass(P)?")
    choice = input("Enter your choice: ")
    while game_state.pendant_triggered == False:
        choice = input("Enter your choice: ")
        while choice:
            if choice.lower() == "s":
                type_print("You easily take the pendant from the woman's necklace.")
                type_print("The woman puts up no resistance but she wears a pained expression as you walk away with her pendant.")
                my_player.items.append(pendant)
                type_print(f"You obtain {pendant.name}!")
                print("----------")
                game_state.pendant_triggered = True
                break
            elif choice.lower() == "p":
                type_print("You pass the woman")
                type_print("You calls you over to her and waves you down. ")
                type_print('-"You are strong and I have a feeling you have an important role to play in these lands."')
                type_print("-'I'd like to give you something that will help you on your journey.' \n-'I would give you my pendant, but it has deep sentimental value to me.'")
                type_print("-'I'm sure that this will be plenty helpful, and likely much more useful than an old lady's jewelry.'")
                my_player.items.append(platinum_ring)
                type_print(f"You obtain {platinum_ring.name}")
                print("----------")
                game_state.pendant_triggered = True
                break
            else:
                type_print("Invalid input.")
                choice = None
    
def tortoise_event():
    print("----------")
    type_print("You come across a peculiar rock imbedded in the ground.")
    type_print("As you approach the rock it begins to rise out of the ground")
    type_print("You realize the rock is actually the shell of a great tortoise the size of a small house.")
    type_print("-'You've startled me! Though, I am grateful to see you.  I rarely get visitors all the way out here'")
    type_print("-'I'd like to give you something. Its useless to me, but it should offer you protection.'")
    my_player.items.append(obsidian_scute)
    type_print(f"You obtain {obsidian_scute.name}!!")
    type_print("-'Dragons get so much more recognition because they are loud and can fly.  I doubt their scales are as tough as our shells though!'")
    type_print("-'Hahahaha! I wish you the best of luck on your travels, adventurer! You take care.'")
    print("----------")
    game_state.tortoise_triggered = True
def elf_event():
    print("----------")
    type_print("You come across a clearing within the forest")
    type_print("There is an elf sitting in the clearing")
    type_print("-'Welcome traveller. I feel fortunate to come across someone who doesnt have a malicious energy during these times'")
    type_print("-'Since I have a feeling you and I might've known eachother in a past life, I'd like to give you a gift.'")
    type_print("-'Lets remember how sweet it feels to get a gift from a friend and how sweet it is to show appreciation through giving a gift.'")
    my_player.items.append(ancient_branch)
    type_print(f"You obtain {ancient_branch.name}")
    type_print("-'Please take care. I'd love to talk to you again when these lands settle down'")
    game_state.elf_triggered = True

vitality_potion = Item("Vitality Potion", lambda: int(round(my_player.max_hp * .75)), 0, 0, 0, 0, 0)
spirit_potion = Item("Spirit Potion", 0, lambda: int(round(my_player.max_mp * .75)), 0, 0, 0, 0)

platinum_ring = Item("Platinum Ring", 0, 0, .4, .4, 30, 30)
ancient_branch = Item("Ancient Branch", 0, 0, .8, 0, 0, 40)
obsidian_scute = Item("Obsidian Scutes", 0, 0, 0, .8, 100, 0)
pendant = Item("Experience Potion", 0, 0, 0, 0, 0, 0)

basic_attack = Attack("Basic Attack", 5, 0, 0, 0, 0)
holy_light = Attack("Holy Light", 10, 8, 0, 0, 0)
fireball = Attack("Fireball", 15, 5, 0, .5, 0)
ice_skin = Attack("Ice Skin", 0, 15, .5, 1, 0)
enchanted_shot = Attack("Enchanted Shot", 15, 15, 0, 0, 0)
fire_grease = Attack("Fire Grease", 0, 15, 0, 2, 0)
vitality_drain = Attack("Vitality Drain", lambda: int(round(my_player.max_hp / 2)), 7, 0, 0, lambda: int(round(my_player.max_hp / 2)) * -1)#
spirit_drain = Attack("Spirit Drain", 0, -20, 0, 0, 10)#
healing_prayer = Attack("Healing Prayer", 0, 15, 0, 0, lambda: round(my_player.max_hp / 1.2) * -1)#

zombie_basic = Attack("Meandering Swipe", 5, 0, 0, 0, 0)
hollow_armor_basic = Attack("Gloom Lance", 10, 0, 0, 0, 0)
minotaur_basic= Attack("Trample", 25, 0, 0, 0, 0)
drake_basic = Attack("Fire Breath", 50, 0, 0, 0, 0)
dragon_basic = Attack("Red Lightning", 80, 0, 0, 0, 0)
worldbreaker_basic = Attack("First Sun", 120, 0, 0, 0, 0)

zombie_attacks = [zombie_basic]
hollow_armor_attacks = [hollow_armor_basic]
minotaur_attacks = [minotaur_basic]
drake_attacks = [drake_basic]
dragon_attacks = [dragon_basic]
worldbreaker_attacks = [worldbreaker_basic]

zombie = Enemy("zombie", 30, 30, zombie_attacks, 50)
hollow_armor = Enemy("hollow armor", 80, 80, hollow_armor_attacks, 80)
minotaur = Enemy("minotaur", 120, 120, minotaur_attacks, 150)
drake = Enemy("winged drake", 400, 400, drake_attacks, 250 )
dragon = Enemy("great dragon", 800, 800, dragon_attacks, 500)
worldbreaker = Enemy("WorldBreaker", 2000, 2000, worldbreaker_attacks, 2000)


def item_use():#-----player using consumable items
    type_print("Select an item: ")
    for item in my_player.items:
        type_print(f"-" + item.name)
    selected_item = input("Select an item:")
    player_item = None
    while player_item == None:
        for item in my_player.items:
            if selected_item.lower() == item.name.lower():
                player_item = item
                break
            elif selected_item.lower() == "q":
                break
        if player_item != "q" and player_item == None:
            type_print("Invalid item")
    if player_item:
        if callable(player_item.hp_restore):
            if player_item.hp_restore() > 0:
                heal_amount = player_item.hp_restore()
                my_player.hp += heal_amount
                type_print(f"You restore {heal_amount}HP.")
                my_player.items.remove(player_item)
        elif player_item.hp_restore > 0:
            heal_amount = player_item.hp_restore
            my_player.hp += player_item.hp_restore
            type_print(f"You restore {item.hp_restore}HP.")
        if callable(player_item.mp_restore):
            if player_item.mp_restore() > 0:
                spirit_amount = player_item.mp_restore()
                my_player.mp += spirit_amount
                type_print(f"You restore {spirit_amount}MP")
                my_player.items.remove(player_item)
        elif player_item.mp_restore > 0:
            spirit_amount = player_item.mp_restore
            my_player.mp += spirit_amount
            type_print(f"You restore {item.mp_restore}MP")
            my_player.items.remove(player_item)
        if player_item == pendant:
            type_print("This item should only be used out of combat. Continue? (Y/N)")
            response = input("Enter: ")
            if response.lower() == "y":
                type_print("You feel energy surge through you, enhancing your body and spirit")
                my_player.exp += my_player.max_hp
                my_player.items.remove(pendant)
            elif response.lower() == "n":
                return
            else:
                print("Invalid input")
        elif player_item == ancient_branch:
            type_print("This item should only be used out of combat. Continue? (Y/N)")
            response = input("Enter: ")
            if response.lower() == "y":
                type_print("You feel a rush of intense spiritual energy surge through your body and mind.")
                my_player.max_mp += ancient_branch.mp_mod
                type_print(f"+{ancient_branch.mp_mod}MP")
                my_player.atk += ancient_branch.atk_mod
                type_print(f"+{ancient_branch.atk_mod}Atk")
                my_player.items.remove(ancient_branch)
            elif response.lower() == "n":
                return
            else:
                print("Invalid input")
        elif player_item == obsidian_scute:
            type_print("This item should only be used out of combat. Continue? (Y/N)")
            response = input("Enter: ")
            if response.lower() == "y":
                type_print("The Obsidian Scutes reorganize across your body creating black reflective armor.")
                my_player.defs += obsidian_scute.def_mod
                type_print(f"+{obsidian_scute.def_mod}Def")
                my_player.max_hp += obsidian_scute.hp_mod
                my_player.hp += obsidian_scute.hp_mod
                type_print(f"+{obsidian_scute.hp_mod}HP")
                my_player.items.remove(obsidian_scute)
            elif response.lower() == "n":
                return
            else:
                print("Invalid input")
        elif player_item == platinum_ring:
            type_print("This item should only be used out of combat. Continue? (Y/N)")
            response = input("Enter: ")
            if response.lower() == "y":
                type_print("You feel a rush of intense spiritual energy surge through your body and mind.")
                my_player.atk += platinum_ring.atk_mod
                type_print(f"+{platinum_ring.atk_mod}Atk")
                my_player.defs += platinum_ring.def_mod
                type_print(f"+{platinum_ring.def_mod}Def")
                my_player.max_hp += platinum_ring.hp_mod
                type_print(f"+{platinum_ring.hp_mod}HP")
                my_player.max_mp += platinum_ring.mp_mod
                type_print(f"+{platinum_ring.mp_mod}MP")
                my_player.items.remove(platinum_ring)
            elif response.lower() == "n":
                return
            else:
                print("Invalid input")
    if my_player.hp > my_player.max_hp:
        my_player.hp = my_player.max_hp
    if my_player.mp > my_player.max_mp:
        my_player.mp = my_player.max_mp
    

def item_find():#--Player finding item after movement
    if my_player.hp > 0:
        found_item = random.choice(item_glossary)
        item_list.append(found_item)
        type_print(f"You come across a {found_item.name}!")

def combat():
    player_turn = True
    original_atk = my_player.atk
    original_def = my_player.defs
    combat = True
    if game_state.dragonkey_triggered and my_player.x == 4 and my_player.y == 4:
        worldbreaker_event()
        attacker = worldbreaker
    else:
        attacker = random.choice(current_enemies)
    type_print(f"The {attacker.name} attacks!")
    def player_action():     
        if attacker.hp > 0:
            type_print(f"You have: \n{my_player.hp}/{my_player.max_hp}HP \n{my_player.mp}/{my_player.max_mp}MP")
            print()
            type_print("Select an action: ")
            for actions in combat_actions:
                type_print(actions.capitalize())
            selected_action = input("Enter your action: ")
            if selected_action.lower() == "attack":
                type_print("Select an attack:")
                for attack in my_player.attacks:
                    if callable(attack.mp_cost):
                        type_print(f"{attack.name} - {attack.hp_cost}HP")
                    else:
                        type_print(f"{attack.name} - {attack.mp_cost}MP")
                selected_attack = input("Enter your attack: ")

                player_attack = None
                for attack in my_player.attacks:
                    if selected_attack.lower() == attack.name.lower():
                        player_attack = attack
                        break
                if player_attack.mp_cost <= my_player.mp:
                    accuracy_roll = random.randint(1, 21)
                    if callable(player_attack.hp_cost):
                        health_cost = player_attack.hp_cost()
                    elif player_attack.hp_cost:
                        health_cost = player_attack.hp_cost
                    else:
                        health_cost = 0
                    if callable(player_attack.mp_cost):
                        mp_cost = player_attack.mp_cost()
                    elif player_attack.mp_cost:
                        mp_cost = player_attack.mp_cost
                    else:
                        mp_cost = 0
                    if player_attack != vitality_drain:
                        if callable(player_attack.base_damage):
                            damage = round(player_attack.base_damage() * my_player.atk)
                        elif player_attack.base_damage:
                            damage = round(player_attack.base_damage * my_player.atk)
                        else:
                            damage = 0
                    else:
                        if callable(player_attack.base_damage):
                            damage = round(player_attack.base_damage())
                        elif player_attack.base_damage:
                            damage = round(player_attack.base_damage)
                        else:
                            damage = 0
                    if 20 > accuracy_roll > 1:
                        my_player.hp -= health_cost
                        my_player.mp -= mp_cost
                        if damage > 0:
                            attacker.hp -= damage
                            type_print(f"You use {player_attack.name}. \nIt inflicts {damage} damage!")
                        if health_cost != 0:
                            my_player.hp -= health_cost
                            type_print(f"Your HP ({-health_cost})")#
                        if player_attack.def_mod != 0:
                            my_player.defs += player_attack.def_mod
                        if player_attack.atk_mod != 0:
                            my_player.atk += player_attack.atk_mod
                    elif accuracy_roll == 20:
                        my_player.hp -= health_cost
                        my_player.mp -= mp_cost
                        if damage > 0:
                            attacker.hp -= damage
                            type_print(f"You use {player_attack.name}. \nIt critically strikes for {damage} damage!!")
                        if health_cost != 0:
                            type_print(f"Your HP rose {-health_cost}")
                        if player_attack.def_mod != 0:
                            my_player.defs += player_attack.def_mod
                        if player_attack.atk_mod != 0:
                            my_player.atk += player_attack.atk_mod
                    elif accuracy_roll == 1:
                        type_print("You've missed!")
                if player_attack == None:
                    type_print("Invalid attack")
            elif selected_action.lower() == "item":
                item_use()
            elif selected_action.lower() == "run":
                escape_roll = random.randint(1, 21)
                if escape_roll == 1:
                    type_print("You couldn't escape")
                    return
                else:
                    nonlocal combat
                    type_print("You ran away")
                    combat = False
            else:
                type_print("Invalid action")
        print()
                        


    def enemy_action():
        if attacker.hp > 0 and my_player.hp > 0:
            chosen_attack = random.choice(attacker.attacks)
            accuracy_roll = random.randint(1, 21)
            if 19 >= accuracy_roll > 1:
                damage = round((chosen_attack.base_damage /my_player.defs), )
                type_print(f"The {attacker.name} uses {chosen_attack.name}. \nYou take {damage} damage!")
                my_player.hp -= damage
            elif accuracy_roll == 1:
                type_print(f"The {attacker.name} uses {chosen_attack.name}. \nIt misses!!")
            elif accuracy_roll == 20:
                damage = round((chosen_attack.base_damage * 2)/ my_player.defs)
                my_player.hp -= damage
                type_print(f"The {attacker.name} uses {chosen_attack.name}. \nIt critically strikes for {damage} damage!!")
        print()

            

    while combat:
        player_turn = True
        while player_turn:
            if attacker.hp > 0 and my_player.hp > 0:
                player_action()
                player_turn = False
            elif attacker.hp <= 0:
                combat = False
                player_turn = False
            elif my_player.hp <= 0:
                type_print("You have been defeated...")
                combat = False
                break
        while not player_turn and combat:
            if attacker.hp <= 0:
                type_print(f"You've defeated the {attacker.name}!")
                my_player.exp += attacker.exp
                combat = False
                attacker.hp = attacker.max_hp
                my_player.atk = original_atk
                my_player.defs = original_def
                break
            elif attacker.hp > 0 and my_player.hp > 0:
                enemy_action()
                player_turn = True
        if not combat:
            if my_player.hp > my_player.max_hp:
                my_player.hp = my_player.max_hp
            break
    if attacker == dragon:
        dragonkey_event()

        



#Job basic moveset
knight_attacks = [holy_light, healing_prayer]
mage_attacks = [fireball, ice_skin]
hunter_attacks = [enchanted_shot, fire_grease]
druid_attacks = [vitality_drain, spirit_drain]

all_attacks = [holy_light, healing_prayer, fireball, ice_skin, enchanted_shot, fire_grease, vitality_drain, spirit_drain]

item_glossary = [vitality_potion, spirit_potion]
item_list = [vitality_potion, spirit_potion]

special_item_glossary = [ancient_branch, obsidian_scute, platinum_ring, pendant]
special_item_list = []
key_items = []

enemy_list = [zombie, hollow_armor, minotaur, drake, dragon, worldbreaker]
current_enemies = [zombie]
enemyupdatelist = [3, 6, 12, 20, 21]


hp = 0
mp = 0
exp = 0
level = 1
player_name = "h"
player_job = ""
attacks = [basic_attack]
removechar = "_"
attacks_text = (str(attacks)).replace(removechar, " ").capitalize()


def show_geography(my_player):
    west_coords = [0, 1, 2, 3]
    east_coords = [5, 6, 7, 8, 9]
    north_coords = [0, 1, 2, 3]
    south_coords = [5, 6, 7, 8, 9]
    #Event trigger Coordinates
    if my_player.x == 7 and my_player.y == 7:
        alter1_event()
    elif my_player.x == 0 and my_player.y == 5:
        alter2_event()
    elif my_player.x == 8 and my_player.y == 0:
        alter3_event()
    elif my_player.x == 2 and my_player.y == 2:
        alter4_event()
    elif my_player.x == 8 and my_player.y == 3 and game_state.pendant_triggered == False:
        pendant_event()
    elif my_player.x == 9 and my_player.y == 7 and game_state.tortoise_triggered ==False:
        tortoise_event()
    elif my_player.x == 3 and my_player.y == 8 and game_state.elf_triggered == False:
        elf_event()
    #area info Coordinates
    elif my_player.x in east_coords and my_player.y in north_coords:
        type_print("You traverse through clear grasslands..")
    elif my_player.x in east_coords and my_player.y in south_coords:
        type_print("You traverse through an arid plain..")
    elif my_player.x in west_coords and my_player.y in north_coords:
        type_print("You traverse through volcanic terrain..")
    elif my_player.x in west_coords and my_player.y in south_coords:
        type_print("You traverse through a dense forest..")


    if game_state.dragonkey_triggered is True:
        pyramid_ne_quadx = [2, 3]
        pyramid_ne_quady = [2, 3]
        pyramid_nw_quadx = [5, 6]
        pyramid_nw_quady = [2, 3]
        pyramid_se_quadx = [5, 6]
        pyramid_se_quady = [5, 6]
        pyramid_sw_quadx = [2, 3]
        pyramid_sw_quady = [5, 6]
        pyramid_nx = [4]
        pyramid_ny = [2, 3]
        pyramid_ex = [5, 6]
        pyramid_ey = [4]
        pyramid_sx = [4]
        pyramid_sy = [5, 6]
        pyramid_wx = [2, 3]
        pyramid_wy = [4]
        if my_player.x in pyramid_ne_quadx and my_player.y in pyramid_ne_quady:
            type_print("You see the top of the pyramid towards the Southwest")
        elif my_player.x in pyramid_nw_quadx and my_player.y in pyramid_nw_quady:
            type_print("You see the top of the pyramid towards the Southeast.")
        elif my_player.x in pyramid_se_quadx and my_player.y in pyramid_se_quady:
            type_print("You see the top of the pyramid towards the Northwest.")
        elif my_player.x in pyramid_sw_quadx and my_player.y in pyramid_sw_quady:
            type_print("You see the top of the pyramid towards the Northeast.")
        elif my_player.x in pyramid_nx and my_player.y in pyramid_ny:
            type_print("You see the top of the pyramid towards the south")
        elif my_player.x in pyramid_sx and my_player.y in pyramid_sy:
            type_print("You see the top of the pyramid towards the North.")
        elif my_player.x in pyramid_ex and my_player.y in pyramid_ey:
            type_print("You can see the top of the pyramid towards the West.")
        elif my_player.x in pyramid_wx and my_player.y in pyramid_wy:
            type_print("You can see the top of the pyramid towards the East.")




def show_actions():
    for action in world_actions:
        print(action.capitalize())
    print("----------")


def ask_player():#overworld options for player, Central loop.
    if my_player.hp > 0:
        user_input = input("What will you do?: ")
        if user_input.lower() == "actions":
            show_actions()
        elif user_input.lower() == "skills":
            for attack in my_player.attacks:
                if callable(attack.hp_cost):
                    health_cost = attack.hp_cost()
                elif attack.hp_cost:
                    health_cost = attack.hp_cost
                else:
                    health_cost = 0
                if health_cost != 0:
                    type_print(attack.name)
                    skill_choice = input("Select a skill to use: ")
                    if skill_choice.lower() == attack.name.lower():
                        my_player.hp -= health_cost
                    elif skill_choice.lower() == "q":
                        break
                    else:
                        type_print("Invalid skill")
        elif user_input.lower() == "move":
            my_player.move(None)
            combat_chance_roll = random.randint(1, 20)
            item_chance_roll = random.randint(1, 21)
            if combat_chance_roll >=10:
                combat()
            if item_chance_roll >= 13:
                item_find()
        elif user_input.lower() == "item":
            item_use()
        elif user_input.lower() == "reflect":
            type_print(f"You have {my_player.hp}/{my_player.max_hp}HP")
            type_print(f"You have {my_player.mp}/{my_player.max_mp}MP")
            type_print(f"You have {my_player.atk}Atk")
            type_print(f"You have {my_player.defs}Def")
            type_print(f"You have {round(my_player.exp)}/{round(my_player.need_exp)}Exp")
        elif user_input.lower() == "godmode":
                my_player.max_hp += 20
                my_player.max_mp += 20
                my_player.hp += 20
                my_player.mp += 20
                my_player.atk += 3
                my_player.defs += 1
                my_player.exp = my_player.need_exp
        elif user_input.lower() == "alter1":
            alter1_event()
        elif user_input.lower() == "alter2":
            alter2_event()
        elif user_input.lower() == "alter3":
            alter3_event()
        elif user_input.lower() == "alter4":
            alter4_event()
        else:
            print("Invalid input")

def add_enemy():
    if my_player.lvl == 3:
        current_enemies.append(hollow_armor)
        type_print("You sense the land's increased hostility...")
    elif my_player.lvl == 6:
        current_enemies.append(minotaur)
        type_print("You sense the land's increased hostility...")
    elif my_player.lvl == 12:
        current_enemies.append(drake)
        type_print("You sense the land's increased hostility...")
    elif my_player.lvl == 16:
        current_enemies.append(dragon)
        type_print("You sense the land's increased hostility...")
    elif my_player.lvl == 20:
        if game_state.dragonkey_triggered:
            current_enemies.append(worldbreaker)
            type_print("You sense the land's increased hostility...")




if answer == "yes":
    job_assigned = False
    while job_assigned == False:
        type_print("Select a class:")
        for job in jobs:
            type_print(job.capitalize())
        player_job = input("Type in your class: ").lower().strip()
        my_player = Player(player_name, player_job, 0, 0, 0, 0, 0, 0, 1, 0, 30, attacks, item_list, x=4, y=4, grid=grid)
        if player_job == "knight":
            my_player.hp += 30
            my_player.max_hp += 30
            my_player.mp += 50
            my_player.max_mp += 50
            my_player.atk += 1
            my_player.defs += 1
            my_player.attacks.extend(knight_attacks)
            type_print(f"Your job is {player_job}. \nYou have {my_player.hp}HP and {my_player.mp}MP")
            print("----------")
            job_assigned = True
        elif player_job == "mage":
            my_player.hp += 15
            my_player.max_hp += 15
            my_player.mp += 100
            my_player.max_mp += 100
            my_player.atk += 1.2
            my_player.defs += .8
            my_player.attacks.extend(mage_attacks)
            type_print(f"Your job is {player_job}. \nYou have {my_player.hp}HP and {my_player.mp}MP")
            print("----------")
            job_assigned = True
        elif player_job == "hunter":
            my_player.hp += 20
            my_player.max_hp += 20
            my_player.mp += 50
            my_player.max_mp += 50
            my_player.atk += 1.2
            my_player.defs += 1.0
            my_player.attacks.extend(hunter_attacks)
            type_print(f"Your job is {player_job}. \nYou have {my_player.hp}HP and {my_player.mp}MP")
            print("----------")
            job_assigned = True
        elif player_job == "druid":
            my_player.hp += 20
            my_player.max_hp += 20
            my_player.mp += 100
            my_player.max_mp += 100
            my_player.atk += 1
            my_player.defs += 1.2
            my_player.attacks.extend(druid_attacks)
            type_print(f"Your job is {player_job}. \nYou have {my_player.hp}HP and {my_player.mp}MP")
            print("----------")
            job_assigned = True
        else:
            print("Invalid job name")
    if player_job:
        type_print("To view possible actions at any time, enter 'actions'")
        print("----------")
        while my_player.location == "4-4":
            type_print("You awake in an open field. While it is peaceful here, you sense danger nearby")
            print()
            break

elif answer == "no":
    print("Damn okay")
else:
    print("Invalid Bruh...")
while answer.lower() == "yes" and my_player.hp >= 0:
    ask_player()
    if my_player.exp >= my_player.need_exp:
        Player.lvl_up()
        add_enemy()
    if game_state.worldbreaker_triggered and my_player.hp > 0:
        worldbreaker_defeated()
        type_print("You've beaten the game.")
        type_print("Ending in 3 seconds...")
        time.sleep(3)
        sys.exit()
    if my_player.hp > 0:
        show_geography(my_player)
    elif my_player.hp <= 0:
        type_print("Game Over")
