class Player:
    def __init__(self, gamertag):
        self.gamertag = str(gamertag)
        self.points = 0
        self.correct_answers = 0
        self.health = 3

    def correct_answer(self):
        self.points += 1000
        self.correct_answers += 1

    def incorrect_answer(self):
        if self.health >= 1:
            self.health -= 1

    def get_health(self):
        return self.health

    def get_gamertag(self):
        return self.gamertag

    def get_points(self):
        return self.points

    def get_correct_answers(self):
        return self.correct_answers
