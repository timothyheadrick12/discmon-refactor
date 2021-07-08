from dc_client import DiscordClient
from gb import Game, Button
from threading import Thread
import time

client = DiscordClient()
# client.run("ODYxOTk4MTEzNzEwOTMxOTY4.YOR8TQ.nkepaU8wSkM_u7EBjXZZqbjd880")


gb = Game()


def test_1():
    while True:
        input("Press enter to input")
        gb.pressButtonEvent(Button.A, 500)


Thread(target=test_1).start()

while True:
    gb.tick()
