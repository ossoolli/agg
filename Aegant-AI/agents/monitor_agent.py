import psutil
import platform
from datetime import datetime

class MonitorAgent:
    def __init__(self):
        self.hostname = platform.node()

    def get_system_status(self):
        # 1. فحص المعالج (CPU)
        cpu_usage = psutil.cpu_percent(interval=1)
        
        # 2. فحص الذاكرة (RAM)
        memory = psutil.virtual_memory()
        
        # 3. فحص القرص الصلب (Disk)
        disk = psutil.disk_usage('/')
        
        # 4. حالة الشبكة (التحميل والرفع)
        net = psutil.net_io_counters()

        status_report = (
            f"📊 **تقرير حالة السيرفر: {self.hostname}**\n"
            f"⏰ الوقت: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
            f"--------------------------------\n"
            f"🖥️ المعالج (CPU): {cpu_usage}%\n"
            f"🧠 الذاكرة (RAM): {memory.percent}% (المستخدم: {memory.used // (1024**2)} MB)\n"
            f"💾 القرص (Disk): {disk.percent}% (المتبقي: {disk.free // (1024**3)} GB)\n"
            f"🌐 الشبكة: ⬆️ {net.bytes_sent // (1024**2)}MB | ⬇️ {net.bytes_recv // (1024**2)}MB\n"
        )
        
        # إضافة تحذيرات ذكية
        warnings = []
        if cpu_usage > 80: warnings.append("⚠️ ضغط عالٍ على المعالج!")
        if memory.percent > 90: warnings.append("⚠️ الذاكرة ممتلئة تقريباً!")
        if disk.percent > 95: warnings.append("⚠️ مساحة القرص حرجة!")
        
        if warnings:
            status_report += "\n**تنبيهات عاجلة:**\n" + "\n".join(warnings)
            
        return status_report

if __name__ == "__main__":
    # هذا الجزء يسمح لنا بتجربة الوكيل بشكل مستقل
    agent = MonitorAgent()
    print(agent.get_system_status())