<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/playpage.PNG width="320" height="240">

*[README.md in Finnish](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/README.md)*

# Who's that Pokémon -recognition app

Who's that Pokémon is an app to mimic the picture quizes presented in the traditional Pokémon anime.

The purpose of the app is to recognise the Pokémon shown on the screen based only by it's black silhouette and input said Pokémon's name in the entry field. The user gets points from each correct answer based on how many evolutions the round is played with.

There are not only every Pokémon from generations 1-8, but also mega evolutions, gigantamax forms and Galarian and Alolan forms. The player has a total of 12 generations/form types to choose from. In total the user can start a round with 1085 Pokémon to recognise.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer1.PNG width="320" height="240"> <img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer2.PNG width="320" height="240">

Main purpose of the app is to memorise Pokémon names but it may also be considered a game.\
\
Each round ends when the user inputs wrong answer three times during the round or when the Pokedex of user's generation choices is empty. After a round, if the user has enough points, they are able to send their score and gamertag to the leaderboards. 

The app is created and tested with Python version 3.9.2.

## Releases

- *[Release 1](https://github.com/anttinevalainen/ot-harjoitustyo/releases/tag/Viikko5)*
- *[Release 2](https://github.com/anttinevalainen/ot-harjoitustyo/releases/tag/Viikko6)*
- *[Final release](https://github.com/anttinevalainen/ot-harjoitustyo/releases/tag/FinalRelease)*

## Instructions to use the app

- *[Instructions in English](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/instructions.md)*
- *[Instructions in Finnish](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/ohjeet.md)*

## Installation

The commands below require Poetry to function.\
[Poetry installation](https://python-poetry.org/docs/#installation)


1. Dependencies are installed by inputting the following command in the app's root directory:

```bash
poetry install
```

2. Now the app can be started with following command:

```bash
poetry run invoke start
```


## Testing

The app tests may be run through with command:

```bash
poetry run invoke test
```

## HTML Test coverage report

Generate the HTML coverage report with command:

```bash
poetry run invoke coverage-report
```
This creates a 'htmlcov' folder in the root directory

### Pylint

Run Pylint with command:

```bash
poetry run invoke lint
```
