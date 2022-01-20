from urllib import request
from pokemon import PokemonEmu, Button
from threading import Thread
from flask import Flask, request

app = Flask(__name__)


@app.route("/r")
def moveRight():
    numSpaces = request.args.get("numspaces", default=1, type=int)
    gb.moveNumSpacesEvent(Button.RIGHT, numSpaces)
    return "Moved right " + str(numSpaces)


@app.route("/l")
def moveLeft():
    numSpaces = request.args.get("numspaces", default=1, type=int)
    gb.moveNumSpacesEvent(Button.LEFT, numSpaces)
    return "Moved left " + str(numSpaces)


@app.route("/u")
def moveUp():
    numSpaces = request.args.get("numspaces", default=1, type=int)
    gb.moveNumSpacesEvent(Button.UP, numSpaces)
    return "Moved up " + str(numSpaces)


@app.route("/d")
def moveDown():
    numSpaces = request.args.get("numspaces", default=1, type=int)
    gb.moveNumSpacesEvent(Button.DOWN, numSpaces)
    return "Moved down " + str(numSpaces)


@app.route("/a")
def pressA():
    gb.pressButtonEvent(Button.A)
    return "Pressed A"


@app.route("/b")
def pressB():
    gb.pressButtonEvent(Button.B)
    return "Pressed B"


def start():
    app.run()


gb = PokemonEmu()


Thread(target=start).start()  # start the server listener in its own thread
# perform an action by sending http request

gb.emu.load_state(open("saves/start_of_game.state", "rb"))
while True:
    gb.tick()
