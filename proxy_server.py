from flask import Flask, request, Response
import requests
from bs4 import BeautifulSoup

from conf import HACKER_NEWS_URL

app = Flask(__name__)

BASE_URL = HACKER_NEWS_URL


def modify_text(text):
    words = text.split()

    modified_words = [word + '™' if len(word) == 6 and word.isalpha() else word for word in words]
    return ' '.join(modified_words)


def modify_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    for element in soup.find_all(string=True):
        if element.parent.name not in ['script', 'style']:
            element.replace_with(modify_text(element))

    return str(soup)


@app.route('/item')
def proxy():
    item_id = request.args.get('id')
    url = f'{BASE_URL}/item?id={item_id}'

    try:
        response = requests.get(url)
        response.raise_for_status()

        modified_content = modify_html(response.content.decode('utf-8'))

        return Response(modified_content, content_type='text/html; charset=utf-8')

    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


if __name__ == '__main__':
    app.run(port=8232)
