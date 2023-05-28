# 載入 selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# openai 相關模組
import os
import openai

#設定 driver 位置
options=Options()
options.chrome_executable_path='C:\\Users\\user\\Desktop\\chromedriver.exe'
# 建立 driver 物件實體，用程式操作瀏覽器
driver = webdriver.Chrome(options=options)
# 前往指定網址，網頁連線
driver.get("https://www.cryptocity.tw/")
#取得網頁原始碼
#print(driver.page_source)

# 建一個 list 存 link
links=[]
# 存 文章列表
articles=[]

#搜尋 class 屬性是 news-text d-flex jc-start ac-center flex-wrap 的所有標籤
tags=driver.find_elements(By.CLASS_NAME, 'news-text.d-flex.jc-start.ac-center.flex-wrap') #類別名稱定位 

# 先爬每個文章的連結
for tag in tags:
    #取得標籤中的超連結
    #(返回第一個出現 a 標籤)
    link=tag.find_element(By.TAG_NAME, 'a').get_attribute('href') #標籤定位 
    #將link加入links陣列
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


driver.close()

print(articles)






# openai.api_key ='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'#將 key 寫在 .txt 裡面


# # openai.api_key = os.getenv("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")

# completion = openai.ChatCompletion.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "user", "content": "Hello!"}
#   ]
# )
# print(completion.choices[0].message)

