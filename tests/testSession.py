'''
测试session回话cookies
'''

import requests
from taoSpider.utils import stringUtils

try:
    from lxml import etree

    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree

        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree

            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree

                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree

                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")
cookie_str = 'ctoken=7gmxxOPhIYdd8Mtl5gWLigiA; cna=IvpVFYuB6msCATpltpRSISG4; t=fd0a1a2dcd9b89d22deed36c62c79dec; _m_h5_tk=d12dd765137d8b06465136643832e483_1557171451033; _m_h5_tk_enc=b7c7e80eb28c9116b4859a6938f5f825; cookie2=12a00ac3f8674a3045f79b6021708d7c; v=0; _tb_token_=ea616e36566ee; unb=1706845563; sg=538; _l_g_=Ug%3D%3D; skt=f19ed21af77b5fbd; cookie1=BxvAfhJKXE88fjwdsTj%2Bid2YbgqwSIiZKlJxbQBiCcU%3D; csg=6d4e2c64; uc3=vt3=F8dByEawOVR7XC%2BQB%2Fw%3D&id2=UoYekxLW0zUv9g%3D%3D&nk2=svsV7fzyZuw%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTU1NzE2MzE5OA%3D%3D; tracknick=%5Cu9633835455; lgc=%5Cu9633835455; _cc_=UIHiLt3xSw%3D%3D; dnk=%5Cu9633835455; _nk_=%5Cu9633835455; cookie17=UoYekxLW0zUv9g%3D%3D; tg=0; mt=ci=22_1; thw=cn; uc1=cookie14=UoTZ48QDi0R8CQ%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&tag=8&cookie15=W5iHLLyFOGW7aA%3D%3D&pas=0; l=bBSa3tGcvDMzTD_QBOfNNuI-5R7tNIOb4sPzw41agICP_o1959lhWZ9AJJ8pC3GVw18wR3WSJbCuBeYBY5f..; isg=BBISzLbamn0UROYBYHjR5Nl2Y9E0iws8oI75ldxqFkWw77PpxLbnzUyFXwv2n45V'

# cookie_dict = stringUtils.cookie_str2dict(cookie_str)

# 1获取百度的返回对象request
url = 'https://uland.taobao.com/sem/tbsearch?refpid=mm_26632258_3504122_32538762&keyword=%E5%A5%B3%E8%A3%85&clk1=c2c2c5f851778441c1eef9a892b196f5&upsid=c2c2c5f851778441c1eef9a892b196f5'
headers = {
    'referer': 'https://login.taobao.com/member/login.jhtml?spm=a2e15.8261149.754894437.1.275229b4oRjJRD&f=top&redirectURL=https%3A%2F%2Fuland.taobao.com%2Fsem%2Ftbsearch%3Frefpid%3Dmm_26632258_3504122_32538762%26keyword%3D%25E5%25A5%25B3%25E8%25A3%2585%26clk1%3Dc2c2c5f851778441c1eef9a892b196f5%26upsid%3Dc2c2c5f851778441c1eef9a892b196f5',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
}

session = requests.session()
session.headers = headers
cookie_jar = stringUtils.cookie_str2jar(cookie_str)
session.cookies = cookie_jar  # 这一步只能添加cookieJar
request = session.get(url)

# 将返回对象保存成HTML
with open('.html', 'w')as f:
    f.write(request.text)

# 2将返回对象的text转成HTML对象
html = etree.HTML(request.content.decode('utf8'))

# 3获取‘时尚女装’的链接url
li_list = html.xpath('//ul[@mx-guid="g1mx_8"]')
print(li_list)
# cla_div = html.xpath('//div')
test = html.xpath('//div[@id="J_stextlink"]')
print(test)

# print(test)
# print(li_list)
# seconde_urls = []
# for dd in li_list:
#     url = dd.xpath('./a/@href')
#     seconde_urls.append(url)
#
# print(seconde_urls)
