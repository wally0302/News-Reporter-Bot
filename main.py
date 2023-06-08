import json
import os
import requests
from bs4 import BeautifulSoup
import datetime
import openai
import telebot
from telepot.loop import MessageLoop
from pprint import pprint
# #Aws
import boto3
import logging
#定時
# from apscheduler.schedulers.blocking import BlockingScheduler



#進入該網站
def get_web_page(url):
    r = requests.get(url) #將網頁資料GET下來
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser

    #該網站的標題
    title = soup.find('h1',class_='story-title')

    #存文章內容的 array
    context=[]
    #取得該網站的 p tag
    total = soup.find_all('p')
    #取得該網站的 p tag 的文字，最後一個p tag是廣告，所以不要
    for i in range(0,len(total)-1):
        context.append(total[i].text)

    
    #創建一個 key-value 的 dictionary
    data = {}
    #將 title 加進 dictionary
    data['title'] = title.text
    #將 context 加進 dictionary
    data['context'] = context
    #將 url 加進 dictionary
    data['url'] = url

    
    #將 data 傳給 chatGpt3
    get_outline(data)

#把 dictionary 丟給chatGpt3 整理成大綱
def get_outline(data):
    # openai api key 替換成自己的
    openai.api_key ='輸入你 openai api key'


    #將 data['context'] 轉成 string
    articles = ''.join(data['context'])

    #跟 gpt 溝通
    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "將以下內容整理成100字的摘要，並使用台灣最常用的正體中文表達:"},
        {"role": "user", "content": articles},
      ]
    )
    #gpt 回傳的結果
    ans=completion.choices[0].message



    print('標題 : '+data['title'])
    print("\n")
    print('網址 : '+data['url'])
    print("\n")
    print('大綱 : '+ans['content'])
    print("\n")
    print("--------------------------------------------------")
    
    #另外存成 json 檔，給 bot 使用
    save_output_as_json(data, ans['content'])
    
    telebot.send_daily_message(data,ans)
    # #傳給 bot
    # while True:

    #     current_time = time.strftime('%H:%M')

    #     if current_time == '09:00':
    #         telebot.send_daily_message(data,ans)

    #     time.sleep(60)  # 等待一分鐘

def save_output_as_json(data,ans):

    # 檔案名稱
    json_file = 'article_' + str(datetime.date.today()) + '.json'  # article_2023-06-05.json

    try:
        # 嘗試讀取現有資料
        with open(json_file, 'r', encoding='utf-8') as f:
            original_data = json.load(f)
    except FileNotFoundError:
        # 若檔案不存在，創建一個空的資料列表
        original_data = []

    # 新資料
    output = {
        '標題': data['title'],
        '網址': data['url'],
        '大綱': ans
    }

    # 將新資料附加到原有資料後面
    original_data.append(output)

    # 將資料寫入 JSON 檔案
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(original_data, f, indent=2, ensure_ascii=False)
    
    result_upload = upload_file(json_file, "wallys3demo", json_file)
    if result_upload :
        print("bucket file uploaded successfully..!")
    else:
        print("bucket file upload failed..!")

#s3 服務
def upload_file(file_name, bucket, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        logging.error(e)
        return False
    return True
    




def main():
    r = requests.get("https://thehackernews.com/") #將網頁資料GET下來
    soup = BeautifulSoup(r.text,"html.parser") #將網頁資料以html.parser

    #今天日期
    today = datetime.date.today()
    formatted_date = today.strftime("%b %d, %Y")# Jun 05, 2023

    #取得class="body-post clear"的tag
    total = soup.find_all('div',class_='body-post clear')

    #array
    titles=[]
    links=[]
    dates=[]

    for i in range(len(total)):
    #取得class="body-post clear"底下的 title、link、date
        #標題
        title = total[i].find('h2',class_='home-title')
        #加進去array
        titles.append(title.text)
        #超連結
        link = total[i].find('a',class_='story-link')
        links.append(link.get('href'))
        #日期，如果找不到日期則顯示None
        if(total[i].find('span',class_='h-datetime') == None):
            dates.append(None)
        else:
            #去除第一個符號
            dates.append(total[i].find('span',class_='h-datetime').text[1:])
    #bot
    MessageLoop(telebot.botID, telebot.handle).run_as_thread()  # 開啟監聽
    print("I'm listening...")

    # get_web_page(links[0])

    # 如果日期是今天，就進去該網站
    for i in range(len(dates)):
        if(dates[i]==formatted_date):
            get_web_page(links[i])




    # while True:

    #     current_time = time.strftime('%H:%M')

    #     if current_time == '08:30':
    #         telebot.send_daily_message()

    #     time.sleep(60)  # 等待一分鐘

main()
# 指定時區（一定要指定，否則會失敗）
# scheduler = BlockingScheduler(timezone="Asia/Shanghai")

# scheduler.add_job(main, 'cron', day_of_week='1-6', hour=13, minute=6)

# scheduler.start()
