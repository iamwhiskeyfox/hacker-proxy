# Прокси-сервер для Hacker News

Этот проект представляет собой простой HTTP-прокси-сервер для отображения содержимого страниц Hacker News с модификацией текста.

## Установка

1. Установите зависимости, запустив следующую команду:

    ```bash
    pip install -r requirements.txt
    ```

2. Запустите прокси-сервер:

    ```bash
    python proxy_server.py
    ```

   Прокси-сервер будет доступен по адресу `http://127.0.0.1:8232`.

## Запуск тестов

1. Убедитесь, что прокси-сервер не запущен или остановите его, если он работает.

2. Запустите тесты с помощью следующей команды:

    ```bash
    python test_proxy_server.py
    ```

   Тесты проверяют базовую функциональность сервера.

## Использование

После успешного запуска сервера, вы можете обратиться к нему через веб-браузер или другие HTTP-клиенты, используя адрес `http://127.0.0.1:8232/item?id=13713480`.

Прокси-сервер модифицирует текст на страницах Hacker News, добавляя значок "™" после каждого слова из шести букв.

Пример: [http://127.0.0.1:8232/item?id=13713480](http://127.0.0.1:8232/item?id=13713480)


__________________________

# Hacker News Proxy

This project is a simple HTTP proxy server designed to display the content of Hacker News pages with text modification.

## Installation

1. Install dependencies by running the following command:

    ```bash
    pip install -r requirements.txt
    ```

2. Start the proxy server:

    ```bash
    python proxy_server.py
    ```

   The proxy server will be available at `http://127.0.0.1:8232`.

## Running Tests

1. Ensure that the proxy server is not running or stop it if it is.

2. Run the tests using the following command:

    ```bash
    python test_proxy_server.py
    ```

   The tests validate the basic functionality of the server.

## Usage

After successfully starting the server, you can access it through a web browser or other HTTP clients using the address `http://127.0.0.1:8232/item?id=13713480`.

The proxy server modifies the text on Hacker News pages by adding the "™" symbol after each six-letter word.

Example: [http://127.0.0.1:8232/item?id=13713480](http://127.0.0.1:8232/item?id=13713480)
