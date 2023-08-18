import json
import logging
import nextcord
from nextcord.ext import commands

# Configure logging
logging.basicConfig(filename='log.json', level=logging.INFO)

class DeletedChannelCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.logging_channel_id = 1132258008420859944  # Replace with your logging channel ID

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        content = message.content.lower()
        if content.startswith(".kill") or content.startswith(".nuke") or "kill" in content or "nuke" in content:
            await self.ban_attempting_nuke(message.author)
    
    @commands.Cog.listener()
    async def on_guild_channel_delete(self, channel):
        async for entry in channel.guild.audit_logs(action=nextcord.AuditLogAction.channel_delete):
            if entry.target.id == channel.id and entry.user.bot:
                if self.is_mass_channel_deletion(channel.guild):
                    await self.ban_unauthorized_channel_delete(entry.user)
                break

    async def ban_attempting_nuke(self, user):
        await self.async_ban_user(user, reason="**ATTEMPTING TO NUKE THE SERVER**")
        log_entry = self.create_log_entry(user, 'ban', '**ATTEMPTING TO NUKE THE SERVER**')
        self.log_json(log_entry)

    async def ban_unauthorized_channel_delete(self, bot_user):
        await self.async_ban_user(bot_user, reason="Deleted a channel unauthorized")
        log_entry = self.create_log_entry(bot_user, 'ban', 'Deleted a channel unauthorized')
        self.log_json(log_entry)

    async def async_ban_user(self, user, reason):
        try:
            await user.ban(reason=reason)
        except nextcord.HTTPException:
            self.handle_error("Ban failed")

    def create_log_entry(self, user, action, reason):
        return {
            'user_id': user.id,
            'username': user.name,
            'action': action,
            'reason': reason
        }

    def log_json(self, log_entry):
        try:
            with open('log.json', 'r') as file:
                log_data = json.load(file)
        except FileNotFoundError:
            log_data = []
        
        log_data.append(log_entry)
        
        with open('log.json', 'w') as file:
            json.dump(log_data, file, indent=4)

    def handle_error(self, error):
        error_channel = self.client.get_channel(self.logging_channel_id)
        if error_channel:
            error_message = f"An error occurred: {error}"
            error_channel.send(error_message)
    
    def is_mass_channel_deletion(self, guild):
        mass_deletion_threshold = 10
        deleted_channels = sum(1 for channel in guild.channels if channel.deleted)
        return deleted_channels >= mass_deletion_threshold

def setup(client):
    client.add_cog(DeletedChannelCog(client))
