import requests,re,json,time

#抖音用户视频获取

def get_url(uid):
    #内网服务，地址因而变
    signurl = 'http://192.168.123.159:8989/v2/dy/userfeed/%s/max_cursor/0'%(uid)
    res = requests.get(signurl)
    res = res.content.decode("utf-8")
    #print(res)
    return res
    
    
def get_result(uid):
    url = get_url(uid)
    headers = {
        #更改为你的cookie
        'cookie': 'odin_tt=e10f3e84ef6beb0ccf19e99686228048a08c6cc59992711e2a4b68adf2d6324d412912affd02df3976094d6b4db1ee4de3b804b4713efcd74dbc49f51db711e0',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36',
    }
    req = requests.get(url=url,headers=headers,verify=False).content.decode("utf-8")
    myjson = json.loads(req)
    extra = myjson.get('extra')
    if extra:
        video_list = myjson.get('aweme_list')
        num = 0
        for video in video_list:
            try:
                item = {}
                num = num + 1
                print('第%s条：'%str(num)+'视频data')
                item['播放地址'] = video.get('video').get('play_addr_lowbr').get('url_list')[2]#第三个地址
                item['分享地址'] = video.get('share_url')
                item['视频截图'] = video.get('video').get('origin_cover').get('url_list')[0]
                item['时长'] = video.get('duration')
                item['标题'] = video.get('desc')
                timestamp = video.get('create_time')
                #转换成localtime
                time_local = time.localtime(timestamp)
                #转换成新的时间格式(2016-05-05 20:28:54)
                dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
                item['创建时间'] = dt
                statistics = video.get('statistics')
                item['评论数'] = statistics.get('comment_count')
                item['获赞数'] = statistics.get('digg_count')
                
                item['分享数'] = statistics.get('share_count')
                print(item,'\n')
            except Exception as e:
                print("错误",e)
    else:
        print("解析失败",req)
            

if __name__ == "__main__":
    get_result(84990209480)
