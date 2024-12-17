import threading
from flask import Flask
import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from ERAVIBES import LOGGER, app, userbot
from ERAVIBES.core.call import ERA
from ERAVIBES.misc import sudo
from ERAVIBES.plugins import ALL_MODULES
from ERAVIBES.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "ERAVIBES Bot is running !"

async def init_bot():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("✦ Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except Exception as e:
        LOGGER("ERAVIBES").error(f"Error loading banned users: {e}")

    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"ERAVIBES.plugins.{all_module}")
    LOGGER("ERAVIBES.plugins").info("✦ Successfully Imported Modules...💞")
    await userbot.start()
    await ERA.start()
    try:
        await ERA.stream_call("https://te.legra.ph/file/29f784eb49d230ab62e9e.mp4")
    except NoActiveGroupCall:
        LOGGER("ERAVIBES").error(
            "✦ Please turn on the videochat of your log group/channel.\n\n✦ Stopping Bot...💣"
        )
        exit()
    except Exception as e:
        LOGGER("ERAVIBES").error(f"Error starting ERA stream: {e}")

    await ERA.decorators()
    LOGGER("ERAVIBES").info(
        "✦ Created By ➥ The Rishu...🐝"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("ERAVIBES").info("❖ Stopping Rishu Music Bot...💌")

def run_flask():
    flask_app.run(host="0.0.0.0", port=8000)

if __name__ == "__main__":
    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    asyncio.run(init_bot())
