import json

# for i in range(1, 8):
#     readPath = '2023-12-1' + str(i) + '-badminton.json'
#     # readPath = '2023-12-10' + '-badminton.json'
#     writePath = 'week' + str(i) + '-badminton.json'
#     # writePath = 'week7' + '-badminton.json'
#     with open(readPath, 'r') as f:
#         message = json.load(f)
#         total_Period_Area = []
#         for j in range(0, 14):  # 共14个时间段
#             start_end_Mes = message["data"][j]["startTime"] + "~" + message["data"][j]["endTime"]
#             time_dict = {"Period": start_end_Mes}
#             areaList = []
#             for k in range(0, 17):  # 共17个场地
#                 areaPriceMes = message["data"][j]["listAreaPrice"][k]
#                 areaPriceId = areaPriceMes["areaPriceId"]
#                 areaId = areaPriceMes["areaId"]
#                 areaName = areaPriceMes["areaName"]
#                 timeId = areaPriceMes["timeId"]
#                 price = areaPriceMes["price"]

#                 area_dict = {
#                     "areaId": areaId,
#                     "timeId": timeId,
#                     "areaPriceId": areaPriceId,
#                     "areaName": areaName,
#                     "price": price,
#                 }

#                 areaList.append(area_dict)
#             time_dict["areaList"] = areaList
#             total_Period_Area.append(time_dict)
#         with open(writePath, 'w+') as wf:
#             json.dump(total_Period_Area, wf, indent=4, ensure_ascii=False)

readPath = '2024-03-06' + '-badminton.json'
writePath = 'week3' + '-badminton.json'
with open(readPath, 'r') as f:
    message = json.load(f)
    total_Period_Area = []
    for j in range(0, 14):  # 共14个时间段
        start_end_Mes = message["data"][j]["startTime"] + "~" + message["data"][j]["endTime"]
        time_dict = {"Period": start_end_Mes}
        areaList = []
        for k in range(0, 17):  # 共4个场地
            areaPriceMes = message["data"][j]["listAreaPrice"][k]
            areaPriceId = areaPriceMes["areaPriceId"]
            areaId = areaPriceMes["areaId"]
            areaName = areaPriceMes["areaName"]
            timeId = areaPriceMes["timeId"]
            price = areaPriceMes["price"]

            area_dict = {
                "areaId": areaId,
                "timeId": timeId,
                "areaPriceId": areaPriceId,
                "areaName": areaName,
                "price": price,
            }

            areaList.append(area_dict)
        time_dict["areaList"] = areaList
        total_Period_Area.append(time_dict)
    with open(writePath, 'w+') as wf:
        json.dump(total_Period_Area, wf, indent=4, ensure_ascii=False)
