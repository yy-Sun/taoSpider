import asyncio
from pyppeteer import launch
from pyppeteer.errors import PageError
import time
import random
from retrying import retry

width, height = 1366, 768


def retry_if_result_none(result):
    return result is None


@retry(retry_on_result=retry_if_result_none, )
async def mouse_slide(page=None, frame=None):
    await asyncio.sleep(2)
    try:
        # 鼠标移动到滑块，按下，滑动到头（然后延时处理），松开按键
        if frame:
            await frame.hover('#nc_1_n1z')
        else:
            await page.hover('#nc_1_n1z')
        await page.mouse.down()
        await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
        await page.mouse.up()
    except Exception as e:
        print(e, ':验证失败')
        return None, page


async def main():
    browser = await launch(headless=False, userDataDir='./userdata/15071272297',
                           args=['--disable-infobars', f'--window-size={width},{height}'])
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})

    await page.goto(
        'https://shop136813853.taobao.com/category.htm?spm=a1z10.1-c.w4010-12442053236.2.4f993705PohR5j&search=y')
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                     '{ webdriver:{ get: () => false } }) }')
    sum = {'num': 0}
    while True:
        # await page.evaluate("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(1.7)

        # title = await  page.xpath('')
        item = {}
        details = await page.xpath('//dd[@class="detail"]')
        for detail in details:
            title = await detail.xpath('./a')
            item['title'] = await (await title[0].getProperty("textContent")).jsonValue()
            item['title'] = item['title'].strip(' \n')
            price = await detail.xpath('./div[@class="attribute"]/div/span[@class="c-price"]')
            item['price'] = await (await price[0].getProperty("textContent")).jsonValue()
            # price_str = await page.evaluate('(element) => element.textContent', price)
            print(item)
            sum['num'] = sum['num'] + 1
            # price_str = await page.evaluate('(element) => element.textContent', price)
            print("..................................")

        try:
            await page.click('div.pagination a.next')
        except PageError:
            print("已经爬取所有...共有" + str(sum['num']) + "条商品")
            break

        try:
            await page.waitFor(6)
            frame = await page.Jeval('#sufei-dialog-content')
            await frame.hover('#nc_1_n1z')
            await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000)})
            await page.mouse.up()

            print('滑块找到了')
        except PageError:
            print('滑块找不到')
        print("**********************下一页**************")
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
