from io import FileIO
import discord
from pokemon import PokemonEmu, Button
from math import isnan
from threading import Thread
import asyncio
import time
import os.path


class DiscordClient(discord.Client):
    def __init__(self, *, gb, **options):
        super().__init__(**options)
        self.gb = gb

    async def on_ready(self):
        """The on_ready() function prints to console when bot has connected to server."""

        print("We have logged in as {0.user}".format(self))

    async def on_message(self, message):
        """Handles recieving messages or in other words, commands.

        NOTE: This should probably be seperated into multiple functions or it will grow giant

        Args:
            message (Message): The message object that was recieved
        """

        if message.author == self.user:  # ignore self messages
            return
        messageArgs = message.content.split()
        if messageArgs[0] == "$move":
            # If the message is a move command handle it. Needs to be tested more
            if messageArgs[1] == "w" or messageArgs[1] == "up":
                if len(messageArgs) >= 3 and (not (isnan(int(messageArgs[2])))):
                    eventName = self.gb.moveNumSpacesEvent(
                        Button.UP, int(messageArgs[2])
                    )
                else:
                    eventName = self.gb.moveNumSpacesEvent(Button.UP, 1)
                filePath = "gifs/" + eventName + ".gif"
                while not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
                    time.sleep(0.1)
                await message.channel.send(
                    file=discord.File("gifs/" + eventName + ".gif")
                )
            elif messageArgs[1] == "a" or messageArgs[1] == "left":
                if len(messageArgs) >= 3 and (not (isnan(int(messageArgs[2])))):
                    eventName = self.gb.moveNumSpacesEvent(
                        Button.LEFT, int(messageArgs[2])
                    )
                else:
                    eventName = self.gb.moveNumSpacesEvent(Button.LEFT, 1)
                filePath = "gifs/" + eventName + ".gif"
                while not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
                    time.sleep(0.1)
                await message.channel.send(
                    file=discord.File("gifs/" + eventName + ".gif")
                )
            elif messageArgs[1] == "s" or messageArgs[1] == "down":
                if len(messageArgs) >= 3 and (not (isnan(int(messageArgs[2])))):
                    eventName = self.gb.moveNumSpacesEvent(
                        Button.DOWN, int(messageArgs[2])
                    )
                else:
                    eventName = self.gb.moveNumSpacesEvent(Button.DOWN, 1)
                filePath = "gifs/" + eventName + ".gif"
                while not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
                    time.sleep(0.1)
                await message.channel.send(file=discord.File(filePath))
            elif messageArgs[1] == "d" or messageArgs[1] == "right":
                if len(messageArgs) >= 3 and (not (isnan(int(messageArgs[2])))):
                    eventName = self.gb.moveNumSpacesEvent(
                        Button.RIGHT, int(messageArgs[2])
                    )
                else:
                    eventName = self.gb.moveNumSpacesEvent(Button.RIGHT, 1)
                filePath = "gifs/" + eventName + ".gif"
                while not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
                    time.sleep(0.1)
                await message.channel.send(
                    file=discord.File("gifs/" + eventName + ".gif")
                )
            else:
                await message.channel.send(
                    "Invalid command format try: $move (direction) (numSpaces)"
                )
        elif messageArgs[0] == "$press":
            # If the message is a press command handle it. Needs to be tested more
            if messageArgs[1] == "a" or messageArgs[1] == "A":
                eventName = self.gb.pressButtonEvent(Button.A)
                filePath = "gifs/" + eventName + ".gif"
                while not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
                    time.sleep(0.1)
                await message.channel.send(
                    file=discord.File("gifs/" + eventName + ".gif")
                )
            elif messageArgs[1] == "b" or messageArgs[1] == "B":
                eventName = self.gb.pressButtonEvent(Button.B)
                filePath = "gifs/" + eventName + ".gif"
                while not os.path.exists(filePath) or os.path.getsize(filePath) == 0:
                    time.sleep(0.1)
                await message.channel.send(
                    file=discord.File("gifs/" + eventName + ".gif")
                )
                print("bird")
            else:
                await message.channel.send(
                    "Invalid command format try: $move (direction) (numSpaces)"
                )


class Threader(Thread):
    """This runs the discord bot in its own thread.

    NOTE: I don't know how it works so I should read up on it
    https://www.codependentcodr.com/asyncio-you-are-a-complex-beast.html
    """

    def __init__(self, gb):
        Thread.__init__(self)
        self.loop = asyncio.get_event_loop()
        self.gb = gb
        self.start()

    async def starter(self):
        self.discord_client = DiscordClient(gb=self.gb)
        await self.discord_client.start(
            "ODYxOTk4MTEzNzEwOTMxOTY4.YOR8TQ.nkepaU8wSkM_u7EBjXZZqbjd880"
        )

    def run(self):
        self.name = "Discord.py"

        self.loop.create_task(self.starter())
        self.loop.run_forever()
