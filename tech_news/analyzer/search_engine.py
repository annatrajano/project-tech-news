from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    news_list = search_news({"title": {"$regex": title, "$options": "-i"}})
    titles = []
    for news in news_list:
        titles.append((news["title"], news["url"]))
    return titles


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
