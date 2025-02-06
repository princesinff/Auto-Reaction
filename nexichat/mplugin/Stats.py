import asyncio
import logging
import random
import time
import psutil
import config
import os
from nexichat import _boot_
from nexichat import get_readable_time
from nexichat import nexichat
from datetime import datetime
from pymongo import MongoClient
from pyrogram.enums import ChatType
from pyrogram import Client, filters
from nexichat import db
from config import OWNER_ID, MONGO_URL, OWNER_USERNAME
from pyrogram.errors import FloodWait, ChatAdminRequired
from nexichat.database.chats import get_served_chats, add_served_chat
from nexichat.database.users import get_served_users, add_served_user
from nexichat.database.clonestats import get_served_cchats, get_served_cusers, add_served_cuser, add_served_cchat
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from pyrogram.enums import ParseMode

# Bot Start Time
START_TIME = time.time()

@nexichat.on_message(filters.command("stats"))
async def stats(cli: Client, message: Message):
    bot_id = (await cli.get_me()).id
    users = len(await get_served_users())
    chats = len(await get_served_chats())
    
    await message.reply_text(
        f"""{(await cli.get_me()).mention} Reaction Bot Stats:

➻ **Chats:** {chats}
➻ **Users:** {users}"""
    )

@nexichat.on_message(filters.command("id"))
async def getid(client, message):
    chat = message.chat
    your_id = message.from_user.id
    message_id = message.id
    reply = message.reply_to_message

    text = f"**[ᴍᴇssᴀɢᴇ ɪᴅ:]({message.link})** `{message_id}`\n"
    text += f"**[ʏᴏᴜʀ ɪᴅ:](tg://user?id={your_id})** `{your_id}`\n"

    if len(message.command) == 2:
        try:
            split = message.text.split(None, 1)[1].strip()
            user_id = (await client.get_users(split)).id
            text += f"**[ᴜsᴇʀ ɪᴅ:](tg://user?id={user_id})** `{user_id}`\n"

        except Exception:
            return await message.reply_text("ᴛʜɪs ᴜsᴇʀ ᴅᴏᴇsɴ'ᴛ ᴇxɪsᴛ.", quote=True)

    text += f"**[ᴄʜᴀᴛ ɪᴅ:](https://t.me/{chat.username})** `{chat.id}`\n\n"

    if (
        not getattr(reply, "empty", True)
        and not message.forward_from_chat
        and not reply.sender_chat
    ):
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ ɪᴅ:]({reply.link})** `{reply.id}`\n"
        text += f"**[ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ɪᴅ:](tg://user?id={reply.from_user.id})** `{reply.from_user.id}`\n\n"

    if reply and reply.forward_from_chat:
        text += f"ᴛʜᴇ ғᴏʀᴡᴀʀᴅᴇᴅ ᴄʜᴀɴɴᴇʟ, {reply.forward_from_chat.title}, ʜᴀs ᴀɴ ɪᴅ ᴏғ `{reply.forward_from_chat.id}`\n\n"
        print(reply.forward_from_chat)

    if reply and reply.sender_chat:
        text += f"ɪᴅ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴄʜᴀᴛ/ᴄʜᴀɴɴᴇʟ, ɪs `{reply.sender_chat.id}`"
        print(reply.sender_chat)

    await message.reply_text(
        text,
        disable_web_page_preview=True,
        parse_mode=ParseMode.DEFAULT,
    )

@nexichat.on_message(filters.command("status"))
async def bot_status(client: Client, message: Message):
    current_time = time.time()
    uptime = current_time - START_TIME  # Calculate uptime
    
    users = len(await get_served_users())  # Get total users
    chats = len(await get_served_chats())  # Get total chats

    cpu_usage = psutil.cpu_percent()  # Get CPU usage
    ram_usage = psutil.virtual_memory().percent  # Get RAM usage
    disk_usage = psutil.disk_usage("/").percent  # Get Disk usage

    python_version = platform.python_version()  # Python version
    os_version = platform.system() + " " + platform.release()  # OS info

    bot_status = f"""
**🤖 Bot Status**
➻ **Uptime:** `{get_readable_time(uptime)}`
➻ **Total Users:** `{users}`
➻ **Total Chats:** `{chats}`
➻ **CPU Usage:** `{cpu_usage}%`
➻ **RAM Usage:** `{ram_usage}%`
➻ **Disk Usage:** `{disk_usage}%`
➻ **Python Version:** `{python_version}`
➻ **OS:** `{os_version}`
    """

    await message.reply_text(bot_status)

def get_readable_time(seconds: int) -> str:
    """Convert seconds into human-readable format."""
    count = 0
    time_list = []
    time_suffix_list = ["s", "m", "h", "d"]
    
    while seconds >= 60 and count < 3:
        seconds, result = divmod(seconds, 60)
        time_list.append(f"{int(result)}{time_suffix_list[count]}")
        count += 1

    time_list.append(f"{int(seconds)}{time_suffix_list[count]}")
    
    return " ".join(time_list[::-1])

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)