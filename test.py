
from openai import OpenAI

def main():
    articles = "jinny是一個很可愛的女孩子，她喜歡吃甜甜圈，她的夢想是成為一個資料科學家，"
    client = OpenAI(
        api_key='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',  
    )

    completion = client.images.generate(
        model="dall-e-3",
        prompt="請根據以下內容產生一張圖片"+articles,
        n=1,
        size="1024x1024"
    )
    # print(completion)
    url = completion.data[0].url
    print(url)

main()
