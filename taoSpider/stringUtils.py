'''
专门处理字符串相关的工作
'''
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
