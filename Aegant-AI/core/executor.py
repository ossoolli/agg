import subprocess
import html

class TaskExecutor:
    def __init__(self, timeout=30):
        self.timeout = timeout  # تأكد أن هذا السطر مزاح بـ 8 مسافات (أو 2 Tabs) من بداية الملف

    def execute(self, command):
        try:
            process = subprocess.run(
                command, 
                shell=True, 
                capture_output=True, 
                text=True, 
                timeout=self.timeout
            )
            output = html.escape(process.stdout + process.stderr)
            return {
                'status': 'success' if process.returncode == 0 else 'failed', 
                'output': output if output else 'Done.'
            }
        except Exception as e:
            return {'status': 'error', 'output': str(e)}