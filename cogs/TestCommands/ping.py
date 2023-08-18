import nextcord
from nextcord.ext import commands

class Ping(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @nextcord.slash_command()
  async def ping(self, interaction: nextcord.Interaction):
    await interaction.response.send_message("pong!", ephemeral=True)
    
def setup(client):
  client.add_cog(Ping(client))