from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""Hᴇʏ {msg.from_user.mention},

ᴡᴇʟᴄᴏᴍᴇ ɪɴ ᴠᴏᴛᴇ ʙᴏᴛ. ᴄʜᴇᴄᴋ ᴄᴏᴍᴍᴀɴᴅꜱ ꜰᴏʀ ᴀᴄᴄᴇꜱꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ ʙʏ /help ᴀɴᴅ ᴀʟꜱᴏ ᴅᴏɴᴛ ꜰᴏʀɢᴇᴛ ᴛᴏ ᴊᴏɪɴ ᴏᴜʀ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ. ᴛʜᴀɴᴋ ʏᴏᴜ!

ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ  : [EVONIX](https://t.me/EvonixZone) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ", url="https://t.me/evonity"),
                    InlineKeyboardButton("ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀᴛ", url="https://t.me/EvonixZone")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
