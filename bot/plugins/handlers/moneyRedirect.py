import pyrogram
from bot.config import Buttons


@pyrogram.Client.on_message(
    pyrogram.filters.regex(pattern=f"^{Buttons.money_regex}$")
    & pyrogram.filters.private
    & pyrogram.filters.incoming
)
async def feedback_handler(bot, update):
    await update.reply_text(text, disable_web_page_preview=True)



text = """Hey 👋

Are you tired of searching for ways to earn money without putting in too much effort? Look no further! I've got an incredible app that works on Android, macOS, and Windows, and it's called Honeygain! 🐝💰

🟢 Sign up now using the link below and receive an instant $5 bonus! 🎁💸

👉 Download : https://r.honeygain.me/GS047C3F4A

Or simply use this code while Signup on Honeygain GS047C3F4A (Note you won't get the free $5 without this code or the above link

Honeygain is a unique app that utilizes your idle internet connection and rewards you with credits, which can be easily converted into real money. 💵💻

Simply install the app on your device, let it run in the background, and watch the cash flow in effortlessly! It's that simple! 😎

Don't miss out on this incredible opportunity! Join thousands of satisfied users who have already earned with Honeygain. Visit their official website for more information and authentic proof of earnings. 📲✅

Hurry up and start earning passively today! 🔥💯

Check Proves in @hackinsider private channel (Join the private channel with link mentioned in it and search honeygain)
(Personally tried and tested by Admin)
"""

