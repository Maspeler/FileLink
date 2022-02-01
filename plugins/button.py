# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if not FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🔮 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝙳𝙸𝚁𝙸𝙺𝚄 🔮", callback_data="about"),
                InlineKeyboardButton(text="• 𝙲𝙻𝙾𝚂𝙴 •", callback_data="close"),
            ],
        ]
        return buttons
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="☄️ 𝙶𝚁𝙾𝚄𝙿 ☄️", url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(text="🔮 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝙳𝙸𝚁𝙸𝙺𝚄 🔮", callback_data="about"),
                InlineKeyboardButton(text="• 𝙲𝙻𝙾𝚂𝙴 •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="☄️ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ☄️", url=client.invitelink),
            ],
            [
                InlineKeyboardButton(text="🔮 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝙳𝙸𝚁𝙸𝙺𝚄 🔮", callback_data="about"),
                InlineKeyboardButton(text="• 𝙲𝙻𝙾𝚂𝙴 •", callback_data="close"),
            ],
        ]
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="🔮 𝚃𝙴𝙽𝚃𝙰𝙽𝙶 𝙳𝙸𝚁𝙸𝙺𝚄 🔮", callback_data="about"),
            ],
            [
                InlineKeyboardButton(text="☄️ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ☄️", url=client.invitelink),
                InlineKeyboardButton(text="☄️ 𝙶𝚁𝙾𝚄𝙿 ☄️", url=client.invitelink2),
            ],
            [InlineKeyboardButton(text="• 𝙲𝙻𝙾𝚂𝙴 •", callback_data="close")],
        ]
        return buttons


def fsub_button(client, message):
    if not FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="☄️ 𝙶𝚁𝙾𝚄𝙿 ☄️", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="♻️ 𝙲𝙾𝙱𝙰 𝚄𝙻𝙰𝙽𝙶 ♻️",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and not FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="☄️ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ☄️", url=client.invitelink),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="♻️ 𝙲𝙾𝙱𝙰 𝚄𝙻𝙰𝙽𝙶 ♻️",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="☄️ 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ☄️", url=client.invitelink),
                InlineKeyboardButton(text="☄️ 𝙶𝚁𝙾𝚄𝙿 ☄️", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="♻️ 𝙲𝙾𝙱𝙰 𝚄𝙻𝙰𝙽𝙶 ♻️",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
