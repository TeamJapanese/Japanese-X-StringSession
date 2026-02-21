"""MIT License"""

"""Copyright (c) 2026 [TeamJapanese](https://github.com/TeamJapanese)"""

"""Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:"""

"""The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software."""

"""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from data import Data
from datetime import datetime
import asyncio, pytz, time, psutil, platform
from Japanese.mongodb import save_user, save_group, remove_user, remove_group
from Japanese.mongodb import (
    get_users_count,
    get_groups_count,
    get_all_user_ids,
    get_all_group_ids
)


# -------------------- Config -------------------- #
LOG_CHAT_ID = -1002519094633  # Your log group ID
BOT_START_TIME = time.time()
TEAM_LINK = "https://t.me/TeamJapaneseOfficial"
BOT_LINK = "https://t.me/JapaneseXStringSessionBot"
BOT_USERNAME = "JapaneseXStringSessionBot"



OWNER_ID = 7208410467  # 

@Client.on_message(filters.command("stats") & filters.user(OWNER_ID))
async def stats_handler(bot, msg):
    users = get_users_count()
    groups = get_groups_count()

    text = f"""
━━━━━━━━━━━━━━━━━━━
📊 **ᴅᴧᴛᴧʙᴧꜱᴇ sᴛᴧᴛs**

👤 **ᴜsᴇʀs:** `{users}`
👥 **ɢʀᴏᴜᴘs:** `{groups}`

🧠 **ᴛᴏᴛᴧʟ:** `{users + groups}`
━━━━━━━━━━━━━━━━━━━
⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})
"""

    await msg.reply_text(text)


# -------------------- Command Filter -------------------- #
def filter_cmd(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

# -------------------- /start Command -------------------- #
@Client.on_message(filter_cmd("start"))
async def start(bot: Client, msg: Message):
    user = msg.from_user
    bot_user = await bot.get_me()

    username = f"@{user.username}" if user.username else "❌ No Username"
    user_link = f"[{user.first_name}](tg://user?id={user.id})"

    # Convert time to IST
    ist = pytz.timezone("Asia/Kolkata")
    current_time = datetime.now(ist).strftime("%d-%m-%Y | %I:%M:%S %p")

    # Send welcome message
    await msg.reply_text(
        Data.START.format(user.mention, bot_user.mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )

    # Log message
    log_text = (
        f"🔔 **ɴᴇᴡ ᴜsᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ!** 🔔\n\n"
        f"👤 **ɴᴀᴍᴇ:** {user_link}\n"
        f"🏷 **ᴜsᴇʀɴᴀᴍᴇ:** {username}\n"
        f"🆔 **ᴜsᴇʀ ɪᴅ:** `{user.id}`\n"
        f"🕒 **ᴛɪᴍᴇ (ɪsᴛ):** `{current_time}`\n"
        f"🔗 **ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ:** [ᴛᴀᴘ ʜᴇʀᴇ](tg://user?id={user.id})\n\n"
        f"⚡ **ᴀᴄᴛɪᴏɴ:** `/start` ᴇxᴇᴄᴜᴛᴇᴅ\n"
        f"🤖 **ʙᴏᴛ:** {bot_user.mention}\n"
        f"💬 **sᴛᴀᴛᴜs:** ᴜsᴇʀ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ sᴜᴄᴄᴇssꜰᴜʟʟʏ 🚀\n"
        f"⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})"
    )

    log_buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("👤 ᴠɪᴇᴡ ᴘʀᴏꜰɪʟᴇ", url=f"tg://openmessage?user_id={user.id}")]
    ])

    try:
        await bot.send_message(
            LOG_CHAT_ID,
            log_text,
            reply_markup=log_buttons,
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"[LOGGING ERROR] {e}")


# -------------------- /help Command -------------------- #
@Client.on_message(filter_cmd("help"))
async def _help(bot: Client, msg: Message):
    await msg.reply_text(
        Data.HELP,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )


# -------------------- /about Command -------------------- #
@Client.on_message(filter_cmd("about"))
async def about(bot: Client, msg: Message):
    await msg.reply_text(
        Data.ABOUT,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(Data.home_buttons)
    )


# -------------------- Inline Keyboard -------------------- #
def get_buttons():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ", url=TEAM_LINK)]
    ])



# -------------------- Auto Save Users & Groups -------------------- #
@Client.on_message(filters.all, group=10)
async def auto_save_handler(bot: Client, msg: Message):
    try:
        if msg.from_user:
            await save_user(msg.from_user)

        if msg.chat and msg.chat.type in ["group", "supergroup"]:
            await save_group(msg.chat)

    except Exception as e:
        print(f"[MONGO SAVE ERROR] {e}")




@Client.on_message(filters.command("broadcast_user") & filters.user(OWNER_ID))
async def broadcast_users(bot, msg):
    if not msg.reply_to_message:
        return await msg.reply_text("❌ Reply to a message to broadcast.")

    sent = 0
    failed = 0

    for user_id in get_all_user_ids():
        try:
            await msg.reply_to_message.forward(user_id)
            sent += 1
            await asyncio.sleep(0.05)
        except:
            failed += 1

    await msg.reply_text(
        f"✅ **Broadcast Completed**\n\n"
        f"👤 Sent: `{sent}`\n"
        f"❌ Failed: `{failed}`"
    )


@Client.on_message(filters.command("broadcast_group") & filters.user(OWNER_ID))
async def broadcast_groups(bot, msg):
    if not msg.reply_to_message:
        return await msg.reply_text("❌ Reply to a message to broadcast.")

    sent = 0
    failed = 0

    for group_id in get_all_group_ids():
        try:
            await msg.reply_to_message.forward(group_id)
            sent += 1
            await asyncio.sleep(0.1)
        except:
            failed += 1

    await msg.reply_text(
        f"✅ **Group Broadcast Done**\n\n"
        f"👥 Sent: `{sent}`\n"
        f"❌ Failed: `{failed}`"
                  )


@Client.on_message(filters.command("broadcast_all") & filters.user(OWNER_ID))
async def broadcast_all(bot, msg):
    if not msg.reply_to_message:
        return await msg.reply_text("❌ Reply to a message to broadcast.")

    sent = 0
    failed = 0

    # ---- USERS ----
    for user_id in get_all_user_ids():
        try:
            await msg.reply_to_message.forward(user_id)
            sent += 1
            await asyncio.sleep(0.05)
        except:
            remove_user(user_id)
            failed += 1

    # ---- GROUPS ----
    for group_id in get_all_group_ids():
        try:
            await msg.reply_to_message.forward(group_id)
            sent += 1
            await asyncio.sleep(0.1)
        except:
            remove_group(group_id)
            failed += 1

    await msg.reply_text(
        f"""
━━━━━━━━━━━━━━━━━━━
📢 **ʙʀᴏᴀᴅᴄᴀsᴛ ᴀʟʟ ᴄᴏᴍᴘʟᴇᴛᴇ**

✅ **sᴇɴᴛ:** `{sent}`
❌ **ʀᴇᴍᴏᴠᴇᴅ:** `{failed}`

⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})
━━━━━━━━━━━━━━━━━━━
"""
    )





# -------------------- /alive Command -------------------- #
@Client.on_message(filters.command("alive") & filters.incoming)
async def alive(bot: Client, msg: Message):
    ist = pytz.timezone("Asia/Kolkata")
    current_time = datetime.now(ist).strftime("%d-%m-%Y | %I:%M:%S %p")

    uptime_seconds = time.time() - BOT_START_TIME
    uptime_str = f"{int(uptime_seconds // 3600)}h:{int((uptime_seconds % 3600) // 60)}m:{int(uptime_seconds % 60)}s"

    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    system = platform.system()
    release = platform.release()
    bot_user = await bot.get_me()

    alive_text = f"""
━━━━━━━━━━━━━━━━━━━
🤖 **ʙᴏᴛ:** [{bot_user.first_name}](https://t.me/{BOT_USERNAME})
🕒 **ᴛɪᴍᴇ (ɪsᴛ):** `{current_time}`
⏱ **ᴜᴘᴛɪᴍᴇ:** `{uptime_str}`
💻 **sʏsᴛᴇᴍ:** `{system} {release}`
⚙️ **ᴄᴘᴜ:** `{cpu}%` | **ʀᴧᴍ:** `{ram}%` | **ᴅɪsᴋ:** `{disk}%`
━━━━━━━━━━━━━━━━━━━
⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})
"""
    image_url = "img/japanese.png"

    await msg.reply_photo(
        photo=image_url,
        caption=alive_text,
        reply_markup=get_buttons()
    )
    

# -------------------- /ping Command -------------------- #
@Client.on_message(filters.command("ping") & filters.incoming)
async def ping(bot: Client, msg: Message):
    start_time = time.time()
    m = await msg.reply_text("⚡ ᴘᴇʀғᴏʀᴍɪɴɢ sʏsᴛᴇᴍ ᴅɪᴧɢɴᴏsᴛɪᴄs...")
    await asyncio.sleep(0.4)
    end_time = time.time()

    ping_ms = (end_time - start_time) * 1000
    uptime_seconds = time.time() - BOT_START_TIME
    uptime_str = f"{int(uptime_seconds // 3600)}h:{int((uptime_seconds % 3600) // 60)}m:{int(uptime_seconds % 60)}s"
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    ist = pytz.timezone("Asia/Kolkata")
    ping_time = datetime.now(ist).strftime("%I:%M:%S %p")
    bot_user = await bot.get_me()

    ping_text = f"""
━━━━━━━━━━━━━━━━━━━
🏓 **ᴘɪɴɢ:** `{ping_ms:.2f} ms`
⏱ **ᴜᴘᴛɪᴍᴇ:** `{uptime_str}`
🕒 **ᴛɪᴍᴇ (ɪsᴛ):** `{ping_time}`
⚙️ **ᴄᴘᴜ:** `{cpu}%` | **ʀᴧᴍ:** `{ram}%` | **ᴅɪsᴋ:** `{disk}%`
━━━━━━━━━━━━━━━━━━━
🤖 **ʙᴏᴛ:** [{bot_user.first_name}](https://t.me/{BOT_USERNAME})
⚡ **ᴘᴏᴡᴇʀᴇᴅ ʙʏ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})
"""
    image_url = "img/japanese.png"

    await msg.reply_photo(
        photo=image_url,
        caption=ping_text,
        reply_markup=get_buttons()
    )

# -------------------- /repo Command -------------------- #
@Client.on_message(filters.command("repo") & filters.incoming)
async def repo_handler(bot: Client, msg: Message):

    repo_text = f"""
━━━━━━━━━━━━━━━━━━━
**[𝑱𝒂𝒑𝒂𝒏𝒆𝒔𝒆 𝑿 𝑺𝒕𝒓𝒊𝒏𝒈 𝑺𝒆𝒔𝒔𝒊𝒐𝒏]({BOT_LINK})**

**ʀᴇᴘᴏꜱɪᴛᴏʀʏ:** ᴏᴘᴇɴ-sᴏᴜʀᴄᴇ
**ꜱᴛᴀᴛᴜꜱ:** ᴀᴄᴛɪᴠᴇʟʏ ᴍᴀɪɴᴛᴀɪɴᴇᴅ
**ꜱᴄᴏᴘᴇ:** ᴘʀᴏᴅᴜᴄᴛɪᴏɴ-ʀᴇᴀᴅʏ ᴄᴏᴅᴇʙᴀꜱᴇ
**ᴅᴏᴄᴜᴍᴇɴᴛᴀᴛɪᴏɴ:** ᴄʟᴇᴀʀ & ᴡᴇʟʟ sᴛʀᴜᴄᴛᴜʀᴇᴅ
━━━━━━━━━━━━━━━━━━━
**ᴍᴀɪɴᴛᴀɪɴᴇʀ:** [ᴛᴇᴧᴍ ᴊᴧᴘᴧɴᴇsᴇ]({TEAM_LINK})
"""

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "ᴠɪᴇᴡ ɢɪᴛʜᴜʙ ʀᴇᴘᴏꜱɪᴛᴏʀʏ",
                    url="https://github.com/TeamJapanese/Japanese-X-StringSession"
                )
            ]
        ]
    )

    await msg.reply_text(
        repo_text,
        reply_markup=buttons,
        disable_web_page_preview=True
    )
