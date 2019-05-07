from requests_html import user_agent, HTMLSession
from taoSpider.utils import stringUtils
import time

# 1指定url
url = 'https://shop102995940.taobao.com/shop/view_shop.htm?spm=a1z0k.7386009.1997989141.2.180818f4Y4f7cr&shop_id=102995940'

# 2构造headers
headers = {'User-Agent': user_agent(),
           'Referer': 'https://shoucang.taobao.com/shop_collect_list.htm?spm=a1z0k.6846577.1130980037.1.4e2e37deesP3wT'}

# 3构造cookieJar
cookieStr = 'swfstore=180681; t=e1c3199fa6f89c397483d456a9465524; cna=7EJVFXXbvToCATyxue2AH6px; tg=0; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; tracknick=%5Cu9633835455; lgc=%5Cu9633835455; enc=nmmXXOdshiIK7VJ5bKQBIHbKFBDwzIbTdaH57AbfWmqerm2LNlapdI6Et4VJtV2nsd%2BU79MLUdHjqMbaJvNbUQ%3D%3D; x=681711433%26e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; cookie2=12aa9f85da9fc0ecb29166accc42b4ea; _tb_token_=3981951ab513e; dnk=%5Cu9633835455; _m_h5_tk=4783c2d421acba9fb277e85806f9b72e_1557204364965; _m_h5_tk_enc=c937b3871292892bb7f2ba0a22e92b01; swfstore=20098; pnm_cku822=098%23E1hvH9vUvbpvUvCkvvvvvjiPRLSU1jYUn2cwsj1VPmPZljimPsdOsjYWR2LWsjEvvphvC9vhvvCvpvyCvhQp5jUvCscpAb2XrqpyCW2%2BFO7t%2BeCZTWex6fItb9TxfwLvdig0747B9Wv7%2B3%2Bu1jc6D46fjLVxfwLwdit07ixr1RoK55EJD7zhl8TJKphv8vvvvUlvpvvnvvm25yCv2nOvvUnvphvpgvvv9ttvpCC6vvm25yCvhjoEvpvVmvvCvca2uphvmvvv92cBqpmD2QhvCvvvMMGtvpvhvvvvv8wCvvpvvUmm; unb=1706845563; sg=538; _l_g_=Ug%3D%3D; skt=c632ccae6310599a; cookie1=BxvAfhJKXE88fjwdsTj%2Bid2YbgqwSIiZKlJxbQBiCcU%3D; csg=5d7f24c1; uc3=vt3=F8dByEa%2Fw%2BP3BurhLWw%3D&id2=UoYekxLW0zUv9g%3D%3D&nk2=svsV7fzyZuw%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTU1NzIxNDg2Mg%3D%3D; _cc_=W5iHLLyFfA%3D%3D; _nk_=%5Cu9633835455; cookie17=UoYekxLW0zUv9g%3D%3D; mt=ci=23_1&np=; uc1=cookie16=VFC%2FuZ9az08KUQ56dCrZDlbNdA%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=VFC%2FuZ9ayeYq2g%3D%3D&existShop=false&pas=0&cookie14=UoTZ48eLzHChGg%3D%3D&tag=8&lng=zh_CN; l=bBTm-uquvDZjllTCBOCNquI8LA79AIRAguPRwCVvi_5CU681gFQOlKtuHFJ6Vj5RsA8B4TgKw_v9-etej; isg=BHd3GQ6_558jnWMNL1_dZVX9BmIBlErnzbk8Zskkt8ateJe60Q4V76BSXpiDkCMW; whl=-1%260%260%261557214970403'
cookieJar = stringUtils.cookie_str2jar(cookieStr)

# 4构造session
session = HTMLSession()
session.headers = headers
session.cookies = cookieJar

# 5获取返回响应对象
r = session.get(url)
# print(r.text)
# 6执行js代码
r.html.render()

# print(r.html)
# with open('1.text') as f:
#     f.write(r.html.text)
# 7提取需要的url路径
elems = r.html.find('dd.detail>a')
urls = []

for e in elems:
    index = 0
    url = 'https:' + e.attrs['href']
    urls.append(url)
    response = session.get(url)
    with open('' + str(index) + '.html', 'w')as f:
        f.write(response.text)
    index += 1
    time.sleep(1)
print(urls)
