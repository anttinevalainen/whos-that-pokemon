from PIL import Image, ImageTk

def check_answer(pokemon, answer):
    '''Returns a a boolean value of answer correctness.

        Args:
            pokemon_full_name: String value of Pokémon name,
            can be used with special forms and mega/gigantamax evolutions!
            answer: User input from play page

        Returns:
            True: Answer matches with Pokémon name
            False: Answer does not match with Pokémon name
    '''

    correct = False

    answer_correct = ''
    user_answer = ''

    pokemon_name = pokemon.get_name().lower()
    answer = answer.lower()
    if pokemon_name == 'gigantamax flapple' and 'appletun' in answer:
        pokemon.set_name('gigantamax appletun')
        pokemon_name = pokemon.get_name().lower()

    full_name = pokemon.get_full_name().upper()

    for character in pokemon_name:
        if character.isalnum():
            answer_correct += character

    for character in answer:
        if character.isalnum():
            user_answer += character

    if answer_correct == user_answer:
        correct = True

    if len(full_name) > 25:
        full_name_s = full_name.split(' (')
        full_name = full_name_s[0] + '\n(' + full_name_s[1]

    if correct:
        text = "Correct! It's\n" + full_name + '!'
    else:
        text = "Wrong! It's\n" + full_name + '!'

    return correct, text

def get_health_photoimage(player):
    '''returns a photoimage of player's health merged with
    the background.

        Args:
            player: The current Player object

        Returns:
            Photoimage object of user's health as three heart
            symbols merged with a piece of app background
    '''


    heart_fp = 'src/data/png/heart.png'
    noheart_fp = 'src/data/png/noheart.png'
    background_fp = 'src/data/png/health_background.png'

    heart = Image.open(heart_fp).convert('RGBA')
    noheart = Image.open(noheart_fp).convert('RGBA')
    health = Image.open(background_fp).convert('RGBA')

    if player.get_health() == 3:
        health.paste(heart, (0, 0), heart)
        health.paste(heart, (74, 0), heart)
        health.paste(heart, (148, 0), heart)
    elif player.get_health() == 2:
        health.paste(heart, (0, 0), heart)
        health.paste(heart, (74, 0), heart)
        health.paste(noheart, (148, 0), noheart)
    elif player.get_health() == 1:
        health.paste(heart, (0, 0), heart)
        health.paste(noheart, (74, 0), noheart)
        health.paste(noheart, (148, 0), noheart)
    else:
        health.paste(noheart, (0, 0), noheart)
        health.paste(noheart, (74, 0), noheart)
        health.paste(noheart, (148, 0), noheart)

    health_photoimage = ImageTk.PhotoImage(image = health)
    return health_photoimage

def correct_answer(player, pokemon):
    '''Adds points to user's score when user gives correct answer.
        Point amount depends on the amount of generations chosen

        Args:
            self

        Returns:
            None
    '''

    gamemode = player.get_gamemode()
    pokedex = player.get_pokedex()
    point_multiplier = gamemode.get_number_of_generations()

    points = 50 * point_multiplier

    player.raise_points(points)
    player.raise_correct_answers()
    pokedex.erase_pokemon(pokemon)

def incorrect_answer(player, pokemon):
    '''Takes one heart away from user's health when they give
        wrong answer to the app

        Args:
            self

        Returns:
            None
    '''

    player.lower_health()

    pokedex = player.get_pokedex()
    pokedex.erase_pokemon(pokemon)
