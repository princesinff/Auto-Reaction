from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from nexichat import nexichat

@nexichat.on_message(filters.command("start"))
async def start_message(client: Client, message: Message):
    bot_name = (await client.get_me()).mention
    user_name = message.from_user.first_name

    # Send the video first
    await message.reply_video(
        video="https://envs.sh/RCD.mp4"  # Replace with the actual video URL or file path
    )

    # Send the caption with buttons in a separate message
    caption = f"""
╭━━━━━━━━━━━━━━━━━━━╮
┃ ✦ ʜᴇʏ {user_name} !, ɴɪᴄᴇ ᴛᴏ ᴍᴇᴇᴛ ʏᴏᴜ !  
╰━━━━━━━━━━━━━━━━━━━╯

💠 ɪ ᴀᴍ {bot_name} ! 
➥ ʏᴏᴜʀ ᴘᴇʀsᴏɴᴀʟ ᴀssɪsᴛᴀɴᴛ ᴡɪᴛʜ ᴘᴏᴡᴇʀғᴜʟ ғᴇᴀᴛᴜʀᴇs!

🌟 © ғᴇᴀᴛᴜʀᴇs ™:
🔹 ᴀᴜᴛᴏ-ʀᴇᴀᴄᴛ ᴛᴏ ᴍᴇssᴀɢᴇs  
🔹 ʙᴇsᴛ ᴄʟᴏɴᴇ ғᴇᴀᴛᴜʀᴇ  
🔹 ɴᴏ ʟᴀɢs & ɴᴏ ᴀᴅs  
🔹 24/7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ  
🔹 ᴀ ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ  

✨ ᴍᴀᴋᴇ ʏᴏᴜʀ ᴏᴡɴ ʙᴏᴛ: `/clone`
"""

    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("💠 ᴀᴅᴅ ᴍᴇ ɪɴ ɢʀᴏᴜᴘ 💠", url="https://t.me/SWEETY9_REACTION_BOT?startgroup=true")],
            [
                InlineKeyboardButton("🛠 sᴜᴘᴘᴏʀᴛ", url="https://t.me/APNA_CLUB_09"),
                InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url="https://t.me/SWEETY_BOT_UPDATE")
            ],
            [InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/PRINCE_WEBZ")]
        ]
    )

    await message.reply_text(caption, reply_markup=buttons)