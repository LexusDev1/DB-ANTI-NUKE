import nextcord
from nextcord.ext import commands

class MessageDetector(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.message_counter = {}
        self.max_message_count = 90  # Change this to your desired limit

    @commands.Cog.listener()
    async def on_message(self, message: nextcord.Message):
        if message.author.bot:
            return
        
        content = message.content.lower()
        
        if "nudity" in content:
            await message.author.send("Warning: Your account has been flagged for inappropriate content.")
        elif any(keyword in content for keyword in ["pornhub.com", "xnxx.com", "youjizz.com", "dagay.com"]):
            await message.author.send("Warning: Your account has been flagged for sharing NSFW content.")

        if any(keyword in content for keyword in ["discord.gg", "invite.gg"]):
            await message.author.send("Warning: Your account has been flagged for sharing a server invite link.")
            await message.delete()
            return

        if message.author.id not in self.message_counter:
            self.message_counter[message.author.id] = 1
        else:
            self.message_counter[message.author.id] += 1

        if self.message_counter[message.author.id] >= self.max_message_count:
            await message.author.send("Warning: You've been warned for excessive messaging. Please refrain from spamming.")

            if self.message_counter[message.author.id] >= self.max_message_count * 90:
                await message.author.send("Warning: Your account has been flagged for continued excessive messaging (spam).")

def setup(client):
    client.add_cog(MessageDetector(client))
