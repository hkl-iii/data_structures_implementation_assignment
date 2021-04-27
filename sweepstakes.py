import random


class Sweepstakes:

    def __init__(self):
        self.contestants = []

    def add_contestants(self):
        self.contestants.push = ['michael jackson']
        self.contestants.push = ['whitney houston']
        self.contestants.push = ['chris brown']
        self.contestants.push = ['mariah carey']
        self.contestants.push = ['luther vandross']
        print(random.choice(self.contestants))
