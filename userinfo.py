import requests,re,json

#抖音用户信息获取

def get_url(uid):
    #内网服务，地址因而变
    #拼接uid
    signurl = 'http://192.168.123.159:8989/0/0/v2/dy/userinfo/%s'%(uid)
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
    req = requests.get(url=url,headers=headers).content.decode("utf-8")
    myjson = json.loads(req)
    try:
        status_code = myjson.get('status_code')
        if status_code == 0:
            item = {}
            user = myjson.get('user')
            item['nickname'] = user.get('nickname')
            item['gender'] = user.get('gender')   #0未填写 1是男 2是女
            unique_id = user.get('unique_id')
            
            if unique_id:
                item['抖音id'] = unique_id#没有另外设置时为short_id
            else:
                item['抖音id'] = user.get('short_id')
            
            item['地址'] = user.get('location')
            item['签名'] = user.get('signature')
            pic = user.get('avatar_larger')
            item['粉丝数'] = user.get('follower_count')
            item['following_num'] = user.get('following_count')
            item['获赞数'] = user.get('total_favorited')
            item['作品数'] = user.get('aweme_count')
            item['动态数'] = user.get('dongtai_count')
            print(item) 
        else:
            print('请求失败'+req)
    except Exception as e:
            print(e)


if __name__ == "__main__":
    get_result(84990209480)
