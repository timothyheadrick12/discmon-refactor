from gb import Game, Button


class PokemonEmu(Game):
    def __init__(self):
        super().__init__("roms/Pokemon - Red Version (USA, Europe) (SGB Enhanced).gb")

    @Game.stackEvent
    def pressButtonEvent(self, button, ticks):
        """(Event) Press a button for the given number of ticks

        NOTE: A, B, START, and SELECT are read on release in Pokemon

        Args:
            button (Button): button to be pressed
            ticks (int): Number of ticks to press the button
        """
        self.holdButton(button)
        self.runForTicks(ticks)
        self.releaseButton(button)
