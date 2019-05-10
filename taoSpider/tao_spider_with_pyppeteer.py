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
        'https://shop34504620.taobao.com/search.htm?spm=a1z10.1-c-s.0.0.269b7465iuYHfT&search=y')
    await page.evaluateOnNewDocument('() =>{ Object.defineProperties(navigator,'
                                     '{ webdriver:{ get: () => false } }) }')
    sum = {'num': 0}
    while True:
        await page.evaluate("""
            (function () {
                var y = document.body.scrollTop;
                var step = 100;
                window.scroll(0, y);
                function f() {
                    if (y < document.body.scrollHeight) {
                        y += step;
                        window.scroll(0, y);
                        setTimeout(f, 50);
                    }
                    else {
                        window.scroll(0, y);
                        document.title += "scroll-done";
                    }
                }
                setTimeout(f, 1000);
                })();
            """)
        # await page.evaluate('window.scrollTo(0, document.documentElement.clientHeight);')
        await asyncio.sleep(4)

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
            await asyncio.sleep(3)
            frame = page.frames
            if len(frame) > 0:
                print('滑块找到了')
                print(len(frame))
                print('聚焦滑块')
                await frame[-2].hover('span#nc_1_n1z')
                print('按下滑块')
                await page.mouse.down()
                print('移动滑块')
                await page.mouse.move(2000, 0, {'delay': random.randint(1000, 2000), 'steps': 100})
                print('松开滑块')
                await page.mouse.up()
                await asyncio.sleep(2)
        except PageError:
            print('没有滑块')

        try:
            await page.click('div.grid div.pagination>a.next')
        except PageError:
            print("已经爬取所有...共有" + str(sum['num']) + "条商品")
            break

        print("**********************下一页**************")
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
