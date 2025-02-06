from pyrogram import Client, filters
from pyrogram.types import Message
from nexichat import nexichat
import random

all_reactions = [
    "👍", "👎", "❤️", "🔥", "🎉", "😂", "😢", "😡", "🤯", "🤔", "🤩",
    "🥰", "😱", "😎", "🤓", "😴", "😜", "👏", "💯", "🤝"
]

@nexichat.on_message(filters.incoming)
async def react_to_messages(client: Client, message: Message):
    try:
        text = message.text.lower() if message.text else ""

        # Specific word reactions
        if "hello" in text:
            reaction = "👋"
        elif "love" in text:
            reaction = "❤️"
        elif "lol" in text or "haha" in text:
            reaction = "😂"
        elif "angry" in text:
            reaction = "😡"
        elif "wow" in text:
            reaction = "🤯"
        else:
            reaction = random.choice(all_reactions)  # Random reaction
        
        await message.react(reaction)

    except Exception as e:
        print(f"Failed to react to message: {e}")