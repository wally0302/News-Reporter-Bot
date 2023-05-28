# 載入 selenium 相關模組
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
#設定 driver 位置
options=Options()
options.chrome_executable_path='C:\\Users\\user\\Desktop\\chromedriver.exe'
# 建立 driver 物件實體，用程式操作瀏覽器
driver = webdriver.Chrome(options=options)
# 前往指定網址，網頁連線
driver.get("https://www.ptt.cc/bbs/Stock/index.html")
#取得網頁原始碼
#print(driver.page_source)

#搜尋 class 屬性是 title 的所有標籤
tags=driver.find_elements(By.CLASS_NAME, 'news-text d-flex jc-start ac-center flex-wrap') #類別名稱定位 
# print(tags)

#逐一取出標籤內容
for tag in tags:
    #取得標籤中的文字
    title=tag.text
    #取得標籤中的超連結
    #(返回第一個出現 a 標籤)
    # link=tag.find_element(By.TAG_NAME, 'a').get_attribute('href') #標籤定位 
    print(title)
    # print(link)
    print('=====================')


driver.close()
