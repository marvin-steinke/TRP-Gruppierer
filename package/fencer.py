from datetime import date, datetime
from functools import total_ordering

@total_ordering
class Fencer:
    def __init__(self, lastname, firstname, birthdate, gender, weapon, club):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = datetime.strptime(birthdate, '%d.%m.%Y')
        self.birthyear = self.birthdate.year
        self.gender = gender
        self.weapon = weapon
        self.club = club
        self.age = self.calcAge()
        self.age_class = self.getAgeClass(self.age)

    def calcAge(self) -> int:
        today = date.today()
        age = today.year - self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))
        return age

    def getAgeClass(self, age) -> str:
        if age < 11: return 'U11'
        elif age < 13: return 'U13'
        elif age < 15: return 'U15'
        elif age < 17: return 'U17'
        elif age < 20: return 'Junioren'
        elif age < 40: return 'Senioren'
        else: return 'Veteranen'

    def str_PDF(self) -> str:
        return f'{self.firstname} {self.lastname}, {self.club}, {self.age} J.'

    def __str__(self) -> str:
        return f'{self.age}{self.gender}, {self.club}, {self.lastname} ({self.weapon})'

    def __lt__(self, other) -> bool:
        return self.age < other.age

    def __eq__(self, other) -> bool:
        return self.age == other.age and self.club == other.club
