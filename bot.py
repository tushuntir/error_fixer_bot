import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
from dotenv import load_dotenv
from agent import repair, finalize

load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
AUTHORIZED_USER_ID = int(os.getenv("AUTHORIZED_USER_ID"))

async def fix(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID:
        return
    await update.message.reply_text("🧠 Advanced AI repair started…")
    result = repair()
    if result == "FIXED":
        finalize()
        await update.message.reply_text("✅ Repo fixed & pushed.")
    elif result == "CLEAN":
        await update.message.reply_text("ℹ️ No errors found.")
    else:
        await update.message.reply_text("❌ Fix failed. Repo restored.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("fix", fix))
app.run_polling()