from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.private & filters.command("start"))
async def start_handler(client, message: Message):
    await message.reply_text("👋 Send me any file and I’ll give you a direct download link.")

@Client.on_message(filters.private & filters.document)
async def handle_file(client, message: Message):
    file_id = message.document.file_id
    file_name = message.document.file_name or "unnamed_file"
    await message.reply_text(
        f"📥 File saved!\n\n🔗 Your link:\nhttps://your-render-url.onrender.com/{file_id}/{file_name}"
    )
