from disnake.ext.commands import Bot as BotBase


class Dezbot(BotBase):
    """
    Dezbot Discord Bot
    """

    def __init__(
        self, token: str, command_prefix: str, version: str, *args, **kwargs
    ):
        super().__init__(
            status=f"{command_prefix}help",
            command_prefix=command_prefix,
            *args,
            **kwargs,
        )
        self.token = token
        self.version = version

    def run(self) -> None:
        super().run(self.token)

    async def on_ready(self):
        print(
            f"Logged in as {self.user.name}#{self.user.discriminator}(v{self.version})"
        )
