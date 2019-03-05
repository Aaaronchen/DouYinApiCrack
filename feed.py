import requests,re,json

#抖音随机视频获取

def get_url():
    #内网服务，地址因而变
    signurl = 'http://192.168.123.159:8989/v2/dy/feed'
    res = requests.get(signurl)
    res = res.content.decode("utf-8")
    #print(res)
    return res
    
    
def get_result():
    url = get_url()
    headers = {
        #更改为你的cookie
        'cookie': 'odin_tt=e10f3e84ef6beb0ccf19e99686228048a08c6cc59992711e2a4b68adf2d6324d412912affd02df3976094d6b4db1ee4de3b804b4713efcd74dbc49f51db711e0',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Mobile Safari/537.36',
    }
    req = requests.get(url=url,headers=headers,verify=False).content.decode("utf-8")
    myjson = json.loads(req)
    aweme_list = myjson.get('aweme_list')
        
    if aweme_list:
        for i in range(len(aweme_list)):
            try:
                video = aweme_list[i]
                videoinfo = {}
                print('第%s条：'%str(i+1)+'这是一条视频data')
                author = video['author']
                statistics = video['statistics']
                
                videoinfo['昵称'] = author.get('nickname')
                videoinfo['抖音id'] = author.get('short_id')
                videoinfo['uid'] = author.get('uid')
                videoinfo['获赞数'] = statistics.get('digg_count')
                videoinfo['评论数'] = statistics.get('comment_count')
                videoinfo['分享数'] = statistics.get('share_count')
                print(videoinfo,'\n')
                
            except Exception as e:
                print('错误原因:',e)


if __name__ == "__main__":
    get_result()
