import requests
from bs4 import BeautifulSoup
import pprint


def ScrapingAllPages():
    full_pages_news = []
    no_pages = [1, 2, 3]
    for page in no_pages:
        res = requests.get("https://news.ycombinator.com/news")
        if page > 1:
            res = requests.get("https://news.ycombinator.com/news?p=" + str(page))
        soup = BeautifulSoup(res.text, "html.parser")

        title = soup.select(".storylink")
        vote = soup.select(".subtext")
        news_list = (filtering_hacker_news(title, vote))
        full_pages_news += news_list
    return sorted(full_pages_news, key=lambda k: k['Vote'], reverse=True)


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
    return news_list


pprint.pprint(ScrapingAllPages())
