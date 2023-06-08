import telepot
import time
from telepot.loop import MessageLoop
from pprint import pprint

botID = telepot.Bot('輸入你 bot 的 token')

# 用來處理收到的訊息
def handle(msg):
    chat_id = msg['chat']['id']  # 聊天室ID
    from_id = msg['from']['id']  # 使用者ID
    text = msg['text']  # 使用者傳來的訊息

    if text == '/start':
        # 儲存使用者ID
        save_user_id(from_id)
        botID.sendMessage(chat_id, 'Hello! I will send you a message every day.')

# 儲存使用者ID
def save_user_id(user_id):
    with open('user_ids.txt', 'a') as file:
        file.write(str(user_id) + '\n')



#每天定時傳送訊息
def send_daily_message(data,ans):
    with open('user_ids.txt', 'r') as file:
        user_ids = file.read().splitlines()
    message = '標題 : ' + data['title'] + '\n\n' \
              '網址 : ' + data['url'] + '\n\n' \
              '大綱 : ' + ans['content'] + '\n\n' \

    for user_id in user_ids:
        botID.sendMessage(user_id, message)





# MessageLoop(botID, handle).run_as_thread()  # 開啟監聽

# print("I'm listening...")

# while True:
#     # 在這裡判斷是否到了每天傳送訊息的時間
#     # 如果是，呼叫send_daily_message函式傳送訊息
#     # 例如，可以使用datetime和time模組來判斷時間
#     current_time = time.strftime('%H:%M')

#     if current_time == '08:44':
#         send_daily_message()

#     time.sleep(60)  # 等待一分鐘