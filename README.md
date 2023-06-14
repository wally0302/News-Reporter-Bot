# 新聞播「Bot」員

## Concept Development
我們意識到現今資訊大爆炸的時代中，使用者常常面臨一個問題：想要看新聞卻不知道從何看起。當他們進行搜尋時，總是被一大堆不同網站的新聞所淹沒，而每個新聞網站又擁有數十篇的新聞，使得使用者不得不花費大量時間去閱讀和篩選。

為了解決這個問題，我們提出了一個創新的解決方案：透過 **Telegram bot 自動推送每日新聞大綱給予使用者**。我們的目標是讓使用者能夠輕鬆地獲取當天的新聞概要，並清楚地知道每則新聞的內容。

這次選擇的網站為 : [The Hacker News](https://thehackernews.com/)
## Function
- ![](https://hackmd.io/_uploads/rJTPu3Mvn.png)
    - 將爬蟲的新聞資料透過 Chatgpt 整理成為簡短的大綱，並利用 Telegram bot 當媒介，定時將每天的新聞大綱傳輸給使用者，方便使用者讀取。
## Implementation Resources
- 使用 Linux Ubuntu 作業系統
- 爬蟲：BeautifulSoup
- Docker
- Telegram bot
- ChatGPT
- AWS (option)
## Implementation Process
### Docker
1. 在 AWS EC2 中的 Linux 安裝 Docker
    - `sudo apt-get update -y`
    - `sudo apt-get install -y curl`
    - `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
    - `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
    - `sudo apt-get install -y docker-ce`
3. 安裝 Dockercompose
    - `sudo apt-get update`
    - `sudo apt-get install docker-compose-plugin`
    - `sudo apt install docker-compose`
### OpenAI
1. 註冊一個 OpenAI API key ([OpenAI API網址](https://platform.openai.com/signup))
2. 點擊右上角 Upgrade
    - ![](https://hackmd.io/_uploads/H16MG7Jw2.png)
3. 點擊左下角 API Key 進入
    - ![](https://hackmd.io/_uploads/S1A4fX1Dn.png)
4. 點擊 Create new secret key 申請一個新的密鑰
    - ![](https://hackmd.io/_uploads/BJGcf7kw2.png)
5. 申請完成可以看到自己多了一個 secret key
    - ![](https://hackmd.io/_uploads/SJ7Hm7kD2.png)
### Telegram bot
1. 在 telegram 中搜尋， [@BotFather](https://t.me/BotFather)
    - ![](https://hackmd.io/_uploads/BJ10vsMP2.png) 
- ![](https://hackmd.io/_uploads/SJVOFiMD2.png)
## Usage
1. 下載 GitHub 專案
    - `git clone https://github.com/wally0302/LSA_final`
2. `cd LSA_fianl/`
3. 去 `.env`修改成自己的 openai Key & telegram bot key
    - ![](https://hackmd.io/_uploads/SkT34oMw3.png)
4. 可以去 `climb.py` 修改 prompt
    - ![](https://hackmd.io/_uploads/ByBnriGP2.png)
5. 可以以去 `telebot.py` 修改 發送時間
    - ![](https://hackmd.io/_uploads/BkmBZ2Gvn.png) 
6. 建立 image :`docker-compose build`
7. 啟動 : `docker-compose up`
## Demo

## Problem
- selenium 問題
    - 原先在爬蟲，我們使用的是 Selenium，但後來測試時發現執行起來速度太慢，運行起來很卡，因此替換成 BeautifulSoup
- OpenAI 問題
    - 因一個 Key 的上限為 5 美元，因此執行時需消耗大量的 OpenAI Key，沒辦法一直重複測試（除非一直重新申請 OpenAI Key）

- 一開始在本機跑程式可以執行成功，但後來放去 Container 裡面，就發現他永遠跑不動...
    - 後來發現是因為 Container 時區不一致 :-1: 
        - ![](https://hackmd.io/_uploads/HyqGBMMv2.png)
    - 解決 : 
        - 編輯 `docker-compose.yml` ， 將主機的時區掛載到容器中
            - ![](https://hackmd.io/_uploads/HyXmwGMD2.png) 
    - 但後來想在 aws 上執行，發現時區也不一致
        - ![](https://hackmd.io/_uploads/H1NQAffv2.png)
    - 解決 : 
        - 編輯 `docker-compose.yml` ，加入您所在的時區
            - ![](https://hackmd.io/_uploads/H19VCzfvh.png)
 



## Thankful
- 惠霖學姊
- 柏瑋學長
## Job Assignment
| 組員| 工作分配|
| -------- | -------- |
| 黃郁庭    | 程式撰寫、文件     | 
| 張可葭    | telegram bot、文件     | 

## References
- [Telegram bot](https://oscarada87.github.io/2019/05/25/%E7%94%A8-Python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84-Telegram-Bot/)
- [How to create telegram bot](https://www.toptal.com/python/telegram-bot-tutorial-python)
- [BeautifulSoup](https://www.learncodewithmike.com/2020/02/python-beautifulsoup-web-scraper.html)
- [OpenAI](https://levelup.gitconnected.com/how-to-get-started-with-openai-in-python-758d3db5f25b)
