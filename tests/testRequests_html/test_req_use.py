from requests_html import user_agent, HTMLSession
from taoSpider import stringUtils

# 1指定url
url = 'https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-14606070172.31.13376051UKY7qX&id=593514799346'

# 2构造headers
headers = {'User-Agent': user_agent(),
           }

# 3构造cookieJar
cookieStr = 't=e1c3199fa6f89c397483d456a9465524; cna=7EJVFXXbvToCATyxue2AH6px; tg=0; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=%5Cu9633835455; lgc=%5Cu9633835455; enc=nmmXXOdshiIK7VJ5bKQBIHbKFBDwzIbTdaH57AbfWmqerm2LNlapdI6Et4VJtV2nsd%2BU79MLUdHjqMbaJvNbUQ%3D%3D; x=681711433%26e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; mt=ci=23_1&np=; v=0; cookie2=1daed13e76a92894ffe8e5c9214e0ee6; _tb_token_=31e85e3ae534f; unb=1706845563; sg=538; _l_g_=Ug%3D%3D; skt=1a12033c3a57611d; cookie1=BxvAfhJKXE88fjwdsTj%2Bid2YbgqwSIiZKlJxbQBiCcU%3D; csg=20626f97; uc3=vt3=F8dByEa%2Fysy8MZRcbLs%3D&id2=UoYekxLW0zUv9g%3D%3D&nk2=svsV7fzyZuw%3D&lg2=VT5L2FSpMGV7TQ%3D%3D; existShop=MTU1NzMwMTQxMg%3D%3D; _cc_=U%2BGCWk%2F7og%3D%3D; dnk=%5Cu9633835455; _nk_=%5Cu9633835455; cookie17=UoYekxLW0zUv9g%3D%3D; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=Vq8l%2BKCLjhS4UhJVbhgU&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTZ48ZuF6lLeQ%3D%3D&tag=8&lng=zh_CN; swfstore=211839; _m_h5_tk=f1fe5d2ac576b200b264b8624cc84ea1_1557310183852; _m_h5_tk_enc=8756cb2131cb8ad811ef93b786f74d11; isg=BP7-BVQ9LnsPiXpCTnzEoqTuTx2Al8PAvKqF6agHasE8S54lEM8SySSqw1ci87rR; l=bBTm-uquvDZjlqspBOCg5uI8LA7OSIRAguPRwCVvi_5pR6T_Lx_OlKy_rF96Vj5R_TYB4TgKw_v9-etU2; whl=-1%260%260%261557303018026'
cookieJar = stringUtils.cookie_str2jar(cookieStr)

# 4构造session
session = HTMLSession()
session.headers = headers
session.cookies = cookieJar

print(session.cookies)

# 5获取返回响应对象
r = session.get(url)
# print(r.text)
# 6执行js代码

with open('34.html', 'w')as f1:
    f1.write(r.html.html)
# 7提取需要的url路径

# elems = r.html.find('div.detail a')
#
# url_detail = 'https:' + elems[0].attrs['href']
# print(url_detail)
#
# time.sleep(1)
# response = session.get(url_detail)
# response.html.render()
# with open('134.html', 'w')as f1:
#     f1.write(response.html.html)
#
# print(session.cookies)
