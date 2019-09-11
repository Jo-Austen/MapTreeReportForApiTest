import json,requests,time
import loggingExtend as loggrr
import os

data = [
    {"Device":"","Message":None},
    {"Device":"","Message":None},
    {"Device":"","Message":None},
    {"Device":"","Message":"可领取收益"},
    {"Device":"","Message":"体验中"}
]

logr = loggrr.Logger(os.path.split(os.path.realpath(__file__))[0]+"/", str(time.ctime()))
def Entrance():
    Adme_url = ""
    # print("TestSuite01:NoLogin_ad/me Test:")
    for data_node in data:
        Params = {
            "platId":"1",
            "appVersion":"6.0.2",
            "os":"ios",
            "isNew":"0",
            "osVersion":"12.3.1",
            "CheckToken":"",
            "DeviceId":data_node["Device"],
            "appname":"ttjj",
            "MarketChannel":" Appstore"
        }
        adme_Res = json.loads((requests.get(Adme_url,params=Params)).text)
        tradeMessage = adme_Res["datas"]["MeTyjActivity"]["TradeMessage"]
        if data_node["Message"] == tradeMessage:
            print('\033[0;32;40mPass | %s:"%s\"\033[0m'%(data_node["Device"],data_node["Message"]))
            logr.info("TestSuite01:NoLogin_ad","PASSD",str(data_node["Device"]),'Expect:%s == Output:%s'%(data_node["Message"],tradeMessage))
        else:
            print('\033[0;31;40mFalse | %s:"%s\"\033[0m'%(data_node["Device"],tradeMessage))
            logr.error("TestSuite01:NoLogin_ad","ERROR",str(data_node["Device"]),'Expect:%s != Output:%s'%(data_node["Message"],tradeMessage))


Entrance()
