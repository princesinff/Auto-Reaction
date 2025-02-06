from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    # Getting bot's name
    bot_name = (await client.get_me()).mention

    # Sending a video along with the reply text
    await message.reply_video(
        video="https://envs.sh/RCD.mp4",  # Replace with the actual video URL or local file path
        caption=(
            f"""**❖ ʜᴇʏ {message.from_user.first_name} ! ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ!  
━━━━━━━━━━━━━━━━━━━━━━━

● ɪ ᴀᴍ {bot_name}!

⦿━━━━━━━━━━━━━━━━━━━━━⦿  
❍ •  ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ  
❍ • ʙᴇsᴛ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ  
❍ • ɴᴏ ʟᴀɢs + ɴᴏ ᴀᴅs  
❍ • 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ  
❍ • ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ  
❍ • sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs  
⦿━━━━━━━━━━━━━━━━━━━━━⦿  

❖ ᴛʜɪs ɪs ᴀ ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ!  
❍ • ᴄʀᴇᴀᴛᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ ᴜsɪɴɢ /clone**"""
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💠 ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ 💠", url="https://t.me/SWEETY9_REACTION_BOT?startgroup=true")],
                [
                    InlineKeyboardButton("🛠 sᴜᴘᴘᴏʀᴛ 🛠 ", url="https://t.me/APNA_CLUB_09"),
                    InlineKeyboardButton(" 🐰 ᴜᴘᴅᴀᴛᴇs 🐰", url="https://t.me/SWEETY_BOT_UPDATE")
                ],
                [InlineKeyboardButton("🌀 ᴏᴡɴᴇʀ 🌀", url="https://t.me/PRINCE_WEBZ")]
            ]
        )
    )
