class Habits:
    def __init__(self, forfeit):
        self.forfeit = forfeit


class Smoking(Habits):
    def __init__(self, forfeit):
        super().__init__(forfeit)


class Drugs(Habits):
    def __init__(self, forfeit, chance_to_die, chance_to_be_rich):
        super().__init__(forfeit)
        self.chance_to_die = chance_to_die
        self.chance_to_be_rich = chance_to_be_rich


class Lust(Habits):
    def __init__(self, forfeit, reward, for_married=False):
        super().__init__(forfeit)
        self.reward = reward
        self.for_married = for_married


class Catism(Habits):
    def __init__(self, forfeit, chance_to_die, reward):
        super().__init__(forfeit)
        self.chance_to_die = chance_to_die
        self.reward = reward


class Alcohol(Habits):
    def __init__(self, forfeit, for_married=True):
        super().__init__(forfeit)
        self.for_married = for_married


class Abuse(Habits):
    def __init__(self, forfeit, reward, only_poor_job=True):
        super().__init__(forfeit)
        self.reward = reward
        self.only_poor_job = only_poor_job


drugman = Drugs(20, [75, 100], [0, 10])

print(drugman.__dict__)
