from enum import Enum, auto
from pyboy import PyBoy, WindowEvent
from functools import wraps, partial
import sys


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

    __captureRate = 1  # Ticks per capture for imageBuffer
    __eventSmoothing = 25  # Ticks around events saved to imageBuffer for smoothing gifs

    def __init__(self, game):
        """Constructor for Game object

        Args:
            game (String): path to rom
        """
        self.__interrupt = False
        self.__eventStack = []
        self.__imageBuffer = []
        self.__tickCounter = 0
        self.emu = PyBoy(game)
        self.__screen = self.emu.botsupport_manager().screen()
        self.emu.set_emulation_speed(0)

    def stackEvent(eventFunc):
        """The stackEvent decorator surrounds a given function with interrupts and adds it to the eventStack

        stackEvents should not call other stackEvents. This is counter intuitive as the called event will be added to
        the very back of the eventStack when called. stackEvents all are saved as gifs in the gif directory after execution

        TODO: Implement event priorities so that one event can overtake another.
        TODO: Implement events tacking a tick function as an argument for ticks to have custom behavior while running that event.

        Args:
            eventFunc (function): Event function that should interrupt running and be added to stack

        Returns:
            function: Decorated function that interrupts emulator when removed from stack
        """
        eventFunc.__executions = 0  # Any events should have there executions tracked so this member variable is added

        # This function is the function than runs when popped from the eventStack array with eventStack.pop(x)()
        @wraps(eventFunc)
        def addInterrupts(*args, **kwargs):
            eventFunc.__executions += 1
            args[0].__interrupt = True

            # event with event smoothing added
            args[0].runForTicks(args[0].__eventSmoothing)
            eventFunc(*args)
            args[0].runForTicks(args[0].__eventSmoothing)

            args[0].saveGifFromBuffer(
                args[0].__imageBuffer,
                name=eventFunc.__name__ + str(eventFunc.__executions),
            )  # every event executed will be saved as a gif in the gifs directory

            args[0].__interrupt = False

        # This function changes functionality of eventFunc so that it instead adds itself to the evenStack on execution
        @wraps(eventFunc)
        def stacker(*args, **kwargs):
            args[0].__eventStack.append(partial(addInterrupts, *args, **kwargs))

        return stacker

    def __absoluteTick(self):
        """The absoluteTick() method is an uninterruptable tick.
        It adds PIL images to the __imageBuffer"""
        self.emu.tick()
        self.__tickCounter += 1
        if self.__tickCounter % self.__captureRate == 0:
            self.__imageBuffer.append(self.__screen.screen_image())

    def tick(self):
        """The tick() method is an interruptable tick."""
        if not self.__interrupt:
            # When not interrupted if eventStack is not empty, execute the next event
            if len(self.__eventStack) != 0:
                self.__eventStack.pop(0)()
            self.emu.tick()
            self.__tickCounter += 1

    def runForTicks(self, ticks):
        """The runForTime method runs the emulator for a given amount of time. It cannot be interrupted during this time .

        Args:
            msec (int milliseconds): Number of milliseconds to run the emulator
        """
        for x in range(ticks):
            self.__absoluteTick()

    def saveGifFromBuffer(
        self,
        buffer,
        name="untitled",
        saveLocation="gifs/",
        msPerFrame=20,  # this is "real time" so it should be used
        loops=0,  # loops of 0 makes it infinite
        minLengthms=500,
    ):
        """The saveGifFromBuffer function takes a list of PIL objects and and saves them to a gif.
        This is intended to be used to save gifs of events being executed.

        Args:
            buffer (list<PIL>): Buffer of PIL images to be converted to gif
            name (str, optional): Name of the gif file. Defaults to "untitled".
            saveLocation (str, optional): Save location of the gif file. Defaults to "gifs/".
            msPerFrame (int, optional): How many milliseconds an image displays on the gif. Defaults to 20.
            loops (int, optional): How many times the gif should loop when opened. Defaults to 0, which is infinite.
            minLengthms (int, optional): The minimum length of the gif in milliseconds.
        """
        if len(buffer) > 1:
            buffer.pop(0).save(
                saveLocation + name + ".gif",
                save_all=True,
                append_images=buffer,
                optimize=True,
                duration=(
                    msPerFrame
                    if ((len(buffer) + 1) * msPerFrame >= minLengthms)
                    else (minLengthms // (len(buffer) + 1))
                ),
                loop=loops,
            )
            buffer.clear()  # clears the list passed to the function
        else:
            print("Buffer is empty! Cannot save gif.")

    def holdButton(self, button):
        """Hold button on emulator.

        Args:
            button (Button): Button to be held
        """
        if button == Button.A:
            self.emu.send_input(WindowEvent.PRESS_BUTTON_A)
        elif button == Button.B:
            self.emu.send_input(WindowEvent.PRESS_BUTTON_B)
        elif button == Button.UP:
            self.emu.send_input(WindowEvent.PRESS_ARROW_UP)
        elif button == Button.DOWN:
            self.emu.send_input(WindowEvent.PRESS_ARROW_DOWN)
        elif button == Button.LEFT:
            self.emu.send_input(WindowEvent.PRESS_ARROW_LEFT)
        elif button == Button.RIGHT:
            self.emu.send_input(WindowEvent.PRESS_ARROW_RIGHT)
        elif button == Button.START:
            self.emu.send_input(WindowEvent.PRESS_BUTTON_START)
        elif button == Button.SELECT:
            self.emu.send_input(WindowEvent.PRESS_BUTTON_SELECT)
        else:
            print("Invalid button value sent to holdButton()")

    def releaseButton(self, button):
        """Release button on emulator

        Args:
            button (Button): The button to be released
        """
        if button == Button.A:
            self.emu.send_input(WindowEvent.RELEASE_BUTTON_A)
        elif button == Button.B:
            self.emu.send_input(WindowEvent.RELEASE_BUTTON_B)
        elif button == Button.UP:
            self.emu.send_input(WindowEvent.RELEASE_ARROW_UP)
        elif button == Button.DOWN:
            self.emu.send_input(WindowEvent.RELEASE_ARROW_DOWN)
        elif button == Button.LEFT:
            self.emu.send_input(WindowEvent.RELEASE_ARROW_LEFT)
        elif button == Button.RIGHT:
            self.emu.send_input(WindowEvent.RELEASE_ARROW_RIGHT)
        elif button == Button.START:
            self.emu.send_input(WindowEvent.RELEASE_BUTTON_START)
        elif button == Button.SELECT:
            self.emu.send_input(WindowEvent.RELEASE_BUTTON_SELECT)
        else:
            print("Invalid button value sent to holdButton()")

    @stackEvent
    def pressButtonEvent(self, button, ticks):
        """(Event) Press a button for the given number of ticks

        Args:
            button (Button): button to be pressed
            ticks (int): Number of ticks to press the button
        """
        self.holdButton(button)
        self.runForTicks(ticks)
        self.releaseButton(button)
