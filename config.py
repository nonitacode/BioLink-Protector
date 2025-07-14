# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

import re

API_ID = "24373333" # Your Telegram API ID
API_HASH = "c8ef87304d6fdd6eb8dacf815353713d" # Your Telegram API Hash
BOT_TOKEN = "8125031749:AAEWr7nnA1llQlLJ02ga0VcFYzrAhQqbaJ8" # Your Bot Token

# MongoDB connection URI
MONGO_URI = "mongodb+srv://bot627668:2bEJ56yJSu7vzLws@cluster0.qbw5van.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DEFAULT_WARNING_LIMIT = 3
DEFAULT_PUNISHMENT = "mute" # Options: "mute", "ban"
DEFAULT_CONFIG = ("warn", DEFAULT_WARNING_LIMIT, DEFAULT_PUNISHMENT)

# Regex pattern to detect URLs in user bios
URL_PATTERN = re.compile(
    r'(https?://|www\.)[a-zA-Z0-9.\-]+(\.[a-zA-Z]{2,})+(/[a-zA-Z0-9._%+-]*)*' #done change here
)
