from pyrogram import Client as shashank
from pyrogram import filters


@shashank.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def shashank_(client: Client, message: Message):
    await message.reply_sticker("CAACAgEAAxkBAAEJ2GxgnAvflL04PN0B-qpRBbk6trc--AAC3AAD227gRIFzzr3VR17HHwQ")
    await message.reply_text(                               
        f"""<b>Hoi {message.from_user.mention} !!
I'm <b>EX<b> PLAYER!
Here to play music for you in your voice chat
I'can here music in voice chat with me without any lag!!
click the below buttons to know more about me:
</b>"""
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "EX support 🚑", callback_data="Sumport")],
                    InlineKeyboardButton(
                        "EX updates 📲", callback_data="suupport")]
                [
                    InlineKeyboardButton(
                        "🆘 Help", url=f"sshelp")
                ],[
                    InlineKeyboardButton(
                        "About EX" data="aboute*)]]
                    InlineKeyboardButton(
                        "Take me to your group", url=f"https://{SOURCE_CODE}")
                ]
            ]
        ),
      
      
      
@app.on_callback_query(filters.regex("Sumport"))
async def stats_callbacc(_, CallbackQuery):
    text = "i dont have any Support chat"
    await app.answer_callback_query(
        CallbackQuery.id, text, show_alert=True
    )
