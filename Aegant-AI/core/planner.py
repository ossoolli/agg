import json
import re

class AIPlanner:
    def __init__(self, gemini_service):
        self.ai = gemini_service
        self.system_instruction = """
        أنت مهندس DevOps خبير. حول هدف المستخدم إلى JSON حصراً.
        يجب أن يحتوي الـ JSON على مصفوفة باسم "steps" وكل خطوة بها "description" و "command".
        مثال: {"plan_name": "فحص الذاكرة", "steps": [{"description": "فحص RAM", "command": "free -m"}]}
        """

    def create_plan(self, user_goal):
        prompt = f"الهدف: {user_goal}. أعطني خطة JSON."
        response = self.ai.ask(prompt, system_instruction=self.system_instruction)
        
        # طباعة الرد في التيرمينال للتشخيص (مهم جداً الآن)
        print(f"\n--- AI RAW PLAN ---\n{response}\n------------------\n")

        try:
            match = re.search(r'\{.*\}', response, re.DOTALL)
            if not match: return {"error": "لم يتم العثور على JSON"}
            
            data = json.loads(match.group(0))
            
            # توحيد أسماء المفاتيح (Normalization)
            if "tasks" in data: data["steps"] = data.pop("tasks")
            if "actions" in data: data["steps"] = data.pop("actions")
            
            return data
        except Exception as e:
            return {"error": f"خطأ في تحليل البيانات: {str(e)}"}

    def create_correction_plan(self, goal, failed_cmd, error_msg):
        prompt = f"الأمر {failed_cmd} فشل بخطأ: {error_msg}. اقترح أمراً بديلاً بصيغة JSON: {{'fixed_command': '...', 'reason': '...'}}"
        response = self.ai.ask(prompt)
        try:
            match = re.search(r'\{.*\}', response, re.DOTALL)
            return json.loads(match.group(0))
        except: return {}