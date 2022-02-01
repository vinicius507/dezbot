import logging

LOG = logging.getLogger("disnake")
LOG.setLevel(logging.INFO)
tty_handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s:%(levelname)s:%(name)s: %(message)s"
)
tty_handler.setFormatter(formatter)
LOG.addHandler(tty_handler)
