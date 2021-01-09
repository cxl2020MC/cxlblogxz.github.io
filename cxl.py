import requests,time
def getToday(cityName):
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + cityName
    response = requests.get(url)
    weatherDict = response.json()
    print(weatherDict)
    if weatherDict['desc'] == 'OK':
        print('你输入的城市是正确的')
        # 获取城市名
        global city, wendu,month,forecast
        city = weatherDict['data']['city']
        print('城市名称', city)
        # 获取当前温度
        wendu = weatherDict['data']['wendu'] + '℃ '
        # 获取月份
        month = time.strftime('%m')
        print(month)
        forecast = weatherDict['data']['forecast']
        # 获取日期
        global date, type, high, low, data
        date = month + '月' + forecast[0]['date']
        # 获取天气类型
        type = forecast[0]['type']
        # 获取最高温度
        high = forecast[0]['high']
        # 获取最低温度
        low = forecast[0]['low']
        ganmao=weatherDict['data']['ganmao']
        
        url = 'https://api.uixsj.cn/hitokoto/get?type=hitokoto&code=json'
        response = requests.get(url)
        weatherDict = response.json()
        print(weatherDict)
        content=weatherDict["type"]+"："+weatherDict['content']
        
        data={'msg':date+"\n"+city+"当前温度为："+wendu+"\n"+"当前天气:"+type+"\n"+"最"+high+"\n"+"最"+low+"\n"+ganmao+"\n"+content,
              'qq':'1176503930'}
    else:
        print('你输入的城市是错误的')
getToday("龙岗区")

url='https://qmsg.zendee.cn/send/bbf96ebf0f97910aebf213da6e5da097'
r=requests.post(url,data=data)
print(r.text)
