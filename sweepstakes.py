import random


class Sweepstakes:

    def __init__(self):
        self.contestants = []

    def add_contestants(self):
        self.contestants.append('michael jackson')
        self.contestants.append('whitney houston')
        self.contestants.append('chris brown')
        self.contestants.append('mariah carey')
        self.contestants.append('luther vandross')
        print(random.choice(self.contestants))
