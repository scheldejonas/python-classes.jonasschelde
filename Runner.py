from Classes import *

import random


# Add - couple of pirates
pirates = Pirates()

pirates.push_pirate(
    name = "Peter",
    gender = "He"
)

pirates.push_pirate(
    name = "Anders",
    gender = "He"
)

pirates.push_pirate(
    name = "Søren",
    gender = "He"
)

pirates.push_pirate(
    name = "Gurli",
    gender = "She"
)

pirates.push_pirate(
    name = "Mille",
    gender = "She"
)

pirates.push_pirate(
    name = "Lars",
    gender = "He"
)

pirates.push_pirate(
    name = "Hans",
    gender = "He"
)

pirates.push_pirate(
    name = "Kirsten",
    gender = "She"
)

pirates.push_pirate(
    name = "Maria",
    gender = "She"
)

pirates.push_pirate(
    name = "Lis",
    gender = "She"
)

pirates.push_pirate(
    name = "Taylor",
    gender = "He"
)

# Start - the party
pirates.start_the_game()

pirates.print_pirates()


# Continue - picking random pirate, until empyt
while pirates._pirate_counter > 1 :

    print()

    print("Who is gonna be the next one !?")

    print(pirates._current_pirate._name + " is rolling the dice")

    i = 0

    random_number = random.randint(0, 6)

    print( pirates._current_pirate._gender + " rolled: " + str(random_number) )

    for i in range(0, random_number ):

        pirates.move_to_next_pirate()


    pirates.pull_current_pirate()

    print()

    if ( pirates._pirate_counter > 1 ):

        print("We have now " + str(pirates._pirate_counter) + " pirates left in the game:")

        pirates.print_pirates()


# End - the game
print()

print("congratulations !")

print()

print(pirates._current_pirate._name + " you have won the ship.")

print()

print("Now - Go rule the seas.")