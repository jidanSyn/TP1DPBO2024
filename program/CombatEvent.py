
import time
import random
from Party import Party
from Console import Console


class CombatEvent:
    def __init__(self, party:Party, enemy_party:Party):
        self.party = party
        self.enemy_party = enemy_party
        self.ally_members = party.get_members()
        self.enemy_members = enemy_party.get_members()

    def is_party_dead(self, members):
        return all(member.get_current_health() == 0 for member in members)
    

    def render_targets(self, target_members):
        for i in range(3):
            print(f"\t{i + 1}. {target_members[i].get_name()}, Lv.{target_members[i].get_level()} ({target_members[i].get_current_health()}/{target_members[i].get_max_health()})", end='')
            
    def render_current_state(self):
        for i in range(3):
            print(f"\t{self.ally_members[i].get_name()}, Lv.{self.ally_members[i].get_level()} ({self.ally_members[i].get_current_health()}/{self.ally_members[i].get_max_health()})")
        
        print()

        for i in range(3):
            print(f"\t{self.enemy_members[i].get_name()}, Lv.{self.enemy_members[i].get_level()} ({self.enemy_members[i].get_current_health()}/{self.ally_members[i].get_max_health()})")

    
    def resolve_action(self, source, target, skill_index):

        if target.get_current_health() <= 0:
            print("Target is already dead!")
            return

        skill = source.get_skills()[skill_index]
        value = skill.calculate_value(source)
        skill_type = skill.get_skill_type()
        if skill_type == "healing": # if healing skill
            target.restore_health(value)
        else: # if damaging skill
            target.take_damage(value, skill_type)

        print(f"{source.get_name()} used {source.get_skills()[skill_index].get_name()} to {target.get_name()}!")

        if target.get_current_health() <= 0:
            target.set_out_of_combat_status(True)
        


    # pseudo:
    # while battle not finished / party defeated
        # clear screen
        # rotate through party and choose skill
        # execute skill/action
        # rotate through enemy party
        # execute action
    def simulate_combat(self):

        combat_ended = False

        # maybe a turn mechanism sorting based on speed?
        for i in range(3, 0, -1):
            print(f"Entering combat in {i}..", end='\r')
            time.sleep(1)


        while not combat_ended:
            Console.clear()
            # render combat screen
            self.render_current_state()
            line_count = 0
            
            # iterate through each ally
            for member in self.ally_members:

                if not member.get_out_of_combat_status():
                    # select action
                    print(f"What will {member.get_name()} do?") 
                    member.display_skills()
                    selected_skill = int(input("Select a skill: "))
                    n_skills = len(member.get_skills())

                    # select target
                    target_members = self.ally_members if member.get_skills()[selected_skill - 1].get_target_type() == "ally" else self.enemy_members # -1 because output is 1-indexed so user will choose in 1-indexed-based while data is zero-indexed

                    self.render_targets(target_members)
                    selected_target = int(input("\nChoose a target: "))

                    line_count += n_skills + 1  # lines to erase, + 1 skill prompt, + n skills + 3 targets
                    Console.clear_lines(line_count)

                    # execute action
                    self.resolve_action(member, target_members[selected_target - 1], selected_skill - 1)

                    # check if combat has ended
                    ally_party_dead = self.is_party_dead(self.ally_members)
                    enemy_party_dead = self.is_party_dead(self.enemy_members)
                    if ally_party_dead or enemy_party_dead:
                        combat_ended = True
                        break

            # iterate through each enemy
            for member in self.enemy_members:
                if not member.get_out_of_combat_status():
                    # select action
                    selected_skill = random.randint(0, len(member.get_skills()) - 1)

                    # select target
                    # target pool is inverted now
                    target_members = self.enemy_members if member.get_skills()[selected_skill].get_target_type() == "ally" else self.ally_members

                    # line_count += n_skills + 4 # lines to erase, + 1 skill prompt, + n skills + 3 targets
                    # Console.clear_lines(line_count)

                    # execute action
                    self.resolve_action(member, target_members[random.randint(0, len(target_members)) - 1], selected_skill)

                    # check if combat has ended
                    ally_party_dead = self.is_party_dead(self.ally_members)
                    enemy_party_dead = self.is_party_dead(self.enemy_members)
                    if ally_party_dead or enemy_party_dead:
                        combat_ended = True
                        break
            
            input("Press Enter to continue...")
            
        if ally_party_dead: # defeated
            print("Defeated...")
            return False
        elif enemy_party_dead: # won
            print("Victory!")
            return True
    
    
