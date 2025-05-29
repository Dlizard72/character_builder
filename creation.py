from random import randint
from dataclasses import dataclass


@dataclass
class Attributes:
    Str: int
    Int: int
    Wis: int
    Dex: int
    Con: int
    Cha: int
    proficient_skills: list[str] = None  

    def __post_init__(self):
        if self.proficient_skills is None:
            self.proficient_skills = []

    def modifier(self, stat_name):
        return (getattr(self, stat_name) - 10) // 2

    def skill_bonus(self, skill_name, proficiency_bonus=2):
        # Map each skill to the corresponding ability
        skill_to_ability = {
            "Acrobatics": "Dex",
            "Animal Handling": "Wis",
            "Arcana": "Int",
            "Deception": "Cha",
            "History": "Int",
            "Insight": "Wis",
            "Intimidation": "Cha",
            "Investigation": "Int",
            "Perception": "Wis",
            "Performance": "Cha",
            "Persuasion": "Cha",
            "Religion": "Int",
            "Sleight of Hand": "Dex",
            "Stealth": "Dex",
            "Survival": "Wis",
        }

        ability = skill_to_ability.get(skill_name)
        if ability is None:
            return 0  # Skill not found

        bonus = self.modifier(ability)
        if skill_name in self.proficient_skills:
            bonus += proficiency_bonus
        return bonus
def roll_die() -> list[int]:
    """Rolls a 6-sided die 4 times and returns them sorted."""
    return sorted(randint(1, 6) for _ in range(4))

def drop_lowest() -> int:
    """Rolls 4d6 and returns the sum of the highest 3 rolls."""
    return sum(roll_die()[1:])

hit_die_by_class = {
    "Barbarian": 12,
    "Fighter": 10,
    "Paladin": 10,
    "Ranger": 10,
    "Bard": 8,
    "Cleric": 8,
    "Druid": 8,
    "Monk": 8,
    "Rogue": 8,
    "Warlock": 8,
    "Sorcerer": 6,
    "Wizard": 6,
    "Artificer": 8
}

def calculate_hp(dnd_class, con_mod):
    base_hit_die = hit_die_by_class.get(dnd_class, 8)  # default to d8 if unknown
    return base_hit_die + con_mod