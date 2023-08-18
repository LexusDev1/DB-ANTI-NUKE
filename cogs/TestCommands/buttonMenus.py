import nextcord
from nextcord.ext import commands, menus

class MySource(menus.ListPageSource):
    def __init__(self, data):
        super().__init__(data, per_page=4)

    async def format_page(self, menu, entries):
        offset = menu.current_page * self.per_page
        return '\n'.join(f'{i}. {v}' for i, v in enumerate(entries, start=offset))

class buttonMenus(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pages_example(self, ctx):
        data = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        pages = menus.ButtonMenuPages(
            source=MySource(data),
            clear_buttons_after=True,
            style=nextcord.ButtonStyle.primary,
        )
        await pages.start(ctx)

def setup(client):
    client.add_cog(buttonMenus(client))
    