import os
import json
import logging
import html
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# استيراد المكونات الأساسية للنظام
from core.executor import TaskExecutor
from core.planner import AIPlanner
from core.security import SecurityValidator
from services.gemini_service import GeminiService

# --- الإعدادات الأساسية ---
TOKEN = '8108330920:AAEPoHRU6nPafPVyNyTsn5fIEfFHC0arxd8'
KEY = 'AIzaSyCJdEFES7s7GYft0SVC-SQD2BMt_2gx4vk'
ADMIN = 1739350058

# إعداد السجلات لمراقبة أداء السيرفر
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# --- تهيئة المحركات ---
ai_service = GeminiService(KEY)
executor = TaskExecutor(timeout=30)
planner = AIPlanner(ai_service)
security = SecurityValidator()

async def handle_autonomous_goal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """المعالج الذكي لتحويل الأهداف إلى أفعال"""
    if update.effective_user.id != ADMIN:
        return

    user_text = update.message.text
    
    # 1. التمييز بين الدردشة العادية وطلب تنفيذ مهمة
    if len(user_text.split()) < 3:
        await context.bot.send_chat_action(update.effective_chat.id, 'typing')
        response = ai_service.ask(user_text)
        await update.message.reply_text(response)
        return

    await update.message.reply_text("🧠 **جاري التخطيط وتدقيق الأمان...**")

    # 2. توليد الخطة التنفيذية
    plan = planner.create_plan(user_text)
    
    if "error" in plan:
        await update.message.reply_text(f"❌ **فشل التخطيط:** {plan['error']}")
        return

    steps = plan.get('steps', [])
    if not steps:
        await update.message.reply_text("❓ **الخطة فارغة:** لم يستطع الذكاء تحديد خطوات تقنية واضحة.")
        return

    await update.message.reply_text(f"📝 **الخطة المعتمدة:** {plan.get('plan_name', 'خطة تنفيذية')}")

    # 3. حلقة التنفيذ الذكية
    for step in steps:
        desc = step.get('description', 'خطوة غير معرفة')
        cmd = step.get('command', '')

        if not cmd: continue

        await update.message.reply_text(f"⏳ **جاري تنفيذ:** {desc}")

        # فحص الأمان قبل إرسال الأمر للتيرمينال
        is_safe, sec_msg = security.validate_command(cmd)
        if not is_safe:
            await update.message.reply_text(f"🛡️ **تم حجب الأمر:** {sec_msg}")
            continue

        # التنفيذ
        res = executor.execute(cmd)

        # --- 4. حلقة التصحيح الذاتي (Self-Healing) ---
        if res['status'] != 'success' or "timeout" in res['output'].lower():
            await update.message.reply_text("⚠️ **فشل التنفيذ أو انتهت المهلة.** جاري إيجاد حل بديل...")
            
            correction = planner.create_correction_plan(user_text, cmd, res['output'])
            fixed_cmd = correction.get('fixed_command')
            
            if fixed_cmd:
                reason = correction.get('reason', 'تصحيح تقني')
                await update.message.reply_text(f"🔧 **الحل:** {reason}\n🔄 **إعادة المحاولة بـ:** `{fixed_cmd}`")
                
                # فحص أمان الأمر الجديد
                is_safe_now, _ = security.validate_command(fixed_cmd)
                if is_safe_now:
                    res = executor.execute(fixed_cmd)

        # 5. عرض النتيجة النهائية لكل خطوة
        status_icon = "✅" if res['status'] == 'success' else "❌"
        # تنظيف المخرجات من أي رموز تكسر تنسيق التلغرام
        safe_output = html.escape(res['output'])
        await update.message.reply_text(
            f"{status_icon} **النتيجة:**\n<pre>{safe_output[:4000]}</pre>", 
            parse_mode='HTML'
        )

if __name__ == '__main__':
    # ملاحظة: تم إزالة pkill من الداخل لتجنب توقف البوت عند التشغيل
    print("🚀 Aegant AI Expert Mode is starting...")
    
    try:
        app = ApplicationBuilder().token(TOKEN).build()
        
        # ربط الرسائل النصية بالمعالج الذكي
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_autonomous_goal))
        
        print("✅ Aegant AI is ONLINE and waiting for goals.")
        app.run_polling()
    except Exception as e:
        print(f"❌ Critical Error: {e}")