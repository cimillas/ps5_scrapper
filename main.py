import asyncio, requests, os
from dotenv import load_dotenv
from playwright.async_api import async_playwright
from target import PlayWrightTarget



bot_token = ''
chat_id = ''

targets = [
    PlayWrightTarget('FNAC','https://www.fnac.es/Consola-PlayStation-5-Videoconsola-Consola/a7724798', '.js-articleOffers', 'Artículo no disponible en web'),
    PlayWrightTarget('Game', 'https://www.game.es/consola-playstation-5-playstation-5-183224', '.product-quick-actions', 'Producto no disponible'),
    PlayWrightTarget('PcComponentes','https://www.pccomponentes.com/sony-pack-playstation-5-edicion-digital-dualsense-midnight-black', '#buy-buttons-section','Avísame'),
    PlayWrightTarget('El Corte Inglés','https://www.elcorteingles.es/videojuegos/A37046604-consola-playstation-5/', '#js_add_to_cart_desktop', 'Agotado temporalmente'),
    PlayWrightTarget('Media Markt','https://www.mediamarkt.es/es/product/_consola-sony-ps5-825-gb-4k-hdr-blanco-1487016.html','[id="pdp-add-to-cart-button"]', None),
    PlayWrightTarget('Amazon', 'https://www.amazon.es/Playstation-Consola-PlayStation-5/dp/B08KKJ37F7','#add-to-cart-button', None)
    ]

def load_vars():
    load_dotenv()
    bot_token = os.environ.get('BOT_TOKEN')
    chat_id = os.environ.get('CHAT_ID')

async def send_telegram_message(message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + message
    response = requests.get(send_text)
    return response.json()

async def main():
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        for target in targets:
            if await target.check_vendor(browser):
                print(await send_telegram_message("HAY PS5 EN {} 😍".format(target.vendor)))

#Cloud functions require a function entrypoint
def init_cloud_func():
    load_vars()
    asyncio.run(main())

#For other executions (not cloud functions or similar)
if __name__ == "__main__":
    load_vars()
    asyncio.run(main())
