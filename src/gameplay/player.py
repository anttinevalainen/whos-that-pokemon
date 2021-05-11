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

    def __init__(self, gamertag, gamemode, pokedex):
        '''Class constructor, creates a new player profile

            Args:
                gamertag: A string of three letters player chooses in
                the gamertag input.

                gamemode: Created in the gamemode class initialization when
                user chooses generations and revision mode.
        '''

        self.gamertag = gamertag
        self.gamemode = gamemode
        self.pokedex = pokedex

        self.points = 0
        self.correct_answers = 0
        self.health = 3


    def get_health(self):
        '''Return's user's current health

        Args:
            self

        Returns:
            Integer value 1-3
        '''

        return self.health

    def lower_health(self):
        '''Lowers user's health by one until zero

        Args:
            self

        Returns:
            None
        '''

        if self.health > 0:
            self.health -= 1

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

    def raise_points(self, amount):
        '''Raises users points with given amount

        Args:
            self
            amount: Integer value of how many points score is raised with

        Returns:
            None
        '''

        self.points += amount

    def raise_correct_answers(self):
        '''Raises users correct answers with one

        Args:
            self

        Returns:
            None
        '''

        self.correct_answers += 1

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

    def get_pokedex(self):
        '''Return's the user's current pokedex object

        Args:
            self

        Returns:
            pokedex object user is playing with
        '''

        return self.pokedex
