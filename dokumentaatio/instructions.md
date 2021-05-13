# Instructions

(The app's latest release can be found [HERE](https://github.com/anttinevalainen/ot-harjoitustyo/releases). Download the release by clickin _Source code_.
These instruction in Finnish can be found [HERE](https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/ohjeet.md)

## Starting the app

Before starting the app for the first time, the user needs to install dependencies with command:

```bash
poetry install
```

The app doesn't need oher initiation procedures. Start the app by inputting the following command:

```
poetry run invoke start
```

## Front page

The first view of the app is the front page, where user may choose to move to start a new round, see leaderboards or close the app:

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/frontpage.PNG width="320" height="240">

A new round is started with Play! -button

## Creating your player and gamemode profile

Upon clicking play, the user needs to configure round settings. The user must choose a three-letter gamertag and pick those generations, they wish to play a round with.\
In the view below, user's gamertag will be 'OWO' and the round is started with generations 1, 2, 3, 6, 7 and 8 plus Alolan and Galarian forms.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/gametag.PNG width="320" height="240">

If the user's gamertag isn't valid (Includes numbers or special characters), the app will notify about it.\
The app will also notify, if the user has not chosen any generations.

The profiles (Payer, Gamemode and Pokedex) for a round will be locked with 'Choose!' button. If the choices for generations and gamertag are valid, a 'Play!' button will appear, with which you can launch a round.

In the gamertag view, user may also choose to use the revision mode during the round. Turning the revision mode on helps the user by telling the name of the Pokémon presented on the screen. Revision mode is used to sensor the functionality of the app and how the answering works. When revision is turned on, player may not send their scores to leaderboards.

## Gameplay view

In the main window of the app, the user is presented with a silhouette of randomly chosen Pokémon from the generation(s) they have chosen. The point is to guess and write down the name of the Pokémon in the entry field.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/playpage.PNG width="320" height="240"> <img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/correct.PNG width="320" height="240">

The guess is sent with the '!' button or by pressing enter. The app tells immediately whether the guess is correct or not. The app will also show the picture of the Pokémon after the user has sent their guess. When the answer is presented, also the possible secondary form name is also presented with the Pokémon name

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer1.PNG width="320" height="240"> <img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/wronganswer2.PNG width="320" height="240">

When user's answer is incorrect, they lose one of their three lives presented on the top left corner of the gameplay screen. User may answer wrong three times during one round before game over.

In both cases, whether the user has answered correctly or incorrectly, the game continues with the 'Next!'-button or by pressing enter. If the user still has lives, the app will choose another random Pokémon silhouette for the user to guess. After every guess, the Pokémon presented will be removed from the Pokedex, so same images will not be presented again. However, different secondary forms of the same Pokémon may still be shown. So after showing the 50% forme on Zygarde, the app wil llater during the round also possibly show the 10% Zygarde forme and the complete form of Zygarde.

## Examples of naming of Pokémon and correct answers

Guessing the Pokémon names is not case-sensitive, so using only small or capital letters is allowed. The app won't mind about special characters, spaces or accented letters. This means that when user is presented with Eevee, also 'Ë é    v Ê ë' is considered correct answer. This is because some Pokémon have accents, special characters and spaces in their name and the user's answer is considered correct even if they won't fully know about the usage of these characters.

| Full name                            | Accepted answer       | The info message in the app                          |
| :----:                               |:-----                 | :-----                                               |
| Horsea                               | Horsea                | Correct! It's HORSEA!                                |
| Aegislash (Shield)                   | Aegislash             | Correct! It's Aegislash (Shield)!                    |
| Aegislash (Blade)                    | Aegislash             | Correct! It's Aegislash (Blade)!                     |
| Mega Venusaur                        | Mega Venusaur         | Correct! It's MEGA VENUSAUR!                         |
| Mega Mewtwo (X)                      | Mega Mewtwo           | Correct! It's MEGA MEWTWO (X)!                       |
| Mime Jr.                             | Mime jr               | Correct! It's MIME JR.!                              |
| Mime Jr.                             | mimejr                | Correct! It's MIME JR.!                              |
| Mime Jr.                             | Mime jr.              | Correct! It's MIME JR.!                              |
| Mime Jr.                             | mimejr.               | Correct! It's MIME JR.!                              |
| Mime Jr.                             | Mime.jr.              | Correct! It's MIME JR.!                              |
| Gigantamax gengar                    | Gigantamax Gengar     | Correct! It's GIGANTAMAX GENGAR!                     |
| Alolan Persian                       | Alolan Persian        | Correct! It's ALOLAN PERSIAN!                        |
| Galarian Ponyta                      | Galarian Ponyta       | Correct! It's GALARIAN PONYTA!                       |
| Gigantamax Urshifu (Single Strike)   | Gigantamax Urshifu    | Correct! It's GIGANTAMAX URSHIFU (SINGLE STRIKE)!    |

Some Pokémon have secondary names, which describe special formes within their evolutionary branch (See above table: Gigantamax Urshifu and Aegislash). These names are presented in the correct/incorrect answer message box inside parentheses. These special formes/secondary names should not be included within the guess and for example, when Aegislash silhouette is presented, the guess should only be 'Aegislash'.\

When user has chosen also the mega evolutions, gigantamax forms and/or Alolan and Galarian forms, the guess should contain also the form prefix ('Mega (Pokémon name)', 'Gigantamax (Pokémon name)', 'Alolan (Pokémon name) or Galarian (Pokémon name)') For example, when user is presented with Gigantamax Gengar silhouette, guessing only 'Gengar' is considered as an incorrect answer.

For example Mewtwo and Charizard have to kind of mega evolutions (X and Y). In these cases the app considers both mentions above, meaning the correct answer is just 'Mega Mewtwo' or 'Mega Charizard'

If the guessing seems complicated, I recommend launching a round or two using the revision mode to get the hang of it! :)

## Game Over

When user gives the wrong answer, the three heart on top left corner will turn gray one by one. After the third wrong guess, the round will be considered over. The round is over also if the user has no Pokémon left to guess from.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/hearts.png width="354" height="127">

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/sendhiscore.png width="320" height="240">

If the user has enough points for the leaderboards, the app will mention about this and the user's score is possible to be saved by pressing the 'Send hiscore' button. After this user may choose to play another round with the same gamemode as before or go back to the index page and initialize new generation choices for the next rounds.

If the user hasn't got enough points for the leaderboards, they may choose to restart a round with the 'Try again' button or return to the index.

## Leaderboards
In the front page, by pressing the hiscore button the user may see the top nine players, their points, how many correct answers they got and how many generations they have played the round with.

<img src=https://github.com/anttinevalainen/ot-harjoitustyo/blob/main/dokumentaatio/pictures/hiscores.png width="320" height="240">
