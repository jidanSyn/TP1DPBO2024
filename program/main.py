# Saya Jidan Abdurahman Aufan NIM [2205422] mengerjakan soal TP1 dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin

import sys
from Console import Console
from PlayerCharacter import PlayerCharacter
from MonsterCharacter import MonsterCharacter
from Role import Role
from Party import Party
from Weapon import Weapon
from CombatEvent import CombatEvent
from Quest import Quest
from Skill import Skill
# from ConsoleUtilities import ConsoleUtilities

# for now im just gonna set to be only 3 roles, warrior, mage, cleric, maybe further game progression
# will see job upgrades / change or smth

# init
slime_skills = [Skill("Tackle")]
goblin_skills = [Skill("Weak Stab")]
wolf_skills = [Skill("Bite", 1.1), Skill("Scratch")]
blank_weapon = Weapon("Placeholder")
goblin_dagger = Weapon("Goblin Dagger", "A rusty goblin dagger")

quests = [
        Quest(
            "Slime Extermination I", "Exterminate a Party of Lv.1 Slimes in the Plains.", "Plains", Party(
                [
                MonsterCharacter("Slime A", '', skills=slime_skills, weapon=blank_weapon), 
                MonsterCharacter("Slime B", '', skills=slime_skills, weapon=blank_weapon), 
                MonsterCharacter("Slime C", '', skills=slime_skills, weapon=blank_weapon)
                ]),
            min_rank="F"
            ),

        Quest(
            "Goblin Extermination I", "Exterminate a Party of Lv.1 Goblins in the Rocky Cave.", "Rocky Cave", 
            Party(
                [
                MonsterCharacter("Goblin A", '', skills=goblin_skills, weapon=goblin_dagger), 
                MonsterCharacter("Goblin B", '', skills=goblin_skills, weapon=goblin_dagger), 
                MonsterCharacter("Goblin C", '', skills=goblin_skills, weapon=goblin_dagger)]),
            min_rank="F"
            ),

        Quest(
            "Wolf Extermination I", "Exterminate a Party of Lv.1 Goblins in the Howling Forest.", "Howling Forest", 
            Party(
                [
                MonsterCharacter("Wolf A", '', skills=wolf_skills, weapon=blank_weapon), 
                MonsterCharacter("Wolf B", '', skills=wolf_skills, weapon=blank_weapon), 
                MonsterCharacter("Wolf C", '', skills=wolf_skills, weapon=blank_weapon)]),
            min_rank="E"
            ),
            
          ]

default_warrior_skills = [Skill("Slash", 1.4, "A basic diagonal sword slash.")]
default_mage_skills = [Skill("Fireball", 1.3, skill_type="magical"), Skill("Whack", 1.1)]
default_cleric_skills = [Skill("Whack", 1.1), Skill("Mini Heal", 1.2, "Heals minor injuries.",skill_type="healing", target_type="ally")]

default_warrior_weapon = Weapon("Iron Shortsword", atk_mod=1.2)
default_mage_weapon = Weapon("Mage Staff", m_atk_mod=1.6)
default_cleric_weapon = Weapon("Cleric Staff", heal_mod=1.5)


role_warrior = Role("Warrior", 3, 1, 4, 3, default_warrior_skills, default_warrior_weapon)
role_mage = Role("Mage", 1, 5, 1, 1, default_mage_skills, default_mage_weapon)
role_cleric = Role("Cleric", 2, 3, 3, 2, default_cleric_skills, default_cleric_weapon)
# ...

# game start
Console.clear()

print("Welcome to Triforce Adventuring Guild!")

# party registration
print("Before anything, let's register your party!")

# get name
print("What is your party's name?")
print("Enter party name: ", end='')
partyname = input()
Console.clear_lines(2)


# who is your warrior
print("What is your warrior's name? ")
w_name = input("Enter warrior name: ")
w_gender = input("Gender(Male/Female): ")
warrior = PlayerCharacter(w_name, w_gender, role=role_warrior)
Console.clear_lines(3)


# who is your mage
print("What is your mage's name? ")
m_name = input("Enter mage name: ")
m_gender = input("Gender(Male/Female): ")
mage = PlayerCharacter(m_name, m_gender, role=role_mage)
Console.clear_lines(3)



# who is your cleric
print("What is your cleric's name? ")
c_name = input("Enter cleric name: ")
c_gender = input("Gender(Male/Female): ")
cleric = PlayerCharacter(c_name, c_gender, role=role_cleric)
Console.clear_lines(3)


party = Party([warrior, mage, cleric], partyname)

print()

# welcome to the adventuring guild! you can choose etc to etc
print("Registration complete! Your party will start at Rank F, you can start looking at quests now,\nor you can go to the shop,\nyou can also check your party's details here.")
input("\nPress Enter to continue...")

confirm = ""
menu_input = -1
# game loop till exit
while True:
    Console.clear()
    # prompt interact shop, quest, exit, party info
    print("What will you do?")
    print("1. Check Quests\n2. Go to Shop\n3. Check Party Info\n4. Exit Game")
    menu_input = int(input("Select: "))
    if menu_input == 1:
        for index, quest in enumerate(quests):
            print(f"Quest #{index + 1}")
            quest.describe_quest()
        
        # if take 
        take_quest = int(input("Select a quest to take: "))
        chosen_quest = quests[take_quest - 1]

        # if chosen_quest.get_min_rank() # todo pengecekan quest berdasarkan rank (BONUS)
        combat_event = CombatEvent(party, chosen_quest.get_target())
        
        # battle loop
        combat_event.simulate_combat()
        
        # calculate character growth
        
    elif menu_input == 2:
        # todo hehe
        # buy new weapon
        # and maybe refine owned weapons? or maybe diff menu, blacksmith?
        print("")
    elif menu_input == 3:
        party.print_party_details()
    elif menu_input == 4:
        print("Are you sure you want to quit? Progress will not be saved..")
        confirm = input("(yes/no): ")
        if confirm == "yes":
            sys.exit()
        elif confirm == "no":
            print("Cancelled quitting the game.")

    input("\nPress Enter to continue...")







# combat logic
