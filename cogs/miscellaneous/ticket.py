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
          nextcord.SelectOption(label="Report Bug", emoji="🦟", description="Opens a ticket for bug report", value="01"),
          nextcord.SelectOption(label="Report Player", emoji="👾", description="Reports a player for cheating or abusing", value="02"),
          nextcord.SelectOption(label="Suggestions", emoji="💬", description="Opens a ticket for your suggestions on the server", value="03"),
          nextcord.SelectOption(label="Report Staff", emoji="🎃", description="Opens a ticket to report a staff whenever they abuse", value="04"),
          nextcord.SelectOption(label="Application", emoji="📖", description="Opens a ticket for your application", value="05")
    ])
    
    async def BotCallback(interaction):
      if select.value[0] == "01":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
        channel = await guild.create_text_channel(f"{interaction.user.name}#{interaction.user.id}\n's ticket", category=category, overwrites=overwrites)
        embed = nextcord.Embed(description=f"Created ticket for {interaction.user.name} # <#{channel.id}>")
        emrule = nextcord.Embed(title="RULES", description="HERE ARE THE RULES IN ORDER TO GET A RESPOND FROM A STAFF")
        emrule.add_field(name="PING ONLY **1** STAFF", value="YOU CAN ONLY PING ONE STAFF IF NO RESPONSE", inline=False)
        emrule.add_field(name="DO NOT MASSPING", value="MASS PINGING IS HIGHLY PROHIBITED AND CAN RESULT INTO NO RESPONSE", inline=False)
        emrule.add_field(name="APPRECIATE THE HELP OF STAFF", value="ALWAYS **THANK** THE STAFF FOR HELPING YOU", inline=False)
        emrule.add_field(name="DO NOT HARASS THE STAFF OR THE RESPONDENT", value="IF WE CAUGHT YOU HARASSING ONE OF OUR STAFF, WE WILL WARN YOU FOR HARASSING ONE", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.followup.send(embed=emrule)
        await channel.send(f"<@{interaction.user.id}>")
      elif select.value[0] == "02":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
        channel = await guild.create_text_channel(f"{interaction.user.name}#{interaction.user.id}\n's ticket", category=category, overwrites=overwrites)
        embed = nextcord.Embed(description=f"Created ticket for {interaction.user.name} # <#{channel.id}>")
        emrule = nextcord.Embed(title="RULES", description="HERE ARE THE RULES IN ORDER TO GET A RESPOND FROM A STAFF")
        emrule.add_field(name="PING ONLY **1** STAFF", value="YOU CAN ONLY PING ONE STAFF IF NO RESPONSE", inline=False)
        emrule.add_field(name="DO NOT MASSPING", value="MASS PINGING IS HIGHLY PROHIBITED AND CAN RESULT INTO NO RESPONSE", inline=False)
        emrule.add_field(name="APPRECIATE THE HELP OF STAFF", value="ALWAYS **THANK** THE STAFF FOR HELPING YOU", inline=False)
        emrule.add_field(name="DO NOT HARASS THE STAFF OR THE RESPONDENT", value="IF WE CAUGHT YOU HARASSING ONE OF OUR STAFF, WE WILL WARN YOU FOR HARASSING ONE", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.followup.send(embed=emrule)
        await channel.send(f"<@{interaction.user.id}>")
      elif select.value[0] == "03":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
        channel = await guild.create_text_channel(f"{interaction.user.name}#{interaction.user.id}\n's ticket", category=category, overwrites=overwrites)
        embed = nextcord.Embed(description=f"Created ticket for {interaction.user.name} # <#{channel.id}>")
        emrule = nextcord.Embed(title="RULES", description="HERE ARE THE RULES IN ORDER TO GET A RESPOND FROM A STAFF")
        emrule.add_field(name="PING ONLY **1** STAFF", value="YOU CAN ONLY PING ONE STAFF IF NO RESPONSE", inline=False)
        emrule.add_field(name="DO NOT MASSPING", value="MASS PINGING IS HIGHLY PROHIBITED AND CAN RESULT INTO NO RESPONSE", inline=False)
        emrule.add_field(name="APPRECIATE THE HELP OF STAFF", value="ALWAYS **THANK** THE STAFF FOR HELPING YOU", inline=False)
        emrule.add_field(name="DO NOT HARASS THE STAFF OR THE RESPONDENT", value="IF WE CAUGHT YOU HARASSING ONE OF OUR STAFF, WE WILL WARN YOU FOR HARASSING ONE", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.followup.send(embed=emrule)
        await channel.send(f"<@{interaction.user.id}>")
      elif select.value[0] == "04":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
        channel = await guild.create_text_channel(f"{interaction.user.name}#{interaction.user.id}\n's ticket", category=category, overwrites=overwrites)
        embed = nextcord.Embed(description=f"Created ticket for {interaction.user.name} # <#{channel.id}>")
        emrule = nextcord.Embed(title="RULES", description="HERE ARE THE RULES IN ORDER TO GET A RESPOND FROM A STAFF")
        emrule.add_field(name="PING ONLY **1** STAFF", value="YOU CAN ONLY PING ONE STAFF IF NO RESPONSE", inline=False)
        emrule.add_field(name="DO NOT MASSPING", value="MASS PINGING IS HIGHLY PROHIBITED AND CAN RESULT INTO NO RESPONSE", inline=False)
        emrule.add_field(name="APPRECIATE THE HELP OF STAFF", value="ALWAYS **THANK** THE STAFF FOR HELPING YOU", inline=False)
        emrule.add_field(name="DO NOT HARASS THE STAFF OR THE RESPONDENT", value="IF WE CAUGHT YOU HARASSING ONE OF OUR STAFF, WE WILL WARN YOU FOR HARASSING ONE", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.followup.send(embed=emrule)
        await channel.send(f"<@{interaction.user.id}>")
      elif select.value[0] == "05":
        category = nextcord.utils.get(guild.categories, name="TICKETS")
        channel = await guild.create_text_channel(f"{interaction.user.name}#{interaction.user.id}\n's ticket", category=category, overwrites=overwrites)
        embed = nextcord.Embed(description=f"Created ticket for {interaction.user.name} # <#{channel.id}>")
        emrule = nextcord.Embed(title="RULES", description="HERE ARE THE RULES IN ORDER TO GET A RESPOND FROM A STAFF")
        emrule.add_field(name="PING ONLY **1** STAFF", value="YOU CAN ONLY PING ONE STAFF IF NO RESPONSE", inline=False)
        emrule.add_field(name="DO NOT MASSPING", value="MASS PINGING IS HIGHLY PROHIBITED AND CAN RESULT INTO NO RESPONSE", inline=False)
        emrule.add_field(name="APPRECIATE THE HELP OF STAFF", value="ALWAYS **THANK** THE STAFF FOR HELPING YOU", inline=False)
        emrule.add_field(name="DO NOT HARASS THE STAFF OR THE RESPONDENT", value="IF WE CAUGHT YOU HARASSING ONE OF OUR STAFF, WE WILL WARN YOU FOR HARASSING ONE", inline=False)
        await interaction.response.send_message(embed=embed, ephemeral=True)
        await interaction.followup.send(embed=emrule)
        await channel.send(f"<@{interaction.user.id}>")
    select.callback = BotCallback
    view = View(timeout=None)
    view.add_item(select )
    await interaction.response.send_message("**CHOOSE** an option below", view=view, ephemeral=True)

class Ticket(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @nextcord.slash_command(description="Opens a ticket")
  
  async def ticket(self, interaction):
    button = Button(label="📥 Create a Ticket", style=nextcord.ButtonStyle.green)
    button.callback = ticketCallback
    view = View(timeout=None)
    view.add_item(button)
    await interaction.response.send_message("Open a ticket below", view=view)
    
    
  
def Ticket(client):
  client.add_cog(Ticket)