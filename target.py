import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

'''
2 different cases:
    (A) Search a common element and check it has out of stck text
    (B) Find an element that points that product is available -> outStockText = null
'''

class PlayWrightTarget:

    def __init__(self, vendor, url, checkElement, outStockText):
        self.vendor = vendor
        self.url = url
        self.checkElement = checkElement
        self.outStockText = outStockText


    async def check_vendor(self, browser):
        page = await browser.new_page()
        await page.goto(self.url, wait_until="commit") #Default until load generate timeout in Amazon

        try:
            web_element = await page.text_content(self.checkElement, timeout=10000)
        except PlaywrightTimeoutError: # If web_element is not found, it is case B with no stock
            await page.close()
            return False

        if self.outStockText is not None: #CASE A
            if self.outStockText in web_element:
                await page.close()
                return False

        await page.close()
        return True