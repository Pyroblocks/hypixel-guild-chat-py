import os
from dotenv import load_dotenv

# The prefix the bot responds to for commands
PREFIX = '!'
# Emojis the bot should use for certain events
EMOJIS = {
    'DISCORD': '<:Discord:925509254922784788>',  # When a message is sent from Discord
    'HYPIXEL': '<:Hypixel:925509305535451176>',  # When a message is sent from Hypixel
    'JOIN': '<:Join:925509255304478720>',  # When a member joins Hypixel
    'LEAVE': '<:Leave:925509255128301626>'  # When a member leaves Hypixel
}
# List of Owner IDs (to use commands like sumo)
OWNER_IDS = [721089849653985421,764197585173872671]


# Don't touch this unless you know what you're doing
load_dotenv()
TOKEN = os.getenv("TOKEN")
GUILD_CHAT_CHANNEL = int(os.getenv("GUILD_CHAT_CHANNEL"))
MINECRAFT_EMAIL = os.getenv("MINECRAFT_EMAIL")
MINECRAFT_PASSWORD = os.getenv("MINECRAFT_PASSWORD")
