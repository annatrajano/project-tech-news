from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    """Seu código deve vir aqui"""
    query = search_news({"title": {"$regex": title, "$options": "-i"}})
    results = []
    for news in query:
        results.append((news["title"], news["url"]))
    return results


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    query = search_news({"tags": {"$regex": tag, "$options": "-i"}})
    results = []
    for news in query:
        results.append((news["title"], news["url"]))
    return results


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    query = search_news(
        {"category": {"$regex": category, "$options": "-i"}}
    )
    results = []
    for news in query:
        results.append((news["title"], news["url"]))
    return results
