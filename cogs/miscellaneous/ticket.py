import nextcord
import nextcord.ui 
import nextcord
from nextcord.ext import commands
from nextcord.ui import (
  View,
  Button,
  Select
  )
  
async def ticketCallback(interaction):
  guild = interaction.guild
  role = nextcord.utils.get(guild.roles, name="Operator")
  overwrites = {
      guild.default_role: nextcord.PermissionOverwrite(view_channel=False),
      interaction.user: nextcord.PermissionOverwrite(view_channel=True),
      role: nextcord.PermissionOverwrite(view_channel=True)
  }
  select = Select(options=[
          nextcord.SelectOption(label="Report Bug", emoji="🦟", description="Opens a ticket for bug report", value="01")
          nextcord.SelectOption(label="Report Player", emoji="👾", description="Reports a player for cheating or abusing", value="02")
          nextcord.SelectOption(label="Suggestions", emoji="💬", description="Opens a ticket for your suggestions on the server", value="03")
          nextcord.SelectOption(label="Report Staff", emoji="🎃", description="Opens a ticket to report a staff whenever they abuse", value="04")
          nextcord.SelectOption(label="Application", emoji="📖", description="Opens a ticket for your application", value="05")
    ])
    
    async def BotCallback(interaction):
      if select.value[0] == "01":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
        channel = await guild.create_text_channel(f"{interaction.user.name}#{interaction.user.id}\n's ticket", category=category, overwrites=overwrites)
        embed = nextcord.Embed(description=f"Created ticket for {interaction.user.name} # <#{channel.id}>")
        emrule = nextcord.Embed(
              title="RULES",
              description="HERE ARE THE **RULES** THAT YOU NEED TO OBEY ON YOUR TICKET IN ORDER TO GET A RESPOND",
          )
          emrule.add_field(name)
        await interaction.response.send_message(embed=embed)
        await channel.send(f"<@{interaction.user.id}>")
      elif select.value[0] == "02":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
      elif select.value[0] == "03":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
      elif select.value[0] == "04":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
      elif select.value[0] == "05":
        category = nextcord.utils.get(guild.categories, name="TICKETS")

class Ticket(commands.Cog):
  def __init__(self, client):
    self.client = client
  
def Ticket(client):
  client.add_cog(Ticket)