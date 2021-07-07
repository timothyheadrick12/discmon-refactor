from enum import Enum, auto
from pyboy import PyBoy, WindowEvent
from threading import Thread


class Button(Enum):
    """Enumeration for buttons.

    Button presses, holds, and releases should be done using Game() methods. This allows for selecting button from main.
    """

    A = auto()
    B = auto()
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    SELECT = auto()
    START = auto()


class Game:
    """Game class contains a running emulator and associated methods"""

    def __init__(self):
        self.__interrupt = False
        self.__emu = PyBoy("roms/Pokemon - Red Version (USA, Europe) (SGB Enhanced).gb")
        self.__emu.set_emulation_speed(0)

    def absoluteTick(self):
        """The absoluteTick() method is an uninterruptable tick."""
        self.__emu.tick()

    def tick(self):
        """The tick() method is an interruptable tick."""
        if not self.__interrupt:
            self.absoluteTick()

    def runForTime(self, msec):
        """The runForTime method runs the emulator for a given amount of time. It can be interrupted during this time .

        Args:
            msec (int milliseconds): Number of milliseconds to run the emulator
        """
        for x in range(msec):
            self.tick()

    def manualInterrupt(self):
        """The manualInterrupt() method is a manual method for interrupting the emulator"""
        self.__interrupt = True

    def __manualRestart(self):
        """The manualRestart() method is a manual method for stopping emulator interruption"""
        self.__interrupt = False

    def holdButton(self, button):
        """Hold button on emulator.

        Args:
            button (Button): Button to be held
        """
        self.manualInterrupt()
        if button == Button.A:
            self.__emu.send_input(WindowEvent.PRESS_BUTTON_A)
        elif button == Button.B:
            self.__emu.send_input(WindowEvent.PRESS_BUTTON_B)
        elif button == Button.UP:
            self.__emu.send_input(WindowEvent.PRESS_ARROW_UP)
        elif button == Button.DOWN:
            self.__emu.send_input(WindowEvent.PRESS_ARROW_DOWN)
        elif button == Button.LEFT:
            self.__emu.send_input(WindowEvent.PRESS_ARROW_LEFT)
        elif button == Button.RIGHT:
            self.__emu.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        elif button == Button.START:
            self.__emu.send_input(WindowEvent.PRESS_BUTTON_START)
        elif button == Button.SELECT:
            self.__emu.send_input(WindowEvent.PRESS_BUTTON_SELECT)
        else:
            print("Invalid button value sent to holdButton()")
        self.__manualRestart()

    def releaseButton(self, button):
        """Release button on emulator

        Args:
            button (Button): The button to be released
        """
        if button == Button.A:
            self.__emu.send_input(WindowEvent.RELEASE_BUTTON_A)
        elif button == Button.B:
            self.__emu.send_input(WindowEvent.RELEASE_BUTTON_B)
        elif button == Button.UP:
            self.__emu.send_input(WindowEvent.RELEASE_ARROW_UP)
        elif button == Button.DOWN:
            self.__emu.send_input(WindowEvent.RELEASE_ARROW_DOWN)
        elif button == Button.LEFT:
            self.__emu.send_input(WindowEvent.RELEASE_ARROW_LEFT)
        elif button == Button.RIGHT:
            self.__emu.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
        elif button == Button.START:
            self.__emu.send_input(WindowEvent.RELEASE_BUTTON_START)
        elif button == Button.SELECT:
            self.__emu.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
        else:
            print("Invalid button value sent to holdButton()")
