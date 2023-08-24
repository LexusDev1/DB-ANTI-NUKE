import nextcord, databases, dislevel, os, yaml, asyncio
from colorama import Fore
from nextcord.ext import commands


with open("storage/configs/yaml/configs.yml", "r") as Discord:
    Configuration = yaml.safe_load(Discord)

TOKEN = Configuration['Discord']['TOKEN']
PREFIX = Configuration['Discord']['PREFIX']
CLIENT_ID = Configuration['SPOTIFY']['CLIENT_ID']
CLIENT_SECRET = Configuration['SPOTIFY']['CLIENT_SECRET']
HOST = Configuration['LAVALINK']['HOST']
PASSWORD = Configuration['LAVALINK']['PASSWORD']
PORT = Configuration['LAVALINK']['PORT']

intents = nextcord.Intents.default()
intents.typing = False
intents.presences = False
intents.message_content = True
intents.members = True
client = commands.Bot(command_prefix=PREFIX, intents=intents, case_insensitive=False)

async def is_event_cog(cog):
    try:
        cog_class = cog.split('.')[-1]
        cog_path_parts = cog.split('.')
        return (
            hasattr(__import__(cog, fromlist=[cog_class]), cog_class)
            and issubclass(getattr(__import__(cog, fromlist=[cog_class]), cog_class), commands.Cog)
            and "event" in cog_path_parts
        )
    except (AttributeError, ImportError):
        return False

async def load_cogs():
    for folder_name in os.listdir("./cogs"):
        if os.path.isdir(f"./cogs/{folder_name}"):
            for filename in os.listdir(f"./cogs/{folder_name}"):
                if filename.endswith(".py"):
                    try:
                        cog_path = f"cogs.{folder_name}.{filename[:-3]}"
                        is_event = await is_event_cog(cog_path)
                        if is_event:
                            print(Fore.GREEN + f"Loaded Event Cog: {cog_path}")
                        else:
                            print(Fore.YELLOW + f"Loaded Cog: {cog_path}")
                        client.load_extension(cog_path)
                        if folder_name == "__pycache__":
                          os.system(f"rm -rf {folder_name}")
                    except Exception as e:
                        print(f"Failed to load cog {cog_path}: {e}")

async def main():
    print(Fore.YELLOW + "Loading cogs...")
    await load_cogs()
    await client.start(TOKEN)
    async with bot.db.cursor() as cursor:
        await cursor.execute("CREATE TABLE IF NOT EXISTS dblevel (level INTEGER, xp INTEGER, user, INTEGER, guild INTEGER)")

asyncio.run(main())
