import nextcord
from nextcord.ext import commands

class LockDown(commands.Cog):
  def __init__(self, client):
    self.client = client
    
  @nextcord.slash_command(description="Toggles the channel on lock")
  async def lock(self, interaction, *, channel: nextcord.TextChannel = None, mode=None):
    if channel == None:
        em = nextcord.Embed(description="Please! Provide the channel")
        await interaction.send(embed=em, ephemeral=True)
    overwrite = channel.overwrites_for(interaction.guild.default_role)
    overwrite.send_messages = False
    await channel.set_permissions(interaction.guild.default_role, overwrite=overwrite)
    
def setup(client):
  client.add_cog(LockDown(client))