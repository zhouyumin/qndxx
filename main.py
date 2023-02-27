# @Time : 2020/10/27 14:19 
# @Author : zym
# @File : main.py 
# @Software: PyCharm
import requests
import bs4
from wsgiref.simple_server import make_server
import json

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36 Edg/86.0.622.51"}

url = "http://www.cyol.com/"
target = ""
title = ""
end_image = ""


# def get_target():
#     res = requests.get(url, headers=header)
#     res.encoding = res.apparent_encoding
#     soup = bs4.BeautifulSoup(res.text, "html.parser")
#     divs = soup.find("div", class_="slideBox")
#     a = divs.find_all("a")
#     global target
#     for each in a:
#         if each["href"].find("daxuexi") != -1:
#             target = each["href"]
#             break
#
#     print('find url:' + target)
#
#
# def get_title():
#     res = requests.get(target, headers=header)
#     res.encoding = res.apparent_encoding
#     soup = bs4.BeautifulSoup(res.text, "html.parser")
#     global title
#     title = soup.head.title.string
#     print('find title:' + title)
#
#
# def get_end_image():
#     global end_image
#     end_image = target[:-10] + 'images/end.jpg'
#     print('get end_image:' + end_image)


def api_get() -> tuple:
    res = requests.get('https://service-0wsl5m13-1256946954.cd.apigw.tencentcs.com/release/qndxx', headers=header)
    if res.ok:
        data = json.loads(res.text)
        return data['dxx_img'], data['title']
    else:
        return '', ''


def render_page(environ, start_response):
    req = environ.get("PATH_INFO")
    print("request url:"+req)
    if "/favicon.ico" == req:
        start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
        return []
    # get_target()
    # get_title()
    # get_end_image()
    global end_image, title
    end_image, title = api_get()

    file = "./index.html"
    with open(file, encoding="utf-8") as f:
        data = f.read()
    data = data.replace("{title}", title)
    data = data.replace("{url}", end_image)
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    return [bytes(data, encoding="utf-8")]


if __name__ == '__main__':
    http = make_server("", 8080, render_page)
    http.serve_forever()
