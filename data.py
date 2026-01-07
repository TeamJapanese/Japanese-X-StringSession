from pyrogram.types import InlineKeyboardButton


class Data:
    # ⚙️ Single button row
    generate_single_button = [
        InlineKeyboardButton(
            "⚡ ɪɴɪᴛɪᴀᴛᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛɪᴏɴ",
            callback_data="generate"
        )
    ]

    # 🏠 Home buttons
    home_buttons = [
        generate_single_button,
        [
            InlineKeyboardButton(
                "🏠 ʀᴇᴛᴜʀɴ ᴛᴏ ᴄᴏɴᴛʀᴏʟ ᴘᴀɴᴇʟ",
                callback_data="home"
            )
        ]
    ]

    # ⚡ Generate-only keyboard
    generate_button = [
        generate_single_button
    ]

    # 🧭 Main menu buttons
    buttons = [
        generate_single_button,
        [
            InlineKeyboardButton("📘 ᴜsᴇʀ ᴍᴀɴᴜᴀʟ", callback_data="help"),
            InlineKeyboardButton("💫 ᴀʙᴏᴜᴛ sʏsᴛᴇᴍ", callback_data="about")
        ],
        [
            InlineKeyboardButton(
                "ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ",
                url="https://github.com/TeamJapanese/Japanese-X-StringSession"
            )
        ],
        [
            InlineKeyboardButton(
                "👑 ᴅᴇᴠᴇʟᴏᴘᴇʀ",
                url="https://t.me/itz_sandeep_shrma"
            )
        ],
    ]

    # 🌌 boot-up message
    START = """
👋 **ᴡᴇʟᴄᴏᴍᴇ, {}!**  
ɪ’ᴍ **{}**, ʏᴏᴜʀ ᴀᴅᴠᴀɴᴄᴇᴅ sᴇssɪᴏɴ ᴀʀᴄʜɪᴛᴇᴄᴛ 🤖  

ᴇɴɢɪɴᴇᴇʀᴇᴅ ꜰᴏʀ **ᴅᴇᴠᴇʟᴏᴘᴇʀs, ᴄʀᴇᴀᴛᴏʀs & ɪɴɴᴏᴠᴀᴛᴏʀs**,  
ɪ ᴄʀᴀꜰᴛ **ᴘʏʀᴏɢʀᴀᴍ** ᴀɴᴅ **ᴛᴇʟᴇᴛʜᴏɴ** sᴇssɪᴏɴs ᴡɪᴛʜ ᴍᴀxɪᴍᴜᴍ ᴘʀᴇᴄɪsɪᴏɴ ⚡  

💠 **ᴄᴏʀᴇ ᴀʙɪʟɪᴛɪᴇs:**  
• ᴇɴᴄʀʏᴘᴛᴇᴅ, ʟᴏᴄᴀʟ-ᴏɴʟʏ 🔒  
• sᴜᴘᴘᴏʀᴛs ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ  
• ᴢᴇʀᴏ ᴅᴀᴛᴀ ʀᴇᴛᴇɴᴛɪᴏɴ 🧠  
• ɪɴsᴛᴀɴᴛ, sᴘᴇᴇᴅ-ᴏᴘᴛɪᴍɪᴢᴇᴅ 🚀  

ᴘʀᴇss **“⚡ ɪɴɪᴛɪᴀᴛᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛɪᴏɴ”** ᴛᴏ sᴛᴀʀᴛ.  
ᴀᴜᴛᴏᴍᴀᴛɪᴏɴ ʙᴇɢɪɴs ɴᴏᴡ.  

👨‍💻 **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** [sᴧɴᴅᴇᴇᴘ sʜᴧʀᴍᴧ](https://t.me/itz_sandeep_shrma)  
🏷️ [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ](https://t.me/TeamJapaneseOfficial) — ᴘʀᴇᴄɪsɪᴏɴ. ᴘᴇʀꜰᴏʀᴍᴀɴᴄᴇ. ᴘᴇʀꜰᴇᴄᴛɪᴏɴ._
    """

    HELP = """
📘 **sʏsᴛᴇᴍ ᴄᴏᴍᴍᴀɴᴅ ᴍᴀɴᴜᴀʟ**

ʜᴇʀᴇ’s ᴇᴠᴇʀʏᴛʜɪɴɢ ʏᴏᴜ ᴄᴀɴ ᴅᴏ:

━━━━━━━━━━━━━━━━━━━━━━━
**/start** — ʟᴀᴜɴᴄʜ ᴏʀ ʀᴇsᴛᴀʀᴛ ᴛʜᴇ sʏsᴛᴇᴍ  
**/help** — ᴅɪsᴘʟᴀʏ ᴛʜɪs ʜᴇʟᴘ ᴘᴀɴᴇʟ  
**/about** — ʟᴇᴀʀɴ ᴀʙᴏᴜᴛ ᴛʜᴇ sʏsᴛᴇᴍ  
**/generate** — ɢᴇɴᴇʀᴀᴛᴇ sᴇssɪᴏɴ ɪɴsᴛᴀɴᴛʟʏ  
**/cancel** ᴏʀ **/restart** — ᴀʙᴏʀᴛ ᴏʀ ʀᴇsᴇᴛ ᴘʀᴏᴄᴇssᴇs  
**/ping** — ᴄʜᴇᴄᴋ ʙᴏᴛ ʀᴇsᴘᴏɴsᴇ ᴀɴᴅ ʟᴀᴛᴇɴᴄʏ  
**/alive** — ᴠᴇʀɪғʏ ɪғ ʙᴏᴛ ɪs ᴏɴʟɪɴᴇ

━━━━━━━━━━━━━━━━━━━━━━━

💡 *ᴛɪᴘ:* ᴜsᴇ ʙᴜᴛᴛᴏɴs ꜰᴏʀ ꜰᴀsᴛᴇsᴛ ɪɴᴛᴇʀᴀᴄᴛɪᴏɴ ⚡
"""

    ABOUT = """
💫 **sʏsᴛᴇᴍ ᴀʀᴄʜɪᴛᴇᴄᴛᴜʀᴇ ᴏᴠᴇʀᴠɪᴇᴡ**

ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ **sᴇssɪᴏɴ ᴀɪ** — ᴄʀᴇᴀᴛᴇᴅ ʙʏ [sᴧɴᴅᴇᴇᴘ sʜᴧʀᴍᴧ](https://t.me/itz_sandeep_shrma)
ʙᴜɪʟᴛ ᴜɴᴅᴇʀ [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ](https://t.me/TeamJapaneseOfficial) ᴛᴏ ᴍᴀᴋᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴇᴀsʏ ᴀɴᴅ ᴘᴏᴡᴇʀꜰᴜʟ.

🔰 **ᴘʀɪᴍᴀʀʏ ᴘᴜʀᴘᴏsᴇ:** ɢᴇɴᴇʀᴀᴛᴇ ᴘʏʀᴏɢʀᴀᴍ & ᴛᴇʟᴇᴛʜᴏɴ sᴇssɪᴏɴs  
⚙️ **ꜰʀᴀᴍᴇᴡᴏʀᴋ:** [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)  
🐍 **ʟᴀɴɢᴜᴀɢᴇ:** [ᴘʏᴛʜᴏɴ](https://www.python.org)  
👑 **ᴅᴇᴠᴇʟᴏᴘᴇʀ:** [sᴧɴᴅᴇᴇᴘ sʜᴧʀᴍᴧ](https://t.me/itz_sandeep_shrma)  
🏷️ **ᴘʀᴏᴊᴇᴄᴛ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ](https://t.me/TeamJapaneseOfficial) — _ʀᴇᴅᴇꜰɪɴɪɴɢ ᴀᴜᴛᴏᴍᴀᴛɪᴏɴ_

🔒 sᴇᴄᴜʀᴇ • 💨 ꜰᴀsᴛ • 💎 ᴇʟᴇɢᴀɴᴛ • 🧠 ɪɴᴛᴇʟʟɪɢᴇɴᴛ
    """

    SUCCESS = """
✅ **sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ!**  

ᴄᴏᴘʏ ɪᴛ ᴀɴᴅ sᴛᴏʀᴇ sᴀꜰᴇʟʏ.  
⚠️ *ɴᴇᴠᴇʀ sʜᴀʀᴇ ᴡɪᴛʜ ᴀɴʏᴏɴᴇ.*

👨‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ: [sᴧɴᴅᴇᴇᴘ sʜᴧʀᴍᴧ](https://t.me/itz_sandeep_shrma)
    """

    CANCELLED = """
⛔ **ᴘʀᴏᴄᴇss ᴀʙᴏʀᴛᴇᴅ.**

ᴅᴀᴛᴀ ɴᴏᴛ sᴛᴏʀᴇᴅ. ʀᴇsᴛᴀʀᴛ ᴡɪᴛʜ /generate
    """

    ERROR = """
🚨 **ᴇʀʀᴏʀ ᴅᴇᴛᴇᴄᴛᴇᴅ.**

ᴘʟᴇᴀsᴇ ᴛʀʏ ᴀɢᴀɪɴ ᴏʀ ᴜsᴇ /start  
🧠 ᴅᴀᴛᴀ ɪs sᴀꜰᴇ ᴀɴᴅ ᴘʀᴏᴛᴇᴄᴛᴇᴅ
    """
