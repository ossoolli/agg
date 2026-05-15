C:\Users\Administrator\Downloads\vristo-tailwind-admin-template-2025-11-27-04-30-42-utc\vristo-main-3.0.0\react\react\vristo-react-starter
gh repo clone ossoolli/ossoolli-main
# Create a new configuration for your test environment
gcloud config configurations create test-env
# Set the project for this specific configuration
gcloud config set project Mytest
gcloud config set project mytest-496209
gcloud services enable  aiplatform.googleapis.com  bigquery.googleapis.com
mkdir -p ai-agents-adk && cd ai-agents-adk
uv venv --python 3.12
source .venv/bin/activaterm -rf ~/.cache
uv pip install google-adk --no-cache
cd ~
cloudshell workspace ai-agents-adk
gcloud projects list
cat README-cloudshell.txt
pip install -r requirements.txt
pip install -r requirements.txt
gcloud config set project mytest-496209
ls ai-agents-sdk
pip install python-telegram-bot
touch telegram_agent.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
# ضع الـ Token الخاص بك هنا
TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
if __name__ == '__main__':;     application = ApplicationBuilder().token(TOKEN).build()
pip install python-telegram-bot google-generativeai
import logging
import google.generativeai as genai
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
# إعدادات التوكن والـ AI
TELEGRAM_TOKEN = '8743809028:AAF00ls4Yo1DRHxc0w8tkzEcaInZu-bfBKA'
# بما أنك داخل Cloud Shell، سيتم التعرف على المشروع تلقائياً، 
# لكننا سنستخدم إعدادات افتراضية بسيطة للبدء
genai.configure(api_key="ضع_هنا_API_KEY_الخاص_بـ_GEMINI") 
model = genai.GenerativeModel('gemini-1.5-flash')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
if __name__ == '__main__':;     application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
nano smart_bot.py
pip install python-telegram-bot google-generativeai
/home/madarmutaz/.venv/bin/python -m pip install python-telegram-bot google-generativeai
python3 smart_bot.py
pkill -f python3
python3 smart_bot.py
pkill -f python3
bash <(curl -sSL \
https://storage.googleapis.com/cloud-samples-data/adc/setup_adc.sh)
source /home/madarmutaz/.venv/bin/activate
pkill -f python3
ps aux | grep smart_bot.py | awk '{print $2}' | xargs kill -9
source /home/madarmutaz/.venv/bin/activate
pip install python-telegram-bot google-generativeai python-dotenv
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import google.generativeai as genai
# --- الإعدادات ---
TELEGRAM_TOKEN = "8108330920:AAEPoHRU6nPafPVyNyTsn5fIEfFHC0arxd8"
GEMINI_API_KEY = "ضع_هنا_مفتاح_جيمناي_الخاص_بك" # استبدله بمفتاح Gemini الخاص بك
# إعداد Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
# إعداد السجلات (Logs) لمراقبة الأخطاء
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
# دالة الترحيب /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
# دالة معالجة الرسائل والرد باستخدام Gemini
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
if __name__ == '__main__':;     application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
source /home/madarmutaz/.venv/bin/activate
nano smart_bot.py
python3 smart_bot.py
nano smart_bot.py
python3 smart_bot.py
nano smart_bot.py
python3 smart_bot.py
nano smart_bot.py
source /home/madarmutaz/.venv/bin/activate
python3 smart_bot.py
source /home/madarmutaz/.venv/bin/activate
nano smart_bot.py
/home/madarmutaz/.venv/bin/python /home/madarmutaz/smart_bot.py
source /home/madarmutaz/.venv/bin/activate
curl "https://api.telegram.org/bot8108330920:AAEPoHRU6nPafPVyNyTsn5fIEfFHC0arxd8/deleteWebhook"
source /home/madarmutaz/.venv/bin/activate
/home/madarmutaz/.venv/bin/python /home/madarmutaz/smart_bot.py
curl "https://api.telegram.org/bot8108330920:AAEPoHRU6nPafPVyNyTsn5fIEfFHC0arxd8/deleteWebhook"
/home/madarmutaz/.venv/bin/python /home/madarmutaz/smart_bot.py
source /home/madarmutaz/.venv/bin/activate
curl "https://api.telegram.org/bot8108330920:AAEPoHRU6nPafPVyNyTsn5fIEfFHC0arxd8/deleteWebhook"
source /home/madarmutaz/.venv/bin/activate
python3 smart_bot.py
curl "https://api.telegram.org/bot8108330920:AAEPoHRU6nPafPVyNyTsn5fIEfFHC0arxd8/deleteWebhook"
pip install python-telegram-bot --upgrade
source /home/madarmutaz/.venv/bin/activate
pip install --upgrade google-generativeai grpcio grpcio-status
/home/madarmutaz/.venv/bin/python /home/madarmutaz/smart_bot.py
pip uninstall -y google-generativeai grpcio && pip install google-generativeai==0.4.1 grpcio==1.60.0
pip uninstall -y google-generativeai grpcio && pip install google-generativeai==0.4.1 grpcio==1.60.0
smart_bot.py
source /home/madarmutaz/.venv/bin/activate
smart_bot.py
source /home/madarmutaz/.venv/bin/activate
/home/madarmutaz/.venv/bin/python /home/madarmutaz/smart_bot.py
python3 smart_bot.py
unset GRPC_VERBOSITY
unset GOOGLE_API_KEY
unset GRPC_VERBOSITY
unset GOOGLE_API_KEY
source /home/madarmutaz/.venv/bin/activate
/home/madarmutaz/.venv/bin/python /home/madarmutaz/smart_bot.py
python3 smart_bot.py
pkill -f smart_bot.py
python3 smart_bot.py
python3 smart_bot.py
source /home/madarmutaz/.venv/bin/activate
/home/madarmutaz/.venv/bin/python /home/madarmutaz/smart_bot.py
pkill -f smart_bot.py
python3 smart_bot.py
curl https://generativelanguage.googleapis.com/v1beta/models?key=AIzaSyCJdEFES7s7GYft0SVC-SQD2BMt_2gx4vk
source /home/madarmutaz/.venv/bin/activate
mkdir -p core agents services storage/logs docker && touch core/planner.py core/executor.py core/security.py core/memory.py agents/monitor_agent.py agents/deploy_agent.py services/gemini_service.py main.py
pkill -f smart_bot.py
source /home/madarmutaz/.venv/bin/activate
python3 main.py
pkill -f main.py
python3 main.py
pkill -f main.py
pkill -f smart_bot.py
pkill -f smart_bot.py
python3 main.py
source /home/madarmutaz/.venv/bin/activate
pkill -f main.py
python3 main.py
pkill -f main.py
python3 main.py
pkill -f main.py
python3 main.py
pkill -f main.py
python3 main.py
source /home/madarmutaz/.venv/bin/activate
python3 main.py  python3 main.py
python3 main.py
source /home/madarmutaz/.venv/bin/activate
python3 main.py
pkill -f main.py
pkill -f main.pypkill -f main.py
killall python3
killall python3killall python3
pkill -f main.py
python3 main.py
source /home/madarmutaz/.venv/bin/activate
pkill -f main.py
python3 main.py
git init
# إضافة ملف .gitignore لمنع رفع الملفات الحساسة
echo "__pycache__/
*.pyc
.env
storage/logs/*" > .gitignore
git add .
git commit -m "Initial commit: Aegant AI Stable Orchestrator with Self-Healing"
source /home/madarmutaz/.venv/bin/activate
source /home/madarmutaz/.venv/bin/activate
https://github.com/ossoolli/agg.git
cd path/to/your/project
git init
git remote add origin https://github.com/ossoolli/agg.git
git add .
git commit -m "إضافة كود وكيل تليجرام مع Vertex AI"
source /home/madarmutaz/.venv/bin/activate
> git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/ossoolli/agg.git'
source /home/madarmutaz/.venv/bin/activate
> git push -u origin master
error: src refspec master does not match any
error: failed to push some refs to 'https://github.com/ossoolli/agg.git'
source /home/madarmutaz/.venv/bin/activate
echo "# agg" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/ossoolli/agg.git
git push -u origin main
git remote add origin https://github.com/ossoolli/agg.git
git branch -M main
git push -u origin main
git branch -M main
source /home/madarmutaz/.venv/bin/activate
git branch -M main
source /home/madarmutaz/.venv/bin/activate
git init
# إضافة ملف .gitignore لمنع رفع الملفات الحساسة
echo "__pycache__/
*.pyc
.env
storage/logs/*" > .gitignore
git add .
git commit -m "Initial commit: Aegant AI Stable Orchestrator with Self-Healing"
source /home/madarmutaz/.venv/bin/activate
/home/madarmutaz/.venv/bin/python /home/madarmutaz/Aegant-AI/main.py
git config --global credential.helper store
git push origin main
git rm -r --cached .cache/
echo ".cache/" >> .gitignore
echo "__pycache__/" >> .gitignore
echo ".venv/" >> .gitignore
git add .gitignore
git commit --amend --no-edit
git push origin main
# إزالة تتبع كل الملفات حالياً
git rm -r --cached .
cat << EOF > .gitignore
# بيئات بايثون
.venv/
venv/
__pycache__/
*.pyc

# ملفات المحرر والنظام
.cache/
.codeoss/
.gemini/
.npm/
.vscode/
.idea/
.DS_Store

# سجلات وملفات مؤقتة
*.log
tmp/
EOF

# إضافة الملفات (سيتم تجاهل الملفات الضخمة تلقائياً بفضل .gitignore)
git add .
# تعديل الـ Commit الأخير ليكون نظيفاً تماماً
git commit --amend --no-edit
# إضافة الملفات (سيتم تجاهل الملفات الضخمة تلقائياً بفضل .gitignore)
git add .
# تعديل الـ Commit الأخير ليكون نظيفاً تماماً
git commit --amend --no-edit
git push origin main --force
rm -rf .git
git init
cat << EOF > .gitignore
.cache/
.codeoss/
.gemini/
.npm/
.venv/
venv/
__pycache__/
*.log
.git-credentials
EOF

git remote add origin https://github.com/ossoolli/agg.git
git push -u origin main --force
git@github.com:ossoolli/agg.git
source /home/madarmutaz/.venv/bin/activate
ps -p $$ -o comm=
