from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from nexichat import nexichat

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    # Sending a video along with the reply text
    await message.reply_video(
        video="https://envs.sh/RCD.mp4",  # Replace with the actual video URL or local file path
        caption=(
            f"""**❖ нᴇʏ  {message.from_user.first_name} !, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !
━━━━━━━━━━━━━━━━━━━━━━━━━━━

● ɪ ᴀᴍ  {(await client.get_me()).mention} !


⦿━━━━━━━━━━━━━━━━━━━━━⦿
❍ •  ɪ'ʟʟ ʀᴇᴀᴄᴛ ᴛᴏ ᴇᴠᴇʀʏ ᴍᴇssᴀɢᴇ  •
│❍ • ʙᴇsᴛ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ •
│❍ • ɴᴏ ʟᴀɢs + ɴᴏ ᴀᴅs •
│❍ • 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ •
│❍ • ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ •
❍ • ɪ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ғᴇᴀᴛᴜʀᴇs •
⦿━━━━━━━━━━━━━━━━━━━━━⦿

❖ ᴛʜɪs ɪs ᴘᴏᴡᴇʀғᴜʟ ʙᴏᴛ, ғᴏʀ ʏᴏᴜʀ ɢʀᴏᴜᴘ/ᴄʜᴀɴɴᴇʟ  •\n\n❍ • ʏᴏᴜ ᴄᴀɴ ᴍᴀᴋᴇ ʏᴏᴜʀ ʙᴏᴛ ʙʏ /clone**"""
        ),
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("💠 ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ 💠", url="https://t.me/SWEETY9_REACTION_BOT?startgroup=true")],
                [
                    InlineKeyboardButton("🛠 sᴜᴘᴘᴏʀᴛ 🛠 ", url="https://t.me/APNA_CLUB_09"),
                    InlineKeyboardButton("🐰 ᴜᴘᴅᴀᴛᴇs 🐰", url="https://t.me/SWEETY_BOT_UPDATE")
                ],
                [InlineKeyboardButton("🌀 ᴏᴡɴᴇʀ 🌀", url="https://t.me/PRINCE_WEBZ")]
            ]
        )
                    )
