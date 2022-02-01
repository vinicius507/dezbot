from datetime import datetime as dt

import disnake
from disnake.ext import commands
from disnake.ext.commands import Cog

from dezbot.bot import Dezbot


class AdminCommands(Cog):
    """
    Administration commands COG
    """

    def __init__(self, bot: Dezbot) -> None:
        super().__init__()
        self.bot = bot

    @commands.slash_command(
        name="status",
        description="Pega o status do Dezbot",
    )
    async def status(self, inter: disnake.ApplicationCommandInteraction):
        """
        Comando para imprimir o status do Dezbot
        """
        embed = disnake.Embed(title="Dezbot Status", type="rich")
        embed.set_thumbnail(
            url=self.bot.user.avatar.url
            if self.bot.user.avatar is not None
            else None
        )
        embed.add_field(
            name="Version", value=f"v{self.bot.version}", inline=False
        )
        embed.add_field(name="Environment", value="Dev")
        embed.add_field(
            name="Latency", value="{:.2}s".format(self.bot.latency)
        )
        embed.set_footer(text=f"{dt.now()}")
        await inter.send(embed=embed, ephemeral=True)


def setup(bot: Dezbot):
    bot.add_cog(AdminCommands(bot=bot))
