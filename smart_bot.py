import logging
import subprocess
import html
import requests
import json
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters

# --- الإعدادات المؤكدة ---
TELEGRAM_TOKEN = "8108330920:AAEPoHRU6nPafPVyNyTsn5fIEfFHC0arxd8"
GEMINI_API_KEY = "AIzaSyCJdEFES7s7GYft0SVC-SQD2BMt_2gx4vk" 
AUTHORIZED_USER_ID = 1739350058

logging.basicConfig(level=logging.INFO)

def ask_gemini_2026(prompt):
    # الاسم مأخوذ مباشرة من لقطة الشاشة الخاصة بك في AI Studio
    # استخدام v1beta لأن الموديلات الجديدة (3.1) تطلق عليه أولاً
    model_id = "gemini-3.1-flash-lite" 
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_id}:generateContent?key={GEMINI_API_KEY}"
    
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        result = response.json()
        
        if response.status_code == 200:
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            # نظام تشخيص ذكي: سيخبرك بالنماذج المتاحة إذا فشل هذا النموذج
            print(f"Error Details: {json.dumps(result, indent=2)}")
            return f"⚠️ الموديل {model_id} غير مفعّل لمفتاحك حالياً. تأكد من قائمة v1beta."
            
    except Exception as e:
        return f"❌ فشل تقني: {str(e)[:50]}"

async def run_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID: return
    command = " ".join(context.args)
    if not command: return
    try:
        process = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=15)
        safe_output = html.escape(process.stdout + process.stderr)
        await update.message.reply_text(f"🖥️ **Terminal:**\n<pre>{safe_output if safe_output else 'Done.'}</pre>", parse_mode='HTML')
    except Exception as e:
        await update.message.reply_text(f"❌ خطأ نظام: {e}")

async def handle_chat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != AUTHORIZED_USER_ID: return
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")
    response = ask_gemini_2026(update.message.text)
    await update.message.reply_text(response)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("cmd", run_cmd))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_chat))
    
    print(f"🚀 البدء باستخدام موديل 2026: gemini-3.1-flash-lite")
    app.run_polling()