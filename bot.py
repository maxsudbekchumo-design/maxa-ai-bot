import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
import requests
TOKEN = os.environ.get("BOT_TOKEN", "8987702613:AAGM_TcSAj0w1l3ZwcYgIi4ZOIdSF0cAt58")
async def start(update: Update, context):
    await update.message.reply_text("🧠 Salom! Men Maxa AI 24/7 man! /rasm deb yoz")
async def rasm_yarat(update: Update, context):
    if not context.args:
        await update.message.reply_text("Yoz: /rasm car red")
        return
    prompt = " ".join(context.args)
    await update.message.reply_text(f"🎨 Chizyapman: {prompt}")
    url = f"https://image.pollinations.ai/prompt/{prompt.replace(' ', '%20')}?nologo=true"
    await update.message.reply_photo(photo=url, caption=f"✅ {prompt}")
async def javob(update: Update, context):
    savol = update.message.text
    try:
        r = requests.get(f"https://text.pollinations.ai/{savol}?model=openai", timeout=25)
        if r.status_code == 200 and len(r.text) > 5:
            await update.message.reply_text(r.text[:4000])
            return
    except:
        pass
    await update.message.reply_text(f"Savol: {savol}")
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("rasm", rasm_yarat))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, javob))
print("Bot ishga tushdi!")
app.run_polling()
