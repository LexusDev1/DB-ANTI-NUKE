import nextcord
from nextcord.ext import commands

class Say(commands.Cog):
    def __init__(self, client):
        self.client = client

    @nextcord.slash_command()
    async def say(self, interaction: nextcord.Interaction, options: str = nextcord.SlashOption(description="Choose the bot message to say", choices=["hi", "hey"])):
        if options == "hi":
            await interaction.response.send_message("Hi", ephemeral=True)
        elif options == "hey":
            await interaction.response.send_message("Hey", ephemeral=True)

def setup(client):
    client.add_cog(Say(client))
