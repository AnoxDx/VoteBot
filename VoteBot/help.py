from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("help"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""ᴄʀᴇᴀᴛᴇ ᴘᴏʟʟ ᴡɪᴛʜ ᴄᴏᴍᴍᴀɴᴅ /poll <chat-link>/<chat-id> ᴀɴᴅ ꜰᴏʀ ᴅᴇʟᴇᴛɪɴɢ ᴛʜᴇ ᴘᴏʟʟ ᴜꜱᴇ /delete""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", url="https://t.me/evonity"),
                    InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
