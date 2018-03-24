import requests
from bs4 import BeautifulSoup


def extract_news(parser):
    """ Extract news from a given web page """
    news_list = []
    inner_table = parser.findAll('tr', {'class': 'athing'}) # все новости начинаются с этой tr
    subtexts = parser.findAll('td', {'class': 'subtext'}) # вторая строка новости (комменты,поинты,автор )
    for i in range(len(inner_table)):
        news = {'author': parser.findAll('a', {'class': 'hnuser'})[i].text,
               'title': parser.findAll('a', {'class': 'storylink'})[i].text,
                'comments': subtexts[i].findAll('a')[-1].text,
                'points': parser.findAll('span', {'class' : 'score'})[i].text,
                'url':  parser.findAll('a', {'class': 'storylink'})[i]['href']}
        news_list.append(news)
    return news_list


def extract_next_page(parser):
    more_link = parser.findAll("a", {'class': 'morelink'})[0]['href']
    return more_link


def get_news(url, n_pages):
    """ Collect news from a given web page """
    news = []
    while n_pages:
        print("Collecting data from page: {}".format(url))
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        news_list = extract_news(soup)
        next_page = extract_next_page(soup)
        url = "https://news.ycombinator.com/" + next_page
        news.extend(news_list)
        n_pages -= 1
    return news
