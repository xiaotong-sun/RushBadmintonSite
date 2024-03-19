import json
import time
import requests
import multiprocessing

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
    "Cookie": "token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvdCI6IndlY2hhdF9xeSIsInQiOiIxMjMxMDYwMTA3OTciLCJleHAiOjE3MTA4NTgyNzcsIm8iOiIxMjMxMDYwMTA3OTciLCJub3ciOjE3MTA4NTQ2NzcsInR0IjoiZGF0YWJhc2UifQ.whQNLa1pp5hsG72PQBk1w0US2Up5FrhNF0A-_18O_Mc",
}

url = 'http://wechat.njust.edu.cn/api/v2/appGym/submitAreaOrder'

# 需要修改的值：opentime，bookDate，price，week，cookie
struct_openTime = "2024-03-10 08:00:02"
bookDate = "2024-03-21"
orderNum = 2
price = 15.0
# price = 0.0
payAmount = price * orderNum

# week1 × period:19:00~21:00 price:15.0
# week2 × period:00:00~00:00 price:15.0
# week3 √ period:15:00~17:00 price:0.0
# week3_× period:19:00~21:00 price:15.0
# week4 √ period:19:00~21:00 price:15.0
# week5 × period:00:00~00:00 price:15.0
week1 = [
    # 6号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "80c197c0c1984d5292db7e74a661e482",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "a505d9ca80d34a45985be5cad1bc1a8c",
                "areaName": "6",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "80c197c0c1984d5292db7e74a661e482",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "c4778c036060426d834a279ae9632bcc",
                "areaName": "6",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 8号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "4e8c8ee1ccee45bbb7ca5774b00a6670",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "5abda24dcf60477cae639140830cf380",
                "areaName": "8",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "4e8c8ee1ccee45bbb7ca5774b00a6670",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "e6b0b6e13b644b34a1518a8ab9e57ef5",
                "areaName": "8",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 9号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "a4296d6cc74a4abaa5663c6090a59dd9",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "ebe1f48a8cde40b29e138823ac82b8c3",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 12号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "6d7c5e380fcb4f1b881104d7f19f79e0",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "bf96e1188b604240956429821645c776",
                "areaName": "12",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "6d7c5e380fcb4f1b881104d7f19f79e0",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "28c2aaf326e74e87bc2df2a1d4d1a831",
                "areaName": "12",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 16号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "44bf52facd134cf6a4c3a581c2d7700a",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "4e88945960f944c1af3b0bf4397e8fdb",
                "areaName": "16",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "44bf52facd134cf6a4c3a581c2d7700a",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "4b240d03894747818262a1c3d549c691",
                "areaName": "16",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
]

week2 = [
    # 6号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "80c197c0c1984d5292db7e74a661e482",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "a505d9ca80d34a45985be5cad1bc1a8c",
                "areaName": "6",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "80c197c0c1984d5292db7e74a661e482",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "c4778c036060426d834a279ae9632bcc",
                "areaName": "6",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 8号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "4e8c8ee1ccee45bbb7ca5774b00a6670",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "5abda24dcf60477cae639140830cf380",
                "areaName": "8",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "4e8c8ee1ccee45bbb7ca5774b00a6670",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "e6b0b6e13b644b34a1518a8ab9e57ef5",
                "areaName": "8",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 9号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "a4296d6cc74a4abaa5663c6090a59dd9",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "ebe1f48a8cde40b29e138823ac82b8c3",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 12号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "6d7c5e380fcb4f1b881104d7f19f79e0",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "bf96e1188b604240956429821645c776",
                "areaName": "12",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "6d7c5e380fcb4f1b881104d7f19f79e0",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "28c2aaf326e74e87bc2df2a1d4d1a831",
                "areaName": "12",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 16号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "44bf52facd134cf6a4c3a581c2d7700a",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "4e88945960f944c1af3b0bf4397e8fdb",
                "areaName": "16",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "44bf52facd134cf6a4c3a581c2d7700a",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "4b240d03894747818262a1c3d549c691",
                "areaName": "16",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
]

week3 = [
    # 1号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 15:00 ~ 16:00
            {
                "areaId": "768abcc7c3804ac4b1ce31abf788fd00",
                "timeId": "4dbc92be62e347ec8cfd55053910fb8a",
                "areaPriceId": "5d9eb66fa1d644969b5d3efbb761c480",
                "areaName": "1",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 16:00 ~ 17:00
            {
                "areaId": "768abcc7c3804ac4b1ce31abf788fd00",
                "timeId": "5ea4167c0e2a46808c6480909fe758c4",
                "areaPriceId": "1f70e3f2693a40048356ba527972693c",
                "areaName": "1",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 3号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 15:00 ~ 16:00
            {
                "areaId": "491dba0be92c4f4faef27283e9fc891f",
                "timeId": "4dbc92be62e347ec8cfd55053910fb8a",
                "areaPriceId": "b52a46cf585041e78ef68ea1238d2923",
                "areaName": "3",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 16:00 ~ 17:00
            {
                "areaId": "491dba0be92c4f4faef27283e9fc891f",
                "timeId": "5ea4167c0e2a46808c6480909fe758c4",
                "areaPriceId": "a64699f4d3164050a852941956216fa5",
                "areaName": "3",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 5号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 15:00 ~ 16:00
            {
                "areaId": "f8fc3d1d76b8463d9f65a38e5247eeeb",
                "timeId": "4dbc92be62e347ec8cfd55053910fb8a",
                "areaPriceId": "69ffdff91e074567a7b1862da6f5ed9e",
                "areaName": "5",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 16:00 ~ 17:00
            {
                "areaId": "f8fc3d1d76b8463d9f65a38e5247eeeb",
                "timeId": "5ea4167c0e2a46808c6480909fe758c4",
                "areaPriceId": "d9ee73ba9c01410a9d5475c4ee879a33",
                "areaName": "5",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 9号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 15:00 ~ 16:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "4dbc92be62e347ec8cfd55053910fb8a",
                "areaPriceId": "89a0211bf4d64b719465ee37a00a3da6",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 16:00 ~ 17:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "5ea4167c0e2a46808c6480909fe758c4",
                "areaPriceId": "1b659917bb0e4cd7a8db40dea4f55d0e",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 13号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 15:00 ~ 16:00
            {
                "areaId": "71c623b466e0478abc0b575169f931eb",
                "timeId": "4dbc92be62e347ec8cfd55053910fb8a",
                "areaPriceId": "0df6f995d09547db9e03df12a6a0673e",
                "areaName": "13",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 16:00 ~ 17:00
            {
                "areaId": "71c623b466e0478abc0b575169f931eb",
                "timeId": "5ea4167c0e2a46808c6480909fe758c4",
                "areaPriceId": "138ab8484a7c41d1b62c2166ca1177fb",
                "areaName": "13",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
]

week3_ = [
    # 1号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "768abcc7c3804ac4b1ce31abf788fd00",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "41b22251d4de4b97915962b47aa0df35",
                "areaName": "1",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "768abcc7c3804ac4b1ce31abf788fd00",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "0ecaaa425a4b400985d15e2b030cf7a8",
                "areaName": "1",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 3号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "491dba0be92c4f4faef27283e9fc891f",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "d103742940d2433096abfe3040be21d4",
                "areaName": "3",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "491dba0be92c4f4faef27283e9fc891f",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "1f56fb1908b64ab591969e5e19d384f4",
                "areaName": "3",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 5号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "f8fc3d1d76b8463d9f65a38e5247eeeb",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "0ba4cbc187964babbded5be1a0ce849e",
                "areaName": "5",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "f8fc3d1d76b8463d9f65a38e5247eeeb",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "aae39fcab3e947479b1a09fa1f9eae51",
                "areaName": "5",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 9号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "523fa68ce409405f8a76d146eb5021ba",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "f8bb40c373184fcfa993dac36c9f9c73",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 13号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "71c623b466e0478abc0b575169f931eb",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "f81313a39b6a4aeabd075d9ddab83e22",
                "areaName": "13",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "71c623b466e0478abc0b575169f931eb",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "3d5923095e52424b8b3f5382689dc84b",
                "areaName": "13",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
]

week4 = [
    # 6号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "80c197c0c1984d5292db7e74a661e482",
                "timeId": "1a09c9bc14004ebd86e63dbf89853dd6",
                "areaPriceId": "e9dc171e1f434a7fb196f8267ea870e6",
                "areaName": "6",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "80c197c0c1984d5292db7e74a661e482",
                "timeId": "561199842d5d453d91bf05947f42f436",
                "areaPriceId": "532e6c8c08824565ab296f948a51c73b",
                "areaName": "6",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 8号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "4e8c8ee1ccee45bbb7ca5774b00a6670",
                "timeId": "1a09c9bc14004ebd86e63dbf89853dd6",
                "areaPriceId": "b56fe15233074504acf8184d35757660",
                "areaName": "8",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "4e8c8ee1ccee45bbb7ca5774b00a6670",
                "timeId": "561199842d5d453d91bf05947f42f436",
                "areaPriceId": "f744fcb207d6471aae04c4f646acdbd2",
                "areaName": "8",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 9号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "1a09c9bc14004ebd86e63dbf89853dd6",
                "areaPriceId": "b21844d661044c669a2f79bce5020b59",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "561199842d5d453d91bf05947f42f436",
                "areaPriceId": "dc6c5d4f46cd4fec9e813e4ddfea1fc1",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 12号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "6d7c5e380fcb4f1b881104d7f19f79e0",
                "timeId": "1a09c9bc14004ebd86e63dbf89853dd6",
                "areaPriceId": "91d663da26a247feab9971c477a85aa9",
                "areaName": "12",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "6d7c5e380fcb4f1b881104d7f19f79e0",
                "timeId": "561199842d5d453d91bf05947f42f436",
                "areaPriceId": "9f4f60bf6a8b471a80974a0e78f0a0a7",
                "areaName": "12",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 16号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "44bf52facd134cf6a4c3a581c2d7700a",
                "timeId": "1a09c9bc14004ebd86e63dbf89853dd6",
                "areaPriceId": "c80a186a94354a01834d8d7c67468c44",
                "areaName": "16",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "44bf52facd134cf6a4c3a581c2d7700a",
                "timeId": "561199842d5d453d91bf05947f42f436",
                "areaPriceId": "0d67832d510e4c019ec454b3c4325cf2",
                "areaName": "16",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
]

week5 = [
    # 6号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "80c197c0c1984d5292db7e74a661e482",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "a505d9ca80d34a45985be5cad1bc1a8c",
                "areaName": "6",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "80c197c0c1984d5292db7e74a661e482",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "c4778c036060426d834a279ae9632bcc",
                "areaName": "6",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 8号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "4e8c8ee1ccee45bbb7ca5774b00a6670",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "5abda24dcf60477cae639140830cf380",
                "areaName": "8",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "4e8c8ee1ccee45bbb7ca5774b00a6670",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "e6b0b6e13b644b34a1518a8ab9e57ef5",
                "areaName": "8",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 9号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "a4296d6cc74a4abaa5663c6090a59dd9",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "496c885b499c47d0a51885c2e68f5021",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "ebe1f48a8cde40b29e138823ac82b8c3",
                "areaName": "9",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 12号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "6d7c5e380fcb4f1b881104d7f19f79e0",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "bf96e1188b604240956429821645c776",
                "areaName": "12",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "6d7c5e380fcb4f1b881104d7f19f79e0",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "28c2aaf326e74e87bc2df2a1d4d1a831",
                "areaName": "12",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
    # 16号场地
    {
        "siteId": "e1f5c85e86c34c46a2d0935452094b77",
        "gymId": "790c8055a06311e8a69022faa7560813",
        "payAmount": payAmount,
        "areaRecordList": [
            # 19:00 ~ 20:00
            {
                "areaId": "44bf52facd134cf6a4c3a581c2d7700a",
                "timeId": "219fb8221393417e9e03c50a4e924a39",
                "areaPriceId": "4e88945960f944c1af3b0bf4397e8fdb",
                "areaName": "16",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
            # 20:00 ~ 21:00
            {
                "areaId": "44bf52facd134cf6a4c3a581c2d7700a",
                "timeId": "554c0fd44f734f58ba09e52186dc8bea",
                "areaPriceId": "4b240d03894747818262a1c3d549c691",
                "areaName": "16",
                "price": price,
                "bookingDate": bookDate,
                "userType": 1,
            },
        ],
    },
]

openTime = time.strptime(struct_openTime, "%Y-%m-%d %H:%M:%S")
openTime = time.mktime(openTime)


def submitOrder(orderMes):
    request_cnt = 0
    while True:
        request_cnt += 1
        res = requests.post(url=url, headers=header, json=orderMes)
        tm = res.elapsed.total_seconds()  # 获取请求时间
        message = json.loads(res.text)
        # print(str(res.status_code) + "\t" + str(tm) + "\t" + message["message"])
        print(str(res.status_code) + "\t" + str(message["status"]) + "\t" + str(tm))
        if message["message"] == "success":
            print("预定成功！！")
            return True
        elif request_cnt >= 5:
            return False
        else:
            time.sleep(2)


if __name__ == '__main__':
    flag = False
    pool = multiprocessing.Pool(processes=7)
    while True:
        print(openTime - time.time())
        if time.time() >= openTime:
            print("------------开始抢票-------------")
            process_list = []
            for i in range(5):
                process_list.append(pool.apply_async(submitOrder, (week4[i],)))
            pool.close()
            pool.join()

            for res in process_list:
                print(res.get())
                flag = res.get() or flag

            break

    if not flag:
        print("抢票失败！！")
    print("------------抢票结束-------------")
