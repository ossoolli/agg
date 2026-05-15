import os
import json
import logging
import html
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# استيراد المكونات من الهيكلية الجديدة
from core.executor import TaskExecutor
from core.planner import AIPlanner
from core.security import SecurityValidator
from services.gemini_service import GeminiService

# 1. تحميل متغيرات البيئة من ملف .env
load_dotenv()

# 2. إعداد المتغيرات الأساسية
TOKEN = os.getenv("TELEGRAM_TOKEN")
KEY = os.getenv("GEMINI_KEY")
ADMIN_ID = int(os.getenv("ADMIN_ID")) if os.getenv("ADMIN_ID") else 0

# إعداد السجلات التشغيلية (Logging)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 3. تهيئة المكونات التقنية
ai_service = GeminiService(KEY)
executor = TaskExecutor(timeout=60) # رفع المهلة لـ 60 ثانية لعمليات الـ Git والرفع
planner = AIPlanner(ai_service)
security = SecurityValidator()

async def handle_autonomous_goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """المعالج الذكي للأهداف الاستقلالية"""
    if update.effective_user.id != ADMIN_ID:
        return

    user_text = update.message.text

    # تمييز الدردشة العادية عن "الأهداف التنفيذية"
    if len(user_text.split()) < 3:
        await context.bot.send_chat_action(update.effective_chat.id, 'typing')
        chat_res = ai_service.ask(user_text)
        await update.message.reply_text(chat_res)
        return

    await update.message.reply_text("🧠 **جاري التخطيط وتدقيق الأمان...**")

    # المرحلة الأولى: إنشاء الخطة
    plan = planner.create_plan(user_text)
    if "error" in plan:
        await update.message.reply_text(f"❌ فشل التخطيط: {plan['error']}")
        return

    steps = plan.get('steps', [])
    if not steps:
        await update.message.reply_text("❓ الخطة فارغة. حاول توضيح الطلب.")
        return

    await update.message.reply_text(f"📝 **الخطة المعتمدة:** {plan.get('plan_name', 'خطة تنفيذية')}")

    # المرحلة الثانية: حلقة التنفيذ مع التصحيح الذاتي
    for step in steps:
        cmd = step['command']
        desc = step['description']
        
        await update.message.reply_text(f"⏳ **جاري تنفيذ:** {desc}")
        
        # فحص الأمان قبل أي خطوة
        is_safe, sec_msg = security.validate_command(cmd)
        if not is_safe:
            await update.message.reply_text(sec_msg)
            continue

        # التنفيذ
        res = executor.execute(cmd)

        # حلقة التصحيح الذاتي (Self-Healing)
        if res['status'] != 'success' or "timeout" in res['output'].lower():
            await update.message.reply_text("⚠️ **تعثر التنفيذ.** جاري البحث عن حل بديل...")
            
            # سؤال المخطط عن مخرج تقني للخطأ
            correction = planner.create_correction_plan(user_text, cmd, res['output'])
            
            if "fixed_command" in correction:
                fixed_cmd = correction['fixed_command']
                reason = correction.get('reason', 'تصحيح تلقائي')
                
                await update.message.reply_text(f"🔧 **الحل:** {reason}\n🔄 **إعادة المحاولة بـ:** `{fixed_cmd}`")
                
                # فحص أمان الأمر الجديد ثم تنفيذه
                is_safe_new, _ = security.validate_command(fixed_cmd)
                if is_safe_new:
                    res = executor.execute(fixed_cmd)

        # عرض النتيجة النهائية للخطوة
        status_icon = "✅" if res['status'] == 'success' else "❌"
        # حماية الرسالة من رموز HTML التي قد يخرجها التيرمينال
        safe_output = html.escape(res['output'])
        await update.message.reply_text(
            f"{status_icon} **النتيجة:**\n<pre>{safe_output[:3500]}</pre>", 
            parse_mode='HTML'
        )

if __name__ == '__main__':
    if not TOKEN or not KEY:
        print("❌ خطأ: لم يتم العثور على TOKEN أو KEY في ملف .env")
    else:
        print("🚀 Aegant AI Expert Mode is ONLINE")
        
        app = ApplicationBuilder().token(TOKEN).build()
        
        # ربط معالج الرسائل النصية
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_autonomous_goal))
        
        app.run_polling()