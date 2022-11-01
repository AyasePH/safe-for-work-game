# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Tri")


# The game starts here.

label start:

    scene bg
    show hentai
    with fade
    e "Greeting fellow degenerate"
    e "I am the creator of this game"
    e "and i presented you with choice for you"
    e "And i also think i know which you gona pick"
menu:
    "Censored":
        jump sfw
    "Uncensored":
        jump nsfw



label sfw:

    hide hentai
    scene sus
    e "wtf bro"

    return

label nsfw:

    e "of course you pick this"

    return
