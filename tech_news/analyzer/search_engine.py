from tech_news.database import search_news

from datetime import datetime


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
    try:
        string_date = datetime.fromisoformat(date).strftime("%d/%m/%Y")
        query = search_news({
            "timestamp": {"$regex": string_date, "$options": "i"}
            })
        return [(article["title"], article["url"])for article in query]
    except ValueError:
        raise ValueError("Data inválida")


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
