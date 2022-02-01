import argparse

from dezbot import __version__
from dezbot.bot import Dezbot
from dezbot.log import LOG as _


def main():
    parser = argparse.ArgumentParser(description="Dezbot Discord Bot")
    parser.add_argument("--token", type=str, nargs=1, required=True)
    parser.add_argument("--prefix", type=str, nargs=1, default="!")
    args = parser.parse_args()
    bot = Dezbot(
        token=args.token[0],
        version=__version__,
        command_prefix=args.prefix,
        description="Dezbot Discord Bot",
    )
    bot.run()
