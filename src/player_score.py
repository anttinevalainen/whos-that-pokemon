class Player_score:
    def __init__(self):
        self.points = 0
        self.correct_answers = 0

    def get_final_score(self):
        return self.points, self.correct_answers

    def get_points(self):
        return self.points
    
    def get_correct_answers(self):
        return self.correct_answers