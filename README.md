# 新聞播「Bot」員

## Concept Development
- 常常想要看新聞但不知道要看哪一篇，搜索時總是會跳出一大堆不同網站的新聞，且每個新聞網站又有幾十篇的新聞。
- 我們希望透過使用 Telegram bot 每天自動推送今日新聞大綱給予使用者，使用者只需要觀看簡短的文字，就知道今日有哪些新聞且分別在講什麼新聞。
## Function
- 將爬蟲的新聞資料透過 Chatgpt 整理成為簡短的大綱，並且如果是外文新聞網站，可同時進行大綱翻譯。利用 Telegram bot 當媒介，定時將每天的新聞大綱傳輸給使用者，方便使用者讀取及選取新聞。
## Implementation Resources
- 使用 Linux Ubuntu 作業系統
- 爬蟲：BeautifulSoup
- Docker
    - 使用 Dockerfile 方便部署，讓要執行專案的環境，在自己的電腦可以跑，也讓它在任何地方都可以跑，只需要下幾行簡單指令就可以跑，不需要繁瑣的安裝流程，方便其他使用者使用
- Telegram bot
- ChatGPT
- AWS
    - EC2：Amazon Elastic Compute Cloud (Amazon EC2)
        - 擴充雲端運算能力及速度，方便開發人員快速的開發及部署應用程式
    - S3：Amazon Simple Storage Service (Amazon S3)
        -  提供儲存功能，且具有良好的安全性及擴充性
    - IAM：AWS Identity and Access Management (IAM)
        - 為一種 Web 服務，能夠控制其餘使用者對 AWS 的存取，集中管理並授權給允許取用其中資料的使用者
    - 應用：
        - 使用 EC2 架設一個 Linux 虛擬機，並將虛擬機中產生的輸出（如下圖）儲存成為一個、 Json 檔案，將 Json 黨儲存在 S3 中，如有使用者要使用此檔案，需透過 IAM 驗證機制，通過後才能使 EC2 中的虛擬機並跟 S3 做結合。
        -  ![](https://hackmd.io/_uploads/BJSmb_i82.png)
        - ![](https://hackmd.io/_uploads/SyUHZdiU3.png)
## Implementation Process
### AWS
1. 進入 [AWS 註冊網站](https://portal.aws.amazon.com/billing/signup#/start/email) 註冊一個帳號
2. 創立一個使用者
3. 建立 EC2
    - ![](https://hackmd.io/_uploads/SJ7L1V1Dn.png)
4. 在其中啟動 Linux 主機
### Docker
1. 在 AWS EC2 中的 Linux 安裝 Docker
2. 輸入以下指令：
    - `sudo apt-get update -y`
    - `sudo apt-get install -y curl`
    - `curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -`
    - `sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"`
    - `sudo apt-get install -y docker-ce`
3. 安裝 Dockercompose
    - `sudo apt-get update`
    - `sudo apt-get install docker-compose-plugin`
    - `sudo apt install docker-compose`
    - `docker compose version`
4.  編寫一個 dockercompose
```dockerfile=
version: "3"
services:
  chrome:
    image: selenium/standalone-chrome
    shm_size: 2gb
    ports:
      - "4444:4444"
      - "7900:7900"
    # environment:
    #   - SE_VNC_NO_PASSWORD=1 # NO_PASSWORD
    #   - SE_VNC_VIEW_ONLY=1   # readonly
```
5. 啟動 docker compose
    - `docker-compose -f docker-compose-standalone-chrome.yml up -d`
    - `sudo docker container ls` 
    - ![](https://hackmd.io/_uploads/S17Ebu4U3.png)
6. 編寫一個 dockerfile
```dockerfile=
# 使用基於Python的映像作為基礎
FROM python:3

# 安裝所需的庫
RUN pip install selenium


# 複製Python代碼到容器中
COPY script.py /app/script.py

# 在容器中運行Python代碼
CMD python3 /app/script.py
``` 
7. 使用 dockerfile 將檔案包成一個 image 
    - `docker build -t test003 .`
8. 利用 image 啟動一個 container 執行爬蟲程式
    - `docker run --network=host test003` 
9. 放到 dockerHub 上
    - 登入 : `docker login`
    - `docker tag 06f96032d5df oaowally/test:1.0` 
    - `docker push oaowally/test:1.0`
    - ![](https://hackmd.io/_uploads/S1QOSt4L2.png)
### OpenAI
1. 註冊一個 OpenAI API key，可從以下網址進入
    - [OpenAI API](https://platform.openai.com/signup)
2. 點擊右上角 Upgrade
    - ![](https://hackmd.io/_uploads/H16MG7Jw2.png)
3. 點擊左下角 API Key 進入
    - ![](https://hackmd.io/_uploads/S1A4fX1Dn.png)
4. 點擊 Create new secret key 申請一個新的密鑰
    - ![](https://hackmd.io/_uploads/BJGcf7kw2.png)
5. 申請完成可以看到自己多了一個 secret key
    - ![](https://hackmd.io/_uploads/SJ7Hm7kD2.png)
6. 下載 OpenAI 套件 `pip install openai`
### BeautifulSoup
- `pip install beautifulsoup4`
- `pip install requests`
### Telegram bot
- 在 telegram 中尋找 [@BotFather](https://t.me/BotFather)
- ![](https://hackmd.io/_uploads/B1bUabywn.png)
- 進入後在對話筐輸入 `/newbot`
- 輸入 bot 名稱
- 輸入 username
- 會回傳 bot 的 tocken，**要記得記下且不要外傳！**
- ![](https://hackmd.io/_uploads/r1TSRbyv3.png)
- 在 terminal 中下載 Telegram bot 套件
    - `pip install python-telegram-bot`

## Usage
1. 下載 GitHub 專案
    - `git clone https://github.com/wally0302/LSA_final`
2. `cd LSA_fianl/`
3. `cd __pycache__/`
4. 
5. 修改檔案：
    - 替換 OpenAi API Key
        - openai.api_key ='**輸入你 openai api key**'
    - 如果要修改整理成大綱的字數或翻譯的語言，修改以下段落
        - messages=[{"role": "system", "content": "將以下內容整理成**100**（可修改）字的摘要，並使用**台灣最常用的正體中文**（可修改）表達:"}] 

- 加入好友 `GPTArticleSummary_bot.`
    - ![](https://hackmd.io/_uploads/Byn3KoZvn.png)
## Code
### 爬蟲
```python=
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
```
### OpenAi
```python=
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
```
## Demo Viedo
## Problem
- selenium 問題
    - 原先在爬蟲，我們使用的是 Selenium，但後來測試時發現執行起來速度太慢，運行起來很卡，因此替換成 BeautifulSoup
- OpenAI 問題
    - 因一個 Key 的上限為 5 美元，因此執行時需消耗大量的 OpenAI Key，沒辦法一直重複測試（除非一直重新申請 OpenAI Key）

- 一開始在本機跑程式可以執行成功，但後來放去 Container 裡面，就發現他永遠跑不動...
    - 後來發現是因為 Container 時區不一致 :-1: 
        - ![](https://hackmd.io/_uploads/HyqGBMMv2.png)
    - 解決
        - 將主機的時區掛載到容器中
            - ![](https://hackmd.io/_uploads/HyXmwGMD2.png) 
    - 但後來想在 aws 上執行，發現 時區也不一致
        - ![](https://hackmd.io/_uploads/H1NQAffv2.png)
    - 解決
        - ![](https://hackmd.io/_uploads/H19VCzfvh.png)
 



## Thankful
- 惠霖學姊
- 柏瑋學長
## Job Assignment
## References
- [Telegram bot](https://oscarada87.github.io/2019/05/25/%E7%94%A8-Python-%E6%89%93%E9%80%A0%E8%87%AA%E5%B7%B1%E7%9A%84-Telegram-Bot/)
- [How to create telegram bot](https://www.toptal.com/python/telegram-bot-tutorial-python)
- [schedule](https://schedule.readthedocs.io/en/stable/)
- [BeautifulSoup](https://www.learncodewithmike.com/2020/02/python-beautifulsoup-web-scraper.html)
- [OpenAI](https://levelup.gitconnected.com/how-to-get-started-with-openai-in-python-758d3db5f25b)
- [EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html)
- [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

## 如何啟動
- `git clone https://github.com/wally0302/LSA_final.git`
- `docker-compose build`
- `docker-compose up`