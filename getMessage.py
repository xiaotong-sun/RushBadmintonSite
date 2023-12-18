import json
import time
import requests

# TODO 将获取到的信息进行整理，得到每个场地的名字，对应的areaID，areaPriceID，timeID，对应的时间段，周几

header = {
    'Host': 'wechat.njust.edu.cn',
    'Proxy-Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309080f) XWEB/8501 Flue',
    'Content-Type': 'application/json',
    'Origin': 'http://wechat.njust.edu.cn',
    'Referer': 'http://wechat.njust.edu.cn/gymBooking/venueBooking.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': '*',
    # cookie需要改变
    "Cookie": "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvIjoiMTIzMTA2MDEwNzk3Iiwib3QiOiJ3ZWNoYXRfcXkiLCJ0dCI6IndlY2hhdF9xeSIsInQiOiIxMjMxMDYwMTA3OTciLCJub3ciOjE3MDI2NDI5ODksImV4cCI6MTcwMjY0NjU4OX0.L9SqJ56incpU2CpLqUcE6itoy-_gLXhkOhXpYiAHSjE",
}

url = 'http://wechat.njust.edu.cn/api/v2/appGym/listAreaPriceBySiteIdAndTime'

# for i in range(1, 8):
#     bookDate = "2023-12-1" + str(i)
#     data = {"siteId": "1ce71c8c2b934461bd33c5bd469fc961", "bookDate": bookDate}  # Baseball
#     # data = {"siteId": "e1f5c85e86c34c46a2d0935452094b77", "bookDate": bookDate}  # Badminton

#     res = requests.post(url=url, headers=header, json=data)
#     tm = res.elapsed.total_seconds()  # 获取请求时间
#     print(tm)
#     print(res.status_code)
#     resText = json.loads(res.text)
#     with open(bookDate + "-baseball.json", "w+") as f:
#         json.dump(resText, f, indent=4, ensure_ascii=False)

bookDate = "2023-12-18"
data = {"siteId": "1ce71c8c2b934461bd33c5bd469fc961", "bookDate": bookDate}  # Baseball
# data = {"siteId": "e1f5c85e86c34c46a2d0935452094b77", "bookDate": bookDate}  # Badminton

res = requests.post(url=url, headers=header, json=data)
tm = res.elapsed.total_seconds()  # 获取请求时间
print(tm)
print(res.status_code)
resText = json.loads(res.text)
with open(bookDate + "-baseball.json", "w+") as f:
    json.dump(resText, f, indent=4, ensure_ascii=False)
