import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get("https://news.ycombinator.com/news")
soup = BeautifulSoup(res.text, "html.parser")

title = soup.select(".storylink")
vote = soup.select(".subtext")



def filtering_hacker_news(title, vote):
    news_list = []
    for index, item in enumerate(title):
        url = title[index].get("href")
        point = vote[index].find(class_="score")
        if point:
            current_vote = int(point.getText().replace(" points", ""))
            if current_vote > 99:
                current_news = {'Title': item.getText(), 'Link': url, 'Vote': current_vote}
                news_list.append(current_news)
    return sorted(news_list, key=lambda k: k['Vote'], reverse=True)



pprint.pprint((filtering_hacker_news(title, vote)))
