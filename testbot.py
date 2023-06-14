from telegram import ReplyKeyboardRemove
import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
import sys
from telepot.namedtuple import ReplyKeyboardMarkup
import os
import climb
# bot ID
bot_api_key = os.environ.get('bot_API_KEY')
botID = telepot.Bot(bot_api_key)

# 用來處理收到的訊息
def handle(msg):
    chat_id = msg['chat']['id']  # 聊天室ID
    from_id = msg['from']['id']  # 使用者ID
    text = msg['text']  # 使用者傳來的訊息
    # 儲存使用者ID
    if text == '/start':
        buttons = [["The Hacker News"], ["TechNews科技新報 - AI 人工智慧"],["VentureBeat"]]
        keyboard_markup = ReplyKeyboardMarkup(keyboard=buttons)
        botID.sendMessage(chat_id=chat_id, text="請選擇要晚上 6.定時發送的網站", reply_markup=keyboard_markup)
    elif text == 'The Hacker News':
        save_user_id_TheHackerNews(from_id)
        # 處理使用者點選"The Hacker News"
        botID.sendMessage(chat_id=chat_id, text="OK，將於每天晚上 6. 寄送 The Hackers News 當日新聞大綱", reply_markup={"remove_keyboard": True})
    elif text == 'TechNews科技新報 - AI 人工智慧':
        save_user_id_TechNews(from_id)
        botID.sendMessage(chat_id=chat_id, text="OK，將於每天晚上 6. 寄送 TechNews科技新報 - AI 人工智慧 當日新聞大綱", reply_markup={"remove_keyboard": True})

    elif text == 'VentureBeat':
        save_user_id_VentureBeat(from_id)
        botID.sendMessage(chat_id=chat_id, text="OK，將於每天晚上 6. 寄送 VentureBeat 當日新聞大綱", reply_markup={"remove_keyboard": True})

# 儲存使用者ID
def save_user_id_TheHackerNews(user_id):
    #如果有此ID則不做任何動作
    with open('user_TheHackerNews.txt', 'r') as file:
        if str(user_id) in file.read():
            return
    #如果沒有此ID則儲存        
    with open('user_TheHackerNews.txt', 'a') as file:
        file.write(str(user_id) + '\n')
def save_user_id_TechNews(user_id):
    #如果有此ID則不做任何動作
    with open('user_TechNews.txt', 'r') as file:
        if str(user_id) in file.read():
            return
    #如果沒有此ID則儲存        
    with open('user_TechNews.txt', 'a') as file:
        file.write(str(user_id) + '\n')
def save_user_id_VentureBeat(user_id):
    #如果有此ID則不做任何動作
    with open('user_VentureBeat.txt', 'r') as file:
        if str(user_id) in file.read():
            return
    #如果沒有此ID則儲存        
    with open('user_VentureBeat.txt', 'a') as file:
        file.write(str(user_id) + '\n')



MessageLoop(botID, handle).run_as_thread()  # 開啟監聽
print("I'm listening...")
sys.stdout.flush()


# while True:
#     time.sleep(1)

while True:
    current_time = time.strftime('%H:%M')
    #到時候可以自行修改，想要幾點定時發送
    if current_time == '14:12':
        print('gogogo')
        sys.stdout.flush()
        climb.get_hackernews()
        climb.get_technews()
        climb.get_venturebeat()
        time.sleep(30)


    
    time.sleep(30)  