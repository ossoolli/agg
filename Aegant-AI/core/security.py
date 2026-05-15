class SecurityValidator:
    def __init__(self):
        # قائمة الأوامر المحظورة تماماً
        self.blacklist = [
            'rm -rf /', 'mkfs', 'shutdown', 'reboot', 
            ':(){ :|:& };:', 'dd if=/dev/zero'
        ]

    def validate_command(self, command):
        """التحقق من سلامة الأمر"""
        cmd_clean = command.lower().strip()
        
        # 1. فحص القائمة السوداء
        for forbidden in self.blacklist:
            if forbidden in cmd_clean:
                return False, f"⚠️ محاولة تنفيذ أمر محظور: {forbidden}"
        
        # 2. فحص الأوامر الحساسة (تتطلب موافقة يدوية مستقبلاً)
        sensitive_keywords = ['rm ', 'mv ', 'chmod', 'chown']
        for word in sensitive_keywords:
            if cmd_clean.startswith(word) or f" {word}" in cmd_clean:
                # هنا يمكننا لاحقاً إضافة نظام "طلب موافقة"
                pass
                
        return True, "Safe"