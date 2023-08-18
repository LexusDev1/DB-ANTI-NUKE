import nextcord
from nextcord.ext import commands
import datetime

class memberChecker(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member: nextcord.Member):
        join_date = member.joined_at.replace(tzinfo=None)  # Convert to offset-naive datetime
        current_date = datetime.datetime.now()
        days_difference = (current_date - join_date).days
        
        if member.bot:
            await member.guild.ban(member, reason="Bot detected on join.")
        else:
            if days_difference < 50:
                embed = nextcord.Embed(
                    title="Account Kicked",
                    description="Your account has been kicked due to a recent join date.",
                    color=0xFF0000
                )
                await member.send(embed=embed)
                await member.kick(reason="Join date is too recent.")
            else:
                embed = nextcord.Embed(
                    title="Welcome to the Server!",
                    description="Thanks for joining! Enjoy your stay.",
                    color=0x00FF00
                )
                await member.send(embed=embed)

def setup(client):
    client.add_cog(memberChecker(client))
