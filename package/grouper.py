from numpy import array_split

class Grouper():
    def __init__(self, fencers, groups_num):
        self.fencers = fencers
        self.groups_num = groups_num
        self.groups = []
        self.weapons_num = 2
        self.group()

    def group(self):
        foil_groups = []
        epee_groups = []
        for fencer in self.fencers:
            match fencer.weapon:
                case 'F': foil_groups.append(fencer)
                case 'D': epee_groups.append(fencer)
                case _: raise ValueError
        foil_groups.sort()
        epee_groups.sort()
        if not foil_groups:
            self.groups = [a.tolist() for a in array_split(epee_groups, self.groups_num)]
            self.weapons_num = 1
            return
        if not epee_groups:
            self.groups = [a.tolist() for a in array_split(foil_groups, self.groups_num)]
            self.weapons_num = 1
            return
        if self.groups_num < 2: self.groups_num = 2
        foil_groups_num = round(len(foil_groups) / len(self.fencers) * self.groups_num)
        if foil_groups_num == 0: foil_groups_num = 1
        epee_groups_num = self.groups_num - foil_groups_num
        foil_groups = [a.tolist() for a in array_split(foil_groups, foil_groups_num)]
        epee_groups = [a.tolist() for a in array_split(epee_groups, epee_groups_num)]
        self.groups = foil_groups + epee_groups
