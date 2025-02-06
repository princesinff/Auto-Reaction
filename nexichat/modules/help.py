from pyrogram import Client, filters
from nexichat import nexichat as app

@app.on_message(filters.command("help"))
async def help_command(client, message):
    help_text = (
        "**🤖 Bot Commands Help Menu**\n\n"
        "✅ **/start** - Check if bot is online.\n"
        "📢 **/broadcast [message]** - Send a message to all chats (Admins only).\n"
        "🔍 /id - Get your Telegram ID & Chat ID.\n"
        "📡 /ping - Check bot response time.\n"
        "🛠 /clone - Create your bot clone.\n"
        "📊 /stats - Get bot usage statistics.\n"
        "💡 /help - Show this help menu.\n"
        "❌ /stop - Stop the bot (Admins only).\n\n"
        "💬 Need help? Contact [Support](https://t.me/PRINCE_WEBZ)."
    )

    await message.reply_text(help_text, disable_web_page_preview=True)