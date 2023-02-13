from itertools import groupby
from numpy import array_split

class Grouper():
    def __init__(self, fencers, groups_num):
        self.fencers = fencers
        self.groups_num = groups_num
        self.weapons_num = 3
        self.groups = []
        self.group()

    def group(self):
        foil, epee, saber = [], [], []
        for fencer in self.fencers:
            match fencer.weapon:
                case 'F': foil.append(fencer)
                case 'D': epee.append(fencer)
                case 'S': saber.append(fencer)
                case _: raise ValueError
        weapons = [foil, epee, saber]
        print(saber[0])
        percentages = []
        for weapon in weapons:
            if not weapon:
                weapons.remove(weapon)
        for weapon in weapons:
            weapon.sort()
            percentages.append(len(weapon) / len(self.fencers))
        if self.groups_num < len(weapons):
            self.groups_num = len(weapons)
        group_sizes = self.divide_into_parts(self.groups_num, percentages)
        for i, weapon in enumerate(weapons):
            groups = self.list_split(weapon, group_sizes[i])
            for group in groups:
                self.groups.append(group)
        self.weapons_num = len(weapons)

    def list_split(self, l, num):
        return [a.tolist() for a in array_split(l, num)]

    def divide_into_parts(self, integer, percentages):
        parts = []
        for percentage in percentages:
            fraction = percentage / 100
            part = integer * fraction
            parts.append(int(round(part)))
        diff = integer - sum(parts)
        for i in range(diff):
            parts[i % len(parts)] += 1
        return parts
