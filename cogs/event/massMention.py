import nextcord
from nextcord.ext import commands
import asyncio

class AntiNuke(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.mention_threshold = 8  # Number of mentions allowed before triggering
        self.warning_threshold = 10  # Number of warnings before kicking
        self.user_warnings = {}  # Store user warnings
        self.user_cooldowns = {}  # Cooldown for users to prevent spam

    async def remove_warnings(self, user_id):
        await asyncio.sleep(3600)  # Cooldown duration (adjust as needed)
        if user_id in self.user_warnings:
            del self.user_warnings[user_id]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return  # Ignore messages from bots

        content = message.content.lower()

        if message.mentions and len(message.mentions) >= self.mention_threshold:
            author_id = message.author.id
            if author_id not in self.user_warnings:
                self.user_warnings[author_id] = 1
                self.user_cooldowns[author_id] = True
                await self.remove_warnings(author_id)
            else:
                self.user_warnings[author_id] += 1

                if self.user_warnings[author_id] >= self.warning_threshold:
                    user = message.author
                    del self.user_warnings[author_id]
                    del self.user_cooldowns[author_id]

                    if isinstance(user, nextcord.User) or isinstance(user, nextcord.Member):
                        await user.kick(reason="Exceeded mention warning threshold.")
                else:
                    if self.user_cooldowns[author_id]:
                        self.user_cooldowns[author_id] = False
                        await self.remove_warnings(author_id)
                        await message.author.send(f"Warning: Please avoid mass mentions in the server.")

def setup(client):
    client.add_cog(AntiNuke(client))
