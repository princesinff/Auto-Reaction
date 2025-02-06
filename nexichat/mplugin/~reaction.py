from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat
import random

# Only good emojis
positive_reactions = [
    "👍", "❤️", "🔥", "🎉", "😂", "🤩", "🥰", "👏", "💯", "🤝"
]

@nexichat.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        text = message.text.lower() if message.text else ""

        # Specific word reactions (good ones only)
        if "hello" in text or "hi" in text:
            reaction = "👋"
        elif "love" in text or "like" in text:
            reaction = "❤️"
        elif "lol" in text or "haha" in text:
            reaction = "😂"
        elif "wow" in text or "amazing" in text:
            reaction = "🤩"
        elif "good" in text or "nice" in text:
            reaction = "💯"
        else:
            reaction = random.choice(positive_reactions)  # Random positive reaction
        
        await message.react(reaction)

    except Exception as e:
        print(f"Failed to react to message: {e}")
