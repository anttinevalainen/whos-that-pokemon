class Player:
    def __init__(self, gamertag, gamemode):
        self.gamertag = str(gamertag)
        self.points = 0
        self.correct_answers = 0
        self.health = 3
        self.gamemode = gamemode

    def correct_answer(self):
        point_multiplier = self.gamemode.get_number_of_generations()
        self.points += 50 * point_multiplier
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

    def get_gamemode(self):
        return self.gamemode
