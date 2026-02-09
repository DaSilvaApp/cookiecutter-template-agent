import logging
import os
from logging.handlers import RotatingFileHandler

from rich.logging import RichHandler

# Need to get the config to the logs from the config file

LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "app.log")

logger = logging.getLogger("app_logger")
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

handler = RotatingFileHandler(LOG_FILE, maxBytes=5_000_000, backupCount=3)
handler.setFormatter(formatter)
logger.addHandler(handler)

console_handler = RichHandler()
logger.addHandler(console_handler)
