import nextcord
from nextcord.ext import commands
import datetime
import os
import json

class memberChecker(commands.Cog):
    def __init__(self, client):
        self.client = client

    async def cog_check(self, ctx):
        return ctx.guild is not None  # Only apply these checks in a guild context

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        join_date = member.joined_at.replace(tzinfo=None)  # Convert to offset-naive datetime
        current_date = datetime.datetime.now()
        days_difference = (current_date - join_date).days
        
        if member.bot:
            await member.guild.ban(member, reason="Bot detected on join.")
        else:
            config_data = await self.load_configuration()
            age_requirement = config_data.get("age")

            if age_requirement is None:
                await member.send(embed=await self.get_age_requirement_embed(None))
                await member.kick(reason="Account does not meet age requirement.")
            elif days_difference < age_requirement:
                await member.send(embed=await self.get_age_requirement_embed(age_requirement))
                await member.kick(reason="Account does not meet age requirement.")
            else:
                await member.send(embed=await self.get_welcome_embed())

    @nextcord.slash_command(description="Sets the value of dates and age")
    async def configuration(self, interaction: nextcord.Interaction, *, date=None, age=None, channel_id=None):
        if not date and not age and channel_id is None:
            await interaction.response.send_message("Please provide the 'date', 'age', or 'channel_id' parameter.", ephemeral=True)
            return

        config_data = await self.load_configuration()

        if date:
            config_data["date"] = date

        if age:
            config_data["age"] = int(age)  # Convert age to an integer
        
        if channel_id:
            config_data["config_channel_id"] = int(channel_id)  # Convert channel_id to an integer

        await self.save_configuration(config_data)
        await self.update_configuration_embed()

        await interaction.response.send_message("Configuration updated successfully.", ephemeral=True)

    async def load_configuration(self):
        config_file = "./configuration.json"
        config_data = {}

        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                config_data = json.load(f)

        return config_data

    async def save_configuration(self, config_data):

        with open("./configuration.json", "w") as f:
            json.dump(config_data, f, indent=4)

    async def update_configuration_embed(self):
        config_data = await self.load_configuration()
        age_requirement = config_data.get("age")
        date = config_data.get("date")
        self.config_channel_id = config_data.get("config_channel_id")  # Update self.config_channel_id
        
        if age_requirement is not None:
            embed = await self.get_age_requirement_embed(age_requirement)
            await self.update_embed_message(embed, date)

    async def update_embed_message(self, embed, date):
        channel = self.client.get_channel(self.config_channel_id)
        
        if channel:
            async for message in channel.history(limit=10):  # Adjust limit as needed
                if message.author == self.client.user and message.embeds:
                    old_embed = message.embeds[0]
                    
                    # Update the embed with new information
                    if embed.title:
                        old_embed.title = embed.title
                    if embed.description:
                        old_embed.description = embed.description
                    if embed.color:
                        old_embed.color = embed.color
                    if embed.footer:
                        old_embed.set_footer(text=embed.footer.text)
                    
                    await message.edit(embed=old_embed)

    async def get_age_requirement_embed(self, age_requirement):
        embed = nextcord.Embed(
            title="Account Kicked",
            description="Your account has been kicked due to not meeting the age requirement.",
            color=0xFF0000
        )
        if age_requirement is not None:
            embed.set_footer(text=f"Age requirement: {age_requirement} days")
        return embed

    async def get_welcome_embed(self):
        embed = nextcord.Embed(
            title="Welcome to the Server!",
            description="Thanks for joining! Enjoy your stay.",
            color=0x00FF00
        )
        return embed

def setup(client):
    client.add_cog(memberChecker(client))
