# 載入 selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# openai 相關模組
import os
import openai
import datetime


def main():
    #設定 driver 位置
    options=Options()
    options.chrome_executable_path='C:\\Users\\user\\Desktop\\chromedriver.exe'
    # 建立 driver 物件實體，用程式操作瀏覽器
    driver = webdriver.Chrome(options=options)
    # 前往指定網址，網頁連線
    driver.get("https://www.cryptocity.tw/")


    # link 列表
    links=[]
    # 文章標題 列表
    titles=[]
    # 文章內容 列表
    articles=[]

    #取得今天日期，將 - 替換成 .
    today = datetime.date.today()
    today = str(today).replace('-', '.') #2023.05.28

    today = '2023.05.26'


    #搜尋 class 屬性是 news-text d-flex jc-start ac-center flex-wrap 的所有標籤
    tags=driver.find_elements(By.CLASS_NAME, 'news-text.d-flex.jc-start.ac-center.flex-wrap') #類別名稱定位 

    # 先爬每個文章的連結
    for tag in tags:
        # 取得文章日期
        date=tag.find_element(By.CLASS_NAME, 'bd3-n').text 

        # 如果文章日期是今天
        if today in date:
            # 文章標題
            title=tag.text
            #將title加入titles
            titles.append(title)
            #取得標籤中的超連結
            #(返回第一個出現 a 標籤)
            link=tag.find_element(By.TAG_NAME, 'a').get_attribute('href') #標籤定位 

            #將link加入links
            links.append(link)


    # 再爬每個文章的內容
    for i in range(len(links)):
        #前往第 i 篇文章
        driver.get(links[i])
        #搜尋 class 屬性是 news-editor 的所有標籤
        #文章內容
        content=driver.find_element(By.CLASS_NAME, 'news-editor').text
        #將content加入articles陣列
        articles.append(content)

    # for i in range(len(links)):
    #     print(titles[i])
    #     print('網址: ' + links[i])
    #     print('='*30)
    driver.close()

    openai.api_key ='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'#將 key 寫在 .txt 裡面


    # openai.api_key = os.getenv("openai_api_key")

    completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "將以下內容整理成50字的摘要，並使用台灣最常用的正體中文表達:"},
        {"role": "user", "content": articles[0]},
      ]
    )
    ans=completion.choices[0].message

    # 這裡是要傳給 bot 印出來的
    print(today)
    print('加密城市')
    print('Title:')
    print(titles[0])
    print('Summary:')
    print(ans['content'])
    print('Link:')
    print(links[0])
    print('='*10)

main()













