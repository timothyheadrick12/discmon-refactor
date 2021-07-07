import discord


class DiscordClient(discord.Client):
    async def on_ready(self):
        """The on_ready() function prints to console when bot has connected to server."""

        print("We have logged in as {0.user}".format(self))
