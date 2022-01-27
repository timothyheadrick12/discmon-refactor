from gameboy import GameboyEmulator, Button


class PokemonEmu(GameboyEmulator):

    directions = [Button.UP, Button.DOWN, Button.LEFT, Button.RIGHT]

    def __init__(self):
        super().__init__("./roms/Pokemon - Red Version (USA, Europe) (SGB Enhanced).gb")
        self.__direction = Button.UP

    @GameboyEmulator.queueEvent
    def pressButtonEvent(self, button):
        """(Event) Press a button for the given number of ticks

        NOTE: A, B, START, and SELECT are read on release in Pokemon

        Args:
            button (Button): button to be pressed
            ticks (int): Number of ticks to press the button
        """
        self.holdButton(button)
        self.runForTicks(4)
        self.releaseButton(button)
        self.runForTicks(100)

    @GameboyEmulator.queueEvent
    def moveNumSpacesEvent(self, button, spaces):
        """(Event) Move a given number of spaces in a given direction

        NOTE: Holding the button for 4 ticks only moves the player slightly. The ticks after releasing
            let the player travel the rest of the way into a unit.

        Args:
            button (Button): UP, DOWN, LEFT, or RIGHT button corresponding to direction of travel
            spaces (int): How many units to move in a given direction
        """
        if button in self.directions:
            for x in range(spaces):
                self.holdButton(button)
                self.runForTicks(4)
                self.releaseButton(button)
                self.runForTicks(15)
            self.__direction = button
        else:
            print("moveNumSpacesEvent expected directional input!")

    @GameboyEmulator.queueEvent
    def changeDirection(self, button):
        """(Event) Change character to the given direction.

        Args:
            button (Button): UP, DOWN, LEFT, or RIGHT button corresponding to direction
        """
        if button in self.directions:
            self.holdButton(button)
            self.runForTicks(2)
            self.releaseButton(button)
            self.runForTicks(15)
        else:
            print("changeDirection expected directional input!")
