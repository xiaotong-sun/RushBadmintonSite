import json
import time
import requests

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
    "Cookie": "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvdCI6IndlY2hhdF9xeSIsInQiOiIxMjMxMDYwMTA3OTciLCJleHAiOjE3MTA4NTgyNzcsIm8iOiIxMjMxMDYwMTA3OTciLCJub3ciOjE3MTA4NTQ2NzcsInR0IjoiZGF0YWJhc2UifQ.whQNLa1pp5hsG72PQBk1w0US2Up5FrhNF0A-_18O_Mc",
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

bookDate = "2024-03-21"
# data = {"siteId": "1ce71c8c2b934461bd33c5bd469fc961", "bookDate": bookDate}  # Baseball
data = {"siteId": "e1f5c85e86c34c46a2d0935452094b77", "bookDate": bookDate}  # Badminton

res = requests.post(url=url, headers=header, json=data)
tm = res.elapsed.total_seconds()  # 获取请求时间
print(tm)
print(res.status_code)
resText = json.loads(res.text)
with open(bookDate + "-badminton.json", "w+") as f:
    json.dump(resText, f, indent=4, ensure_ascii=False)
