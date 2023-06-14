from telegram import ReplyKeyboardRemove
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
import climb
import sys
from telepot.namedtuple import ReplyKeyboardMarkup
import os
# bot ID
bot_api_key = os.environ.get('bot_API_KEY')
# bot_api_key=
botID = telepot.Bot(bot_api_key)

# 用來處理收到的訊息
def handle(msg):
    chat_id = msg['chat']['id']  # 聊天室ID
    from_id = msg['from']['id']  # 使用者ID
    text = msg['text']  # 使用者傳來的訊息
    # 儲存使用者ID
    if text == '/start':
        save_user_id(from_id)
        buttons = [["The Hacker News"], ["TechNews科技新報 - AI 人工智慧"],["VentureBeat"]]
        keyboard_markup = ReplyKeyboardMarkup(keyboard=buttons)
        botID.sendMessage(chat_id=chat_id, text="請選擇要晚上 6.定時發送的網站", reply_markup=keyboard_markup)
    elif text == 'The Hacker News':
        index=0
        # 處理使用者點選"The Hacker News"
        botID.sendMessage(chat_id=chat_id, text="OK，將於每天晚上 6. 寄送 The Hackers News 當日新聞大綱", reply_markup={"remove_keyboard": True})
        # 在這裡呼叫定時執行函式
        schedule_hackernews(index)
    elif text == 'TechNews科技新報 - AI 人工智慧':
        index=1
        botID.sendMessage(chat_id=chat_id, text="OK，將於每天晚上 6. 寄送 TechNews科技新報 - AI 人工智慧 當日新聞大綱", reply_markup={"remove_keyboard": True})
        schedule_hackernews(index)
    elif text == 'VentureBeat':
        index=2
        botID.sendMessage(chat_id=chat_id, text="OK，將於每天晚上 6. 寄送 VentureBeat 當日新聞大綱", reply_markup={"remove_keyboard": True})
        schedule_hackernews(index)


# 定時執行 The Hacker News
def schedule_hackernews(index):
    while True:
        current_time = time.strftime('%H:%M')
        # 判斷是否為指定的時間
        if current_time == '15:37':
            print('gogogo')
            sys.stdout.flush()
            if index==0:
                climb.get_hackernews()
            elif index==1:
                climb.get_technews()
            elif index==2:
                climb.get_technews()

            time.sleep(30)

        time.sleep(30)

# 儲存使用者ID
def save_user_id(user_id):
    #如果有此ID則不做任何動作
    with open('user_ids.txt', 'r') as file:
        if str(user_id) in file.read():
            return
    #如果沒有此ID則儲存        
    with open('user_ids.txt', 'a') as file:
        file.write(str(user_id) + '\n')

MessageLoop(botID, handle).run_as_thread()  # 開啟監聽
print("I'm listening...")
sys.stdout.flush()



while True:
    time.sleep(1)
