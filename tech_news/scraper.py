# Docs: https://docs.python.org/3/library/time.html
import time

# Docs: https://docs.python-requests.org/en/master/
import requests

# Docs: https://parsel.readthedocs.io/en/latest/usage.html
from parsel import Selector

from tech_news.database import create_news


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, headers={"user-agent": "Fake user-agent"})
        time.sleep(1)
        if (response.status_code) == 200:
            return response.text
        return None
    except requests.Timeout:
        return None


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    links = selector.css("h2.entry-title a::attr(href)").getall()
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(text=html_content)
    next_page_link = selector.css(".next.page-numbers::attr(href)").get()
    return next_page_link if (next_page_link) else None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""
    selector = Selector(html_content)
    url = selector.css("head link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").re_first(r"\d{2}/\d{2}/\d{4}")
    writer = selector.css(".author a::text").get()
    comments_count = (
        selector.css(".post-comments h5::text").re_first(r"\d+") or 0
    )
    summary = selector.xpath(
        'string(//div[@class="entry-content"]/p[1])'
    ).getall()[0]
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css(".category-style .label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary.rstrip(),
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    url = fetch("https://blog.betrybe.com")
    list = scrape_novidades(url)
    count = 0
    results = []
    while len(list) < amount:
        next = scrape_next_page_link(url)
        url = fetch(next)
        list.extend(scrape_novidades(url))

    while count < amount:
        article = fetch(list[count])
        results.append(scrape_noticia(article))
        count += 1

    create_news(results)
    return results

