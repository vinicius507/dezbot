from disnake.ext.commands import Bot as BotBase


class Dezbot(BotBase):
    """
    Dezbot Discord Bot
    """

    def __init__(self, token: str, version: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.token = token
        self.version = version
        self.status = f"{self.command_prefix}help"

    def run(self) -> None:
        super().run(self.token)

    def on_ready(self):
        print(
            f"Logged in as {self.user.name}#{self.user.discriminator}({self.version})"
        )
