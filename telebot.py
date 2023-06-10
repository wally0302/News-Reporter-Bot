import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint
import climb
import os 
import sys
print('123')

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
        save_user_id(from_id)
        botID.sendMessage(chat_id, 'Hello ！會於每天的 18:00 準時發送 The Hacker News 當日新聞大綱！')

    # #設定時間
    # if text =='/timing':        
    #     botID.sendMessage(chat_id, '請輸入時間 (格式為 HH:MM)')

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
    current_time = time.strftime('%H:%M')
#    print('go')
#    sys.stdout.flush()
 #   climb.get()
    #到時候可以自行修改，想要幾點定時發送
    if current_time == '23:45':
        print('gogogo')
        sys.stdout.flush()
        climb.get()
        time.sleep(30)

    time.sleep(30)  