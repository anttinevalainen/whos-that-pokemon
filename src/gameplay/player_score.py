class Player:
    '''A class that depicts user's player profile based on
    gamertag choice and game progress

    Attributes:
        gamertag: A three letter string value of user's choice

        points: A number that rises when user answers correctly

        correct_answers: A number that rises by one when user answers correctly

        health: A number that lowers by one when user answers correctly.
        Can only be 0-3

        gamemode: User's choice of playing with different generations
        and with or without the revision mode
    '''

    def __init__(self, gamertag, gamemode):
        '''Class constructor, creates a new player profile

            Args:
                gamertag: A string of three letters player chooses in
                the gamertag input.

                gamemode: Created in the gamemode class initialization when
                user chooses generations and revision mode.
        '''

        self.gamertag = gamertag
        self.points = 0
        self.correct_answers = 0
        self.health = 3
        self.gamemode = gamemode

    def correct_answer(self):
        '''Adds points to user's score when user gives correct answer.
        Point amount depends on the amount of generations chosen

        Args:
            self

        Returns:
            None
        '''

        point_multiplier = self.gamemode.get_number_of_generations()
        self.points += 50 * point_multiplier
        self.correct_answers += 1

    def incorrect_answer(self):
        '''Takes one heart away from user's health when they give
        wrong answer to the app

        Args:
            self

        Returns:
            None
        '''

        if self.health >= 1:
            self.health -= 1

    def get_health(self):
        '''Return's user's current health

        Args:
            self

        Returns:
            Integer value 1-3
        '''

        return self.health

    def get_gamertag(self):
        '''Return's user's current gamertag

        Args:
            self

        Returns:
            string value of three letters
        '''

        return self.gamertag

    def get_points(self):
        '''Return's user's current points

        Args:
            self

        Returns:
            Integer value depicting user's points
        '''

        return self.points

    def get_correct_answers(self):
        '''Return's the number of times user has answered correctly

        Args:
            self

        Returns:
            Integer value depicting user's correct answers
        '''

        return self.correct_answers

    def get_gamemode(self):
        '''Return's the user's current gamemode object

        Args:
            self

        Returns:
            Gamemode object user is playing with
        '''

        return self.gamemode
