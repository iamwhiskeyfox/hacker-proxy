from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

from conf import HACKER_NEWS_URL

app = Flask(__name__)


def modify_text(text):
    words = re.findall(r'\b\w{6}\b', text)
    for word in words:
        modified_word = word + '™'
        text = text.replace(word, modified_word, 1)
    return text


def modify_html(html, base_url):
    soup = BeautifulSoup(html, 'html.parser')
    for element in soup.find_all(string=True):
        if element.parent.name not in ['script', 'style']:
            element.replace_with(modify_text(element))
        elif element.parent.name == 'script' and 'src' in element.parent.attrs:
            element.parent['src'] = urljoin(base_url, element.parent['src'])

    for tag in soup.find_all(['img', 'link', 'script'], src=True):
        tag['src'] = urljoin(base_url, tag['src'])

    for tag in soup.find_all('link', href=True):
        tag['href'] = urljoin(base_url, tag['href'])

    return str(soup)


def fetch_and_modify(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        modified_content = modify_html(response.content.decode('utf-8'), url)

        return Response(modified_content, content_type='text/html; charset=utf-8')

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


@app.route('/')
def index():
    return fetch_and_modify(HACKER_NEWS_URL)


@app.route('/item')
def item():
    item_id = request.args.get('id')
    item_url = f'{HACKER_NEWS_URL}/item?id={item_id}'
    return fetch_and_modify(item_url)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8232)
