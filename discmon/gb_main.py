from pyboy import PyBoy, WindowEvent
from threading import Thread

class Game:

    emu = PyBoy('roms/Pokemon - Red Version (USA, Europe) (SGB Enhanced).gb')
    awaitingInput = False
    pressedKey = ""

    def trackKeys():
        while(True):
            if(not Game.awaitingInput):
                Game.pressedKey = input("Enter a key: ")
                if(Game.pressedKey == "a"):
                    Game.awaitingInput = True
                if(Game.pressedKey == "s"):
                    Game.awaitingInput = True

    def __init__(self):
        Thread(target = Game.trackKeys).start()
        while(True):
            if(Game.awaitingInput):
                if(Game.pressedKey == "a"):
                    Game.emu.send_input(WindowEvent.PRESS_BUTTON_A)
                Game.awaitingInput = False
            Game.emu.tick()
            if(len(Game.emu.get_input()) != 0):
                Game.emu.send_input(WindowEvent.RELEASE_BUTTON_A)



Game()