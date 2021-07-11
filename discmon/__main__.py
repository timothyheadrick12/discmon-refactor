from dc_client import DiscordClient
from pokemon import PokemonEmu, Button
from threading import Thread

client = DiscordClient()
# client.run("ODYxOTk4MTEzNzEwOTMxOTY4.YOR8TQ.nkepaU8wSkM_u7EBjXZZqbjd880")


gb = PokemonEmu()


def test_1():
    while True:
        letter = input("Press enter to input")

        if letter == "L":
            gb.emu.load_state(open("saves/start_of_game.state", "rb"))
        if letter in ("1", "2", "3", "4"):
            gb.moveNumSpacesEvent(Button.LEFT, int(letter))
        if letter in ("5", "6", "7", "8"):
            gb.moveNumSpacesEvent(Button.UP, int(letter))
        if letter == "r":
            gb.changeDirection(Button.RIGHT)


Thread(target=test_1).start()

gb.emu.load_state(open("saves/start_of_game.state", "rb"))
while True:
    gb.tick()
