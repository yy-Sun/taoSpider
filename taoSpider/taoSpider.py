from requests_html import user_agent, HTMLSession
import requests


def cookie_str2dict(cookie_str):
    """
    将一个cookies字符串转换成dict字典
    :param s: 字符串
    :return: 字典
    """
    # 首先将字符串切割
    cookie_list = cookie_str.split(';')

    # 创建一个空字典
    cookie_dick = {}

    # 将切割后的key value 添加到字典中
    for cookie in cookie_list:
        # 找到key value分割的第一个'='下标
        cookie = cookie.strip(' ')
        index = cookie.index('=')
        cookie_dick[cookie[:index]] = cookie[index + 1:]

    return cookie_dick


def cookie_str2jar(cookie_str):
    cookie_dict = cookie_str2dict(cookie_str)
    return requests.utils.cookiejar_from_dict(cookie_dict)


# 1添加urls
urls = [
    'https://shop34208248.taobao.com/search.htm?spm=a1z10.5-c-s.w4002-12085767654.1.7dfa650dOZBIax&search=y',
    'https://ynuf.aliapp.org/if.htm?hybrid=1', 'https://g.alicdn.com/alilog/oneplus/blk.html']

# 2添加cookies
cookie_str = 't=e1c3199fa6f89c397483d456a9465524; cna=7EJVFXXbvToCATyxue2AH6px; tg=0; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=%5Cu9633835455; lgc=%5Cu9633835455; enc=nmmXXOdshiIK7VJ5bKQBIHbKFBDwzIbTdaH57AbfWmqerm2LNlapdI6Et4VJtV2nsd%2BU79MLUdHjqMbaJvNbUQ%3D%3D; x=681711433%26e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; mt=ci=23_1&np=; _m_h5_tk=f1fe5d2ac576b200b264b8624cc84ea1_1557310183852; _m_h5_tk_enc=8756cb2131cb8ad811ef93b786f74d11; v=0; cookie2=172b01f782c5e4e959307d6f4ccdaed9; _tb_token_=7e3f3b3e7eb7; unb=1706845563; sg=538; _l_g_=Ug%3D%3D; skt=29ce339c0afd5a7e; cookie1=BxvAfhJKXE88fjwdsTj%2Bid2YbgqwSIiZKlJxbQBiCcU%3D; csg=24eaf155; uc3=vt3=F8dByEa%2FysraF271AGM%3D&id2=UoYekxLW0zUv9g%3D%3D&nk2=svsV7fzyZuw%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTU1NzMwMzM5NA%3D%3D; _cc_=URm48syIZQ%3D%3D; dnk=%5Cu9633835455; _nk_=%5Cu9633835455; cookie17=UoYekxLW0zUv9g%3D%3D; swfstore=184214; pnm_cku822=098%23E1hvxpvUvbpvUvCkvvvvvjiPRLSWQjtRRFLZQj3mPmPy6jibR2cpAjt8PsMUljlEiQhvCvvv9UUtvpvhvvvvvUyCvvOUvvhCa6RivpvUvvmvnaXbbD%2FtvpvIvvvvVZCvvROvvU80phvWgvvv96CvpC29vvm25yCvhjpvvU8TphvWr9yCvhQvM5OvCsN%2BFOcn%2B3C1pKFEDaVTRogRD7zwaXTAVArl%2BExrV8tYVVzwafmAdch%2BYExr18TxEcqvafmlHs9lBuV91Wkwe53UARLOlCAZvphvC9vhvvCvpvGCvvpvvPMM; l=bBTm-uquvDZjlMF9BOfgNuI8LA7OfCdf1sPzw4OG7IB1O75iYddvjHwdTx1yK3Q_E_fB2eKPF2hRZRFvyCaSi; isg=BKWllndNFXaPOXE3gTGPn5M7tGgfSlgNSz_OvKePkF6GvsYwbjbWRByUSEJtvnEs; uc1=cookie16=UIHiLt3xCS3yM2h4eKHS9lpEOw%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=Vq8l%2BKCLz3%2F65A%3D%3D&existShop=false&pas=0&cookie14=UoTZ48ZuEELGcQ%3D%3D&tag=8&lng=zh_CN; whl=-1%260%260%261557306498263'
cookies_jar = cookie_str2jar(cookie_str)

# 2.5构建headers
headers = {'User-Agent': user_agent(),
           'referer': 'https://shoucang.taobao.com/shop_collect_list_n.htm?spm=a1z0k.7386009.1997992801.3.758a18f4mGUaCW'}

# 3创建session
session = HTMLSession()
session.headers = headers
session.cookies = cookies_jar

# 4进入所有商品界面（先寻找div.detail a,如果能找到，且大于4个，说明已经在所有商品界面,没有则寻找带‘所有’
r = session.get(urls[0])
session.get(urls[1])
session.get(urls[2])
# 两个字的链接）
# 5下拉到最底层
js = """
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
"""
# js2 = "var q=document.documentElement.scrollTop=100000"
# 将界面拉到底层

r.html.render()
with open('.html', 'w')as f:
    f.write(r.html.html)
# 6翻页
"""
无法渲染js代码,渲染出来的代码有问题，尝试直接使用Pyppeteer
"""
# 7处理下一个url商铺
# 将cookies保存到cookies池
