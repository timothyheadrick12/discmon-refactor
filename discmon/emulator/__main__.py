from urllib import request
from pokemon import PokemonEmu, Button
from threading import Thread
from flask import Flask, request, jsonify
import time
import os.path

app = Flask(__name__)


def waitForFile(eventName):
    filePath = "gifs/" + eventName + ".gif"
    while not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
        time.sleep(0.1)
    return jsonify({"fileName": filePath})


@app.route("/r")
def moveRight():
    numSpaces = request.args.get("numspaces", default=1, type=int)
    eventName = gb.moveNumSpacesEvent(Button.RIGHT, numSpaces)
    return waitForFile(eventName)


@app.route("/l")
def moveLeft():
    numSpaces = request.args.get("numspaces", default=1, type=int)
    eventName = gb.moveNumSpacesEvent(Button.LEFT, numSpaces)
    return waitForFile(eventName)


@app.route("/u")
def moveUp():
    numSpaces = request.args.get("numspaces", default=1, type=int)
    eventName = gb.moveNumSpacesEvent(Button.UP, numSpaces)
    return waitForFile(eventName)


@app.route("/d")
def moveDown():
    numSpaces = request.args.get("numspaces", default=1, type=int)
    eventName = gb.moveNumSpacesEvent(Button.DOWN, numSpaces)
    return waitForFile(eventName)


@app.route("/a")
def pressA():
    eventName = gb.pressButtonEvent(Button.A)
    return waitForFile(eventName)


@app.route("/b")
def pressB():
    eventName = gb.pressButtonEvent(Button.B)
    return waitForFile(eventName)


def start():
    app.run()


gb = PokemonEmu()


Thread(target=start).start()  # start the server listener in its own thread
# perform an action by sending http request

gb.emu.load_state(open("saves/start_of_game.state", "rb"))
while True:
    gb.tick()
