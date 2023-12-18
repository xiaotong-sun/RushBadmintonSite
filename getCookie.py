# 没能实现成功
import requests

headers = {
    "Host": "wechat.njust.edu.cn",
    "Proxy-Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/10.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309080f) XWEB/8501 Flue",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "*",
    "Accept-Encoding": "gzip, deflate",
}
session = requests.Session()  # 创建session对象
# 第一次使用session，捕获请求cookie
url = 'http://wechat.njust.edu.cn/gymMicroportal/gymMicroportal.html?i=1'
page_text = session.get(url=url, headers=headers).text
print(page_text)
