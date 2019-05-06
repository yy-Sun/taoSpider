str_test = "1er=eafji=fds=".strip()
from taoSpider.utils import stringUtils

index = str_test.index('=')
print(index)

str_test2 = 'ctoken=7gmxxOPhIYdd8Mtl5gWLigiA; cna=IvpVFYuB6msCATpltpRSISG4; t=fd0a1a2dcd9b89d22deed36c62c79dec; _m_h5_tk=d12dd765137d8b06465136643832e483_1557171451033; _m_h5_tk_enc=b7c7e80eb28c9116b4859a6938f5f825; cookie2=12a00ac3f8674a3045f79b6021708d7c; v=0; _tb_token_=ea616e36566ee; unb=1706845563; sg=538; _l_g_=Ug%3D%3D; skt=f19ed21af77b5fbd; cookie1=BxvAfhJKXE88fjwdsTj%2Bid2YbgqwSIiZKlJxbQBiCcU%3D; csg=6d4e2c64; uc3=vt3=F8dByEawOVR7XC%2BQB%2Fw%3D&id2=UoYekxLW0zUv9g%3D%3D&nk2=svsV7fzyZuw%3D&lg2=UIHiLt3xD8xYTw%3D%3D; existShop=MTU1NzE2MzE5OA%3D%3D; tracknick=%5Cu9633835455; lgc=%5Cu9633835455; _cc_=UIHiLt3xSw%3D%3D; dnk=%5Cu9633835455; _nk_=%5Cu9633835455; cookie17=UoYekxLW0zUv9g%3D%3D; tg=0; mt=ci=22_1; thw=cn; uc1=cookie14=UoTZ48QDi0R8CQ%3D%3D&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&existShop=false&cookie21=VT5L2FSpccLuJBreK%2BBd&tag=8&cookie15=W5iHLLyFOGW7aA%3D%3D&pas=0; l=bBSa3tGcvDMzTD_QBOfNNuI-5R7tNIOb4sPzw41agICP_o1959lhWZ9AJJ8pC3GVw18wR3WSJbCuBeYBY5f..; isg=BBISzLbamn0UROYBYHjR5Nl2Y9E0iws8oI75ldxqFkWw77PpxLbnzUyFXwv2n45V'
print(stringUtils.cookie_str2dict(str_test2))
