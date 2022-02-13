# ps5_scrapper

I just want a PS5!!

Web scrapper developed with Playwright-python (https://playwright.dev/python)


## Installation

It is highly suggested to use into a Python VENV

```sh
python -m venv virtualenv && cd virtualenv && source virtualenv/bin/activate
```

Clone repo and install dependecies and create a .env file

```sh
pip install -r requirements.txt
```
```sh
## ENV FILE
BOT_TOKEN='<Telegram bot token>'
CHAT_ID='<Telegram chat ID>'
```

Lastly, install Playwright browsers bundles

```sh
playwright install
```

## Notes
Tested under Python 3.8
