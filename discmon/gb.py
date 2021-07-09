from enum import Enum, auto
from pyboy import PyBoy, WindowEvent
from functools import wraps, partial
from threading import Event, Thread


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

    def __init__(self, game):
        """Constructor for Game object that initializes __interrupt to false and sets_emulation_speed to 2

        Args:
            game (String): path to rom
        """
        self.__interrupt = False
        self.__eventStack = []
        self.__emu = PyBoy(game)
        self.__emu.set_emulation_speed(2)

    def stackEvent(eventFunc):
        """The stackEvent decorator surrounds a given function with interrupts and adds it to the eventStack

        stackEvents should not call other stackEvents. This is counter intuitive as the called event will be added to
        the very back of the eventStack when called

        Args:
            eventFunc (function): Event function that should interrupt running and be added to stack

        Returns:
            function: Decorated function that interrupts emulator when removed from stack
        """

        # This function is the function than runs when popped from the eventStack array with eventStack.pop(x)()
        @wraps(eventFunc)
        def addInterrupts(*args):
            args[0].__interrupt = True
            eventFunc(*args)
            args[0].__interrupt = False

        # This function changes functionality of eventFunc so that it instead adds itself to the evenStack on execution
        @wraps(eventFunc)
        def stacker(*args):
            args[0].__eventStack.append(partial(addInterrupts, *args))

        return stacker

    def absoluteTick(self):
        """The absoluteTick() method is an uninterruptable tick."""
        self.__emu.tick()

    def tick(self):
        """The tick() method is an interruptable tick."""
        if not self.__interrupt:
            # When not interrupted if eventStack is not empty, execute the next event
            if len(self.__eventStack) != 0:
                self.__eventStack.pop(0)()
            self.absoluteTick()

    def runForTicks(self, ticks):
        """The runForTime method runs the emulator for a given amount of time. It cannot be interrupted during this time .

        Args:
            msec (int milliseconds): Number of milliseconds to run the emulator
        """
        for x in range(ticks):
            self.absoluteTick()

    def __holdButton(self, button):
        """Hold button on emulator.

        Args:
            button (Button): Button to be held
        """
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

    def __releaseButton(self, button):
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

    @stackEvent
    def pressButtonEvent(self, button, ticks):
        """(Event) Press a button for the given number of ticks

        Args:
            button (Button): button to be pressed
            ticks (int): Number of ticks to press the button
        """
        self.__holdButton(button)
        self.runForTicks(ticks)
        self.__releaseButton(button)
