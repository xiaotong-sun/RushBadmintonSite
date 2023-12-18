import json
import time
import requests

# TODO 添加指定时间开始抢票
# TODO 添加容错机制，如果一个抢票失败，就抢另一个
# TODO 尝试能否自动获取cookie
# TODO 现在有另一个思路，就是不提前写死场地的各种id，而是在抢的时候再获取并填充，但是这可能导致抢票速度变慢。好处就是不用手动写请求体信息，但是，如果这些信息是固定的话，其实写一次就可以了，工作量主要在第一次上。

header = {
    'Host': 'wechat.njust.edu.cn',
    'Proxy-Connection': 'keep-alive',
    'Accept': 'application/json, text/plain, */*',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 NetType/WIFI MicroMessenger/7.0.20.1781(0x6700143B) WindowsWechat(0x6309080f) XWEB/8461 Flue',
    'Content-Type': 'application/json',
    'Origin': 'http://wechat.njust.edu.cn',
    'Referer': 'http://wechat.njust.edu.cn/gymBooking/venueBooking.html',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    # cookie需要改变
    "Cookie": "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvIjoiMTIzMTA2MDEwNzk3Iiwib3QiOiJ3ZWNoYXRfcXkiLCJ0dCI6IndlY2hhdF9xeSIsInQiOiIxMjMxMDYwMTA3OTciLCJub3ciOjE3MDI2Mzg1NzAsImV4cCI6MTcwMjY0MjE3MH0.dOCBQA5REyjRuYYGZjAKzRgnw5nklnUG3a1xGeYfdKw",
}

url = 'http://wechat.njust.edu.cn/api/v2/appGym/submitAreaOrder'

# siteId 对应的应该是乒乓球或者羽毛球场地
# gymId  对应的应该是哪个场馆
# >> areaID 对应的场地中的哪块区域
# >> timeID 对应的是哪个时间段的id，相同运动的同一时间段是相同的，不同运动之间是不相同的。不同天对应的timeId是相同的
# >> areaPriceID 对应的是某天某个场地某个时间段的价格id，每一周之间可复用

bookDate = "2023-12-16"
orderNum = 1
price = 15
payAmount = price * orderNum

data = {
    # "siteId": "4007243990b243938283ce51ea5af072", # 乒乓球
    # "siteId": "e1f5c85e86c34c46a2d0935452094b77",  # 羽毛球
    'siteId': '1ce71c8c2b934461bd33c5bd469fc961',  # 网球-体育园
    # "gymId": "790c8055a06311e8a69022faa7560813", # 体育中心（乒乓球, 羽毛球）
    'gymId': '790c8055a06311e8a69022faa7560814',  # 体育部（网球-体育园）
    "payAmount": payAmount,
    "payDuration": 60,  # 这个的值好像无所谓
    "areaRecordList": [
        {
            # "areaId": "782adf2542cb426b8f31c4b1de3d4ada",  # 乒乓球22号场地
            # "areaId": "b71eb9e460d7480aaf5e0decfc87476b",  # 网球-体育园3号场地
            "areaId": "4650b64907094cb196a5e99f3bd68e84",  # 网球-体育园4号场地
            "bookingDate": bookDate,  # 这个是必须的
            # "timeId": "96c1a3f81fa64837aeb6cfa460f4ab40",  # 网球-体育园3号场地 15:00~16:00
            "timeId": "96c1a3f81fa64837aeb6cfa460f4ab40",  # test
            # "timeId": "25a8e1198b9548149b9d1223f244bd87",  # 网球-体育园3号场地 16:00~17:00
            # "timeId": "98d2ce673d894bb29b1947a6e0a98170",  # 18:00~19:00
            "userType": 1,  # 这个应该不需要改变, 但是必须有
            # "areaPriceId": "6160b00fa0b2491da01b2e1f36ba3875",  # 乒乓球22号场地 18:00~19:00
            # "areaPriceId": "efbad7d50da54b82bf912b5e766e50c3",  # 网球-体育园3号场地 15:00~16:00
            "areaPriceId": "28d507ffdbd449a9860bc842fecc94df",  # test
            # "areaPriceId": "f346affe20b54c22aab5f3843121a89f",  # 网球-体育园3号场地 16:00~17:00
            "price": price,  # 这个是必要的, 乒乓球5元, 周末白天网球15元
        },
        # {
        #     # "areaId": "782adf2542cb426b8f31c4b1de3d4ada",  # 乒乓球22号场地
        #     "areaId": "b71eb9e460d7480aaf5e0decfc87476b",  # 网球-体育园3号场地
        #     "bookingDate": bookDate,  # 这个是必须的
        #     # "timeId": "96c1a3f81fa64837aeb6cfa460f4ab40",  # 15:00~16:00
        #     "timeId": "25a8e1198b9548149b9d1223f244bd87",  # 16:00~17:00
        #     # "timeId": "98d2ce673d894bb29b1947a6e0a98170",  # 18:00~19:00
        #     "userType": 1,  # 这个应该不需要改变
        #     # "areaPriceId": "6160b00fa0b2491da01b2e1f36ba3875",  # 乒乓球22号场地 18:00~19:00
        #     # "areaPriceId": "efbad7d50da54b82bf912b5e766e50c3",  # 网球-体育园3号场地 15:00~16:00
        #     "areaPriceId": "f346affe20b54c22aab5f3843121a89f",  # 网球-体育园3号场地 16:00~17:00
        #     "price": price,  # 这个是必要的, 乒乓球5元, 周末白天网球15元
        # },
    ],
    "bookTimes": 1,
}

res = requests.post(url=url, headers=header, json=data)
tm = res.elapsed.total_seconds()  # 获取请求时间
print(tm)
print(res.status_code)
print(res.text)
