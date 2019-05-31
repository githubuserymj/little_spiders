import urllib.request

from future.moves.tkinter import scrolledtext
from lxml import etree
from requests.packages.urllib3.exceptions import *
import urllib.parse
import time
import random
import requests
import json
import urllib
from tkinter import *
from tkinter import ttk
import tkinter
import re
import webbrowser
import threading

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
stop_thread_event = False#进程停止标志，初始为false


# ------------------------------------------功能函数-----------------------------------------#
def tianhui_search():
    key = key_entry.get()
    t = threading.Thread(target=tianhui_faka, args=(key,))
    t.setDaemon(True)
    t.start()

def personfaka_search():
    key = key_entry.get()
    t = threading.Thread(target=person_faka, args=(key,))
    t.setDaemon(True)
    t.start()

def faka920_search():
    key = key_entry.get()
    t = threading.Thread(target=faka920, args=(key,))
    t.setDaemon(True)
    t.start()

def faka_search():
    key = key_entry.get()
    t = threading.Thread(target=faka,args=(key,))
    t.setDaemon(True)
    t.start()

def yiyou_search():
    key = key_entry.get()
    t = threading.Thread(target=yiyou_faka, args=(key,))
    t.setDaemon(True)
    t.start()

def faka331_search():
    key = key_entry.get()
    t = threading.Thread(target=faka331, args=(key,))
    t.setDaemon(True)
    t.start()

def faka510_search():
    key = key_entry.get()
    t = threading.Thread(target=faka510, args=(key,))
    t.setDaemon(True)
    t.start()

def show_secret(event):
    secret_text.delete(1.0,END)
    for item in tree.selection():
        item_text = tree.item(item, "values")
        secret_text.insert(INSERT, '\n[订单编号]\n' + item_text[1] + '\n\n[订单日期]\n' + item_text[2] + '\n\n[订单信息]\n' + item_text[3] + '\n\n[金额]\n' + item_text[4] + '\n\n[卡密]\n' + item_text[5] + '\n\n[订单链接]\n' + item_text[6])

def search():
    row = tree.get_children()
    for item in row:
        tree.delete(item)

    progress_bar.create_rectangle(0, 0, 640, 11, width = 0, fill='white')
    frame3.update()

    faka = faka_lists.get()
    if faka == '天辉发卡':
        tianhui_search()
    elif faka == '个人发卡':
        personfaka_search()
    elif faka == '920发卡':
        faka920_search()
    elif faka == '发卡网':
        faka_search()
    elif faka == '易友发卡':
        yiyou_search()
    elif faka == '331发卡':
        faka331_search()
    elif faka == '510发卡':
        faka510_search()

# def auto_search():
#     keys = ['123456', '1234567', '12345678', '123456789', '1234567890', '666666', '123123', '456456', '789789','456789', 'abc123']
#     funclist = [tianhui_faka,person_faka,faka920,faka,yiyou_faka,faka331,faka510]
#     while stop_thread_event != True:
#         # stop_thread_event = False
#         fun = random.choice(funclist)
#         key = random.choice(keys)
#         th= threading.Thread(target=fun,args=(key,))
#         th.setDaemon(True)
#         th.start()
#         th.join()
#         time.sleep(5)
def random_key():
    keys = ['123456', '1234567', '12345678', '123456789', '1234567890', '666666', '123123', '456456', '789789','456789', 'abc123']
    key_entry.delete(0,END)
    key_entry.insert(INSERT,random.choice(keys))


def stop():
    global stop_thread_event
    stop_thread_event = True#将结束标记设置为True，表示停止位生效

def progress(length,line):#进度条
    len = 640/length #步长
    progress_bar.create_rectangle(0, 0, len * line, 11, width=0, fill='#828790') #单位填充矩形
    frame3.update()

def search_use(infor,secret):#搜索大概的用途
    if secret.find('未付款') != -1:
        return '订单未付款'
    elif infor.find('芒果') != -1:
        return '[芒果视频会员账号]'
    elif infor.find('mgtv') != -1:
        return '[芒果视频会员兑换码]'
    elif infor.find('腾讯') != -1:
        return '[腾讯视频会员账号]'
    elif infor.find('优酷') != -1:
        return '[优酷视频会员账号]'
    elif infor.find('Apex') != -1 or secret.find('Apex') != -1:
        return '[Apex账号]'
    elif infor.find('未付款') != -1:
        return '[订单未付款]'
    else:
        return '[未知卡密]'

def open_url(event):
    for item in tree.selection():
        # item = I001
        item_text = tree.item(item, "values")
        column = tree.identify_column(event.x)  # 列
        row = tree.identify_row(event.y)  # 行
        print(row + ',' + column)
        if column == '#7':
            print(item_text[6])
            webbrowser.open(item_text[6])

def tianhui_faka(key):
    global stop_thread_event
    stop_thread_event = False
    url = 'https://www.vipkm.com/orderquery?orderid=%s&querytype=3'%key
    header = {
        'Host': 'www.vipkm.com',
        'Connection': 'keep - alive',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3497.81Safari / 537.36',
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Accept - Encoding': 'gzip, deflate, br',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Cookie': '__root_domain_v=.vipkm.com; _qddaz=QD.8f132i.f9q2b2.jrah6dbf; __jsluid=8a2f73a46132baab5437931b48b5602e; se329e120=16jsoi6rni4qphd3l2kqfhdr92; Hm_lvt_2f94f14746fb489fdd7f110a124c14d1=1554365442,1554446314,1554447164,1554551758; _qddamta_2852158534=3-0; _qdda=3-1.1; _qddab=3-dkgl2z.ju5h42zf; Hm_lpvt_2f94f14746fb489fdd7f110a124c14d1=1554554535'
    }
    print(url)
    try:
        rep = urllib.request.Request(url,headers=header)
        res = urllib.request.urlopen(rep)
    except urllib.error.URLError as e:
        secret_text.delete(1.0,END)
        secret_text.insert(INSERT,"网页打开失败，请检查网络连接！")
    html = res.read().decode('utf-8')
    html = etree.HTML(html)
    orderlist = html.xpath('//h4/a/text()')
    informationlist = html.xpath('//div[@class="srchtxt srchtxt-particulars"]/div[@class="wrapper"]/p[1]/text()')
    moneylist = html.xpath('//div[@class="srchtxt srchtxt-particulars"]/div[@class="wrapper"]/p[2]/text()')
    hreflists = html.xpath('//h4/a/@href')

    for i in range(0,len(hreflists)):
        hreflists[i] = 'https://www.vipkm.com' + hreflists[i]
    line = 0
    for order, infor,money, href in zip(orderlist, informationlist,moneylist,hreflists):
        if stop_thread_event == True:
            print('线程已停止......')
            break
        else:
            try:
                rep = urllib.request.Request(href,headers=header)
                response = urllib.request.urlopen(rep)

            except urllib.error.URLError as e:
                secret_text.insert(INSERT, "网页打开失败，请检查网络连接！")

            html = response.read().decode('utf-8')
            orderid = href.split("/")[-3]
            # print(html)
            # print(goodurl)
            try:
                token = re.search(r"token: \"(.*)\",",html).group(1)
                print(token)
            except:
                print("cookie已过期！")
                secret_text.insert(INSERT, 'cookie已过期！')
            # print(token)
            secret_url = "https://www.vipkm.com/checkgoods?token=%s&orderid="%token + orderid
            # print(secret_url)
            try:
                rep = urllib.request.Request(secret_url, headers=header)
                secret_response = urllib.request.urlopen(rep)
            except urllib.error.URLError as e:
                secret_text.insert(INSERT, "网页打开失败，请检查网络连接！")

            secret_html = secret_response.read().decode('utf-8')
            target = json.loads(secret_html)
            secret_html = str(target["msg"])
            secret_html = etree.HTML(secret_html)
            secret = ''
            for part_of_secret in secret_html.xpath('//p/text()'):
                secret = secret + part_of_secret + '\n'

            html = etree.HTML(html)
            date = html.xpath('//h4/text()')
            date = date[0].split("：")[-1]
            print(order + ' \t' + date + ' \t' + infor + ' \t' + href)
            line = line + 1
            tree.insert("", "end", values=(line, order.split("：")[-1], date, infor.split("：")[-1], '¥'+money.split("：")[-1],secret.replace("卡密：",""), href))  # 插入数据，
            tree.update()
            progress(len(orderlist),line)

def person_faka(key):
    global stop_thread_event
    stop_thread_event = False
    url = 'http://www.zzh134.cn/search.html?ddid=%s'%key
    headers = {
        'Hos': 'www.zzh134.cn',
        'Connection': 'keep - alive',
        'Cache - Control': 'max - age = 0',
        'Upgrade - Insecure - Requests': '1',
        'User - Agent': 'Mozilla / 5.0(WindowsNT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3497.81Safari / 537.36',
        'Accept': 'text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'Referer': 'http: // www.zzh134.cn / search.html?ddid = 123456 & page = 13',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.9'

    }
    try:
        res = requests.get(url, headers=headers)
        print(res.status_code)
        html = res.text
    except:
        print("出错了")
    html = etree.HTML(html)
    data = html.xpath('//p/text()')
    data = data[0]
    print(data)
    numlist = re.findall(r'([0-9])', data)
    print(numlist)
    order_num = ''
    for num in numlist:
        order_num = order_num + num
    page_num = round(int(order_num) / 5)
    print(page_num)
    page = 0
    line = 0
    while page != page_num:
        page = page + 1
        url = 'http://www.zzh134.cn/search.html?ddid=123456&page=%s' % str(page)
        try:
            res = requests.get(url, headers=headers)
            print(res.status_code)
            html = res.text
        except:
            print("出错了")
        html = etree.HTML(html)
        orderlist = html.xpath('//h3/text()')
        datelist = html.xpath('//ul[@class="am-list am-list-static"]/li[2]/text()')
        informationlist = html.xpath('//ul[@class="am-list am-list-static"]/li[1]/text()')
        moneylist = html.xpath('//ul[@class="am-list am-list-static"]/li[3]/text()')

        for order, date, infor, money in zip(orderlist, datelist, informationlist, moneylist):
            if stop_thread_event == True:
                print('线程已停止......')
                break
            else:
                order = order.split('：')[-1]
                secret_url = 'http://www.zzh134.cn/index/orderInfo.html?ddid=%s' % order
                try:
                    res = requests.get(secret_url, headers=headers)
                    secret_html = res.text
                    line = line + 1
                except:
                    print("出错了")
                secret_html = etree.HTML(secret_html)
                secretlist = secret_html.xpath('//div[@id="target"]/text()')
                secret = str(secretlist)
                secret = secret.replace('\n', '').replace(' ', '').replace('\\n', '').replace('[', '').replace(']','').replace('\'', '').replace(',', '\n')
                print('订单号：' + order + ' 订单时间：' + date + ' 订单信息：'  + infor +  '\n卡密：\n' + secret + '\n')
                tree.insert("", "end", values=(line, order, date.split('：')[-1], infor, '¥'+money.split('：')[-1], secret, secret_url))  # 插入数据，
                tree.update()
                progress(int(order_num)-1, line)

def faka920(key):
    global stop_thread_event
    stop_thread_event = False
    url = 'https://www.920ka.com/Order/Query?type=3&queryvalue='+key
    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        # 'cookie': 'ASP.NET_SessionId=qjucyg5zycxykqej0noxiqfd',#此发卡网必须使用session来保持会话，用第一次获取到的cookie来获取卡密，不然获取卡密就会判断为非法获取
        'referer': 'https://www.920ka.com/order/query?type=3&queryvalue=%s'%key,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    session = requests.session()
    res = session.post(url,timeout = 5,headers = headers,verify = False)
    print(res.cookies)
    html = res.text
    html = etree.HTML(html)
    secret_urllists = []
    orderlist = html.xpath('//tr/td[@class="text-center"][1]/text()')
    datelist = html.xpath('//tr/td[@class="text-center"][2]/text()')
    moneylist = html.xpath('//tr/td[@class="text-center"]/span[@class="text-red"]/text()')
    for order in orderlist:
        secret_url = 'https://www.920ka.com/Ajax/GetCardList/' + order
        secret_urllists.append(secret_url)
    line = 0
    for order,secret_url, date, money in zip(orderlist,secret_urllists, datelist, moneylist):
        if stop_thread_event == True:
            print('线程已停止......')
            break
        else:
            try:
                secret_html = session.get(secret_url, headers=headers,timeout = 5)
                secret_html = secret_html.text
            except urllib.error.URLError as e:
                continue
            print(secret_url)
            target = json.loads(secret_html)
            str = target['msg']
            str = str.replace(' <br>', '\n')
            secret = str.split('|+|')[0]
            print(secret)
            print(date + ' ¥' + money)
            if secret.find('未发卡') != -1 or secret.find('已发卡') != -1:
                continue
            else:
                line = line + 1
                tree.insert("", "end", values=(line, order, date, '此发卡网无商品信息','¥'+money, secret, secret_url))  # 插入数据，
                tree.update()
                progress(len(orderlist), line)

def faka(key):
    global stop_thread_event
    stop_thread_event = False
    url = 'http://www.faka.com/order/query?type=3&queryvalue=%s'%key
    headers = {
        'Referer': 'https://ldfaka.com/chaxuns?querytype=3',
        'Connection': 'keep-alive',
        'Host': 'www.faka.com',
        'cookie': 'ASP.NET_SessionId=o4xmy5xd51rpsavanq3b2did',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',

    }
    res = requests.get(url,headers = headers,verify = False)
    html = res.text
    html = etree.HTML(html)
    orderlist = html.xpath('//td[@class="text-center"][1]/text()')
    orderstatuslist = html.xpath('//td[@class="text-center"][5]/span/text()')
    moneylist = html.xpath('//td[@class="text-center"][4]/span/text()')
    datelist = html.xpath('//td[@class="text-center"][2]/text()')

    line = 0
    for order, date, status, money in zip(orderlist,datelist,orderstatuslist,moneylist):
        if stop_thread_event == True:
            print('线程已停止......')
            break
        else:
            print(stop_thread_event)
            secret_url = 'http://www.faka.com/Ajax/GetCardList/%s'%order
            res = requests.get(secret_url, headers=headers)
            html = res.text
            target = json.loads(html)
            secret = target['msg']
            status = str(status).replace(' ', '').replace('\n', '')
            print(secret_url + '\n' + order + '\n' + date + '\n' + secret + '\n' +  money + ' ' + status + '\n')
            if secret.find('未发卡') != -1:
                continue
            line = line + 1
            tree.insert("", "end", values=(line, order, date, '[此发卡网无商品信息]' + status,'¥' + money, secret, secret_url))  # 插入数据
            tree.update()
            progress(len(orderlist), line)

def yiyou_faka(key):
    global stop_thread_event
    stop_thread_event = False
    url = 'http://www.eayous.cn/orderquery.htm?st=orderid&kw=%s'%key

    headers = {
        'Host': 'www.eayous.cn',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'ZDEDebuggerPresent=php,phtml,php3; PHPSESSID=et3rl0pklm4u7bs0oqt72pvm70'

    }
    try:
        res = requests.get(url, headers=headers)
        html = res.text
        html = etree.HTML(html)
    except:
        print('网页打开失败，请检查网络连接！')
        secret_text.insert(INSERT, "网页打开失败，请检查网络连接！")
    orderlist = html.xpath('//div[@class="main_box"]/p[5]/text()')
    informationlist = html.xpath('//div[@class="main_box"]/div[2]/text()')
    moneylist = html.xpath('//div[@class="main_box"]/p[3]/b/text()')
    datelist = html.xpath('//div[@class="main_box"]/h3/text()')

    line = 0
    for order, date, infor, money in zip(orderlist, datelist, informationlist, moneylist):
        if stop_thread_event == True:
            print('线程已停止......')
            break
        else:
            order = order.split(':')[-1]
            secret_url = 'http://www.eayous.cn/checkgoods.htm?orderid=%s' % order
            res = requests.get(secret_url, headers=headers)
            html = res.text
            if html.startswith(u'\ufeff'):
                html = html.encode('utf8')[3:].decode('utf8')
            target = json.loads(html)
            secret = target['msg'].replace('<br />', '\n')
            print('订单编号：' + order + ' ' + date + ' ' + infor + ' ' + secret + ' 金额：' + money)
            date = date.split('：')[-1]
            infor = infor.replace('使用说明:','')
            if secret.find('未付款') != -1:
                continue
            use = search_use(infor,secret)
            infor = use + infor
            line = line + 1
            tree.insert("", "end", values=(line, order, date, infor, '¥' + money, secret, secret_url))  # 插入数据
            tree.update()
            progress(len(orderlist), line)

def faka331(key):
    global stop_thread_event
    stop_thread_event = False
    url = 'https://www.331ka.com/order.html'  # 获取订单信息的api
    secret_url = 'https://www.331ka.com/order/query_get_cards.html'  # 获取卡密的api
    headers = {
        'Host': 'www.331ka.com',
        'Referer': 'https://www.331ka.com/order.html',
        'Content-Length': '25',
        'Connection': 'Keep-Alive',
        'Cache-Control': 'no-cache',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN',
        'Cookie': 'PHPSESSID=hmv8qiutrjsliivn30vc3hpkhg'

    }

    order_data = {
        'kw': key,
        't': '1554684582513'
    }

    res = requests.post(url, headers=headers, data=order_data, verify=False)
    html = res.text
    target = json.loads(html)
    print(res.status_code)
    line = 0
    for data in target['data']:
        if stop_thread_event == True:
            print('线程已停止......')
            break
        else:
            orderid = data['orderid']
            money = data['money']
            time = data['time']
            secret_html_url = 'https://www.331ka.com/order/orderquery.html?orderid=%s' % orderid
            secret_html = requests.get(secret_html_url, verify=False).text
            sigh = re.search(r'sign=(.*)" class', secret_html).group(1)
            print('订单编号：' + orderid + ' 订单金额：' + money + ' 订单时间：' + time + ' sign：' + sigh)

            secret_headers = {
                'origin': 'https://www.331ka.com',
                'referer': 'https://www.331ka.com/order/orderquery.html?orderid=' + orderid,
                'Connection': 'Keep-Alive',
                'Cache-Control': 'no-cache',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'X-Requested-With': 'XMLHttpRequest',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN',
                'Cookie': 'PHPSESSID=fvlljcom4r8mlknbrdkg2tgp4c'
            }
            secret_data = {
                'orderid': orderid,
                'sign': sigh,
            }
            message_url = 'https://www.331ka.com/order/orderquery.html?orderid=' + orderid
            requests.get(message_url, headers=secret_headers, verify=False)
            print(message_url + '打开完成')

            secret_json_html = requests.post(secret_url, headers=secret_headers, data=secret_data, verify=False)
            secret_json_html = secret_json_html.text
            secret_json_data = json.loads(secret_json_html)
            if secret_json_data['msg'] == 'ok':
                secret = '卡密：' + secret_json_data['data']['cards'][0]['card_num'] + ' 卡密：' +secret_json_data['data']['cards'][0]['card_pwd']
                print(secret)
                html = etree.HTML(secret_json_data['data']['comment'])
                try:
                    messagelist = html.xpath('//p/text()')
                    message = ''
                    for data in messagelist:
                        message = message + data + '\n'
                    print(message)
                    line = line + 1
                    tree.insert("", "end",values=(line, orderid, time, message, '¥' + money, secret, message_url))  # 插入数据
                except:
                    print('此订单无使用说明')
                    line = line + 1
                    tree.insert("", "end",values=(line, orderid, time, '此订单无使用说明', '¥' + money, secret, message_url))  # 插入数据
                tree.update()
                progress(len(target['data'])-1, line)
                print('\n')
            else:
                print(secret_json_data['msg'])

def faka510(key):
    global stop_thread_event
    stop_thread_event = False
    url = 'https://www.510ka.com/QueryOrder?orderid=%s&querytype=3'%key
    headers = {
        'Host': 'www.510ka.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Referer': 'https://www.510ka.com/',
        'Cookie': '__jsluid=2fd85a899735efb7b113039b18f4dd54; s3ad0bd92=ma8rol56hjkdb86snkp9p0jv15; Hm_lvt_9b222a50f9f6966d1e46fea89f626192=1554728097,1554782347,1555599137; Hm_lpvt_9b222a50f9f6966d1e46fea89f626192=1555599152'

    }
    session = requests.session()
    res = session.get(url, headers=headers, verify=False)
    print('状态码：' + str(res.status_code))
    html = res.text
    try:
        token = re.search(r"token: \"(.*)\"", html).group(1)
    except:
        print("cookie已过期！")
        secret_text.delete(1.0,END)
        secret_text.insert(INSERT, 'cookie已过期！')
    print('token：' + token)
    # print(html)
    html = etree.HTML(html)
    orderlist = html.xpath('//div[@class="center"]//span/text()')
    print(orderlist)
    datelist = html.xpath('//div[@class="center"]/h3/text()')
    print(datelist)
    moneylist = html.xpath('//div[@class="right"]/text()')
    for i in range(len(moneylist)):
        moneylist[i] = moneylist[i].replace('\n', '').replace(' ', '')
    print(moneylist)
    line = 0
    for order, date, money in zip(orderlist, datelist, moneylist):
        if stop_thread_event == True:
            print('线程已停止......')
            break
        else:
            secret_html_url = 'https://www.510ka.com/orderquery/orderid/' + order
            secret_url = 'https://www.510ka.com/checkgoods?orderid=%s&token=' % order + token
            line = line + 1
            try:
                print('打开' + secret_html_url)
                secret_html = session.get(secret_url, headers=headers, verify=False).text
                infor = re.search(r'<p>(使用说明.*)<', secret_html).group(1)
                secret = re.search(r'<p>(.*)<p>使用说明', secret_html).group(1).replace('<p>', '').replace('<\/p>', '\n')
                print('订单编号：' + order + ' 订单日期：' + date + ' 订单信息：' + infor + '\n卡密\n' + secret)
                tree.insert("", "end",values=(line, order, date, infor, '¥' + money.split("：")[-1], secret, secret_html_url))  # 插入数据
                tree.update()
                progress(len(orderlist), line)
            except:
                tree.insert("", "end", values=(line, order, '', '所有订单均不能获取卡密则为cookie过期', '', '', secret_html_url))
                print(order + '获取卡密信息出错！[所有订单均不能获取卡密则为cookie过期]\n')
                continue
            print('\n')
            time.sleep(0.1)
#------------------------------------------------------------------------------------------#


# ------------------------------------------UI布局-----------------------------------------#
tk = tkinter.Tk()
tk.geometry('1090x470+70+100')
# tk.resizable(width = False, height = False)#不知为何在别人电脑上虽然能够运行，但排版乱了
tk.title("小鱼发卡助手")

frame1 = Frame(tk, width=900, height=500)
frame2 = Frame(tk, width=100, height=500)
frame3 = Frame(tk, width=1000, height=100)

tree = ttk.Treeview(frame1, height=20, show="headings",columns=("序号", "订单编号", "订单日期", "订单信息", "金额", "卡密", "订单链接"))  # 表格  # 表格
tree.column("序号", width=37, anchor='center')
tree.column("订单编号", width=135, anchor='center')  # 表示列,不显示
tree.column("订单日期", width=135, anchor='center')
tree.column("订单信息", width=250, anchor='center')
tree.column("金额", width=50, anchor='center')
tree.column("卡密", width=70, anchor='center')
tree.column("订单链接", width=40, anchor='center')

tree.heading("序号", text="序号")  # 显示表头
tree.heading("订单编号", text="订单编号")
tree.heading("订单日期", text="订单日期")
tree.heading("订单信息", text="订单信息")
tree.heading("金额", text="金额")
tree.heading("卡密", text="卡密")
tree.heading("订单链接", text="链接(双击打开)")

y_scrollbar = Scrollbar(frame1, orient=VERTICAL, command=tree.yview)
tree.configure(yscrollcommand=y_scrollbar.set)
y_scrollbar.grid(row=0, column=1, sticky=NS)

x_scrollbar = Scrollbar(frame1, orient=HORIZONTAL, command=tree.xview)
tree.configure(xscrollcommand=x_scrollbar.set)
x_scrollbar.grid(row=1, column=0, sticky=EW)

Label(frame2, text='小鱼发卡助手', font=('宋体', 20)).grid(row=0, column=0, columnspan=4, pady=5)
variable = StringVar()
variable.set("天辉发卡")
faka_lists = ttk.Combobox(frame2, width=8, textvariable=variable,
                          values=("天辉发卡", "个人发卡", "920发卡", "发卡网", "易友发卡", "331发卡", "510发卡"), state='readonly')
faka_lists.grid(row=1, column=0)
Label(frame2, text='请输入弱口令：').grid(row=1, column=1, padx=3, pady=10, sticky=N)
key_entry = Entry(frame2, width=17)
key_entry.insert(INSERT,'123456')

Button(frame2, text='搜索', command=search).grid(row=1, column=3, pady=5)
Label(frame2, text='卡密信息:').grid(row=2, column=0, sticky=SW)
Button(frame2, text='随机key', command=random_key).grid(row=2, column=2, pady=5, padx=5, sticky=E)
Button(frame2, text='停止', command=stop).grid(row=2, column=3, pady=5)
secret_text = scrolledtext.ScrolledText(frame2, width=45, height=22, fg='blue')
segmentation_line = Canvas(frame3, width=1085, height=0.5, bg='#828790')

message_label = Label(frame3, text='软件仅供技术交流和研究，所有数据均采集第三方，请勿用于非法用途!').grid(row=1, column=0, sticky=W)
progress_bar_text = Label(frame3, text='进度：')
progress_bar = Canvas(frame3, width=640, height=10, bg='white')

tree.grid(row=0, column=0, sticky=NSEW)
secret_text.grid(row=3, column=0, columnspan=4, sticky=N)
key_entry.grid(row=1, column=2, padx=5, pady=10, sticky=N)
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=1, column=0, columnspan=2)
segmentation_line.grid(row=0, column=0, columnspan=2)
progress_bar_text.grid(row=1, column=1, sticky=W)
progress_bar.grid(row=1, column=1, sticky=E)

secret_text.insert(INSERT,
'''             欢迎使用小鱼发卡助手

1.天辉发卡：挂与辅助卡密，平台用户较多
2.个人发卡：个人的发卡平台，目前主售京东卡密，平台用户较多
3.920发卡：挂，平台用户一般
4.发卡网：无卡密卡密商品信息，用处不大
5.易友发卡：主要视频会员卡密，平台用户较多
6.331发卡网：主要游戏外挂与辅助，平台用户较多
7.510发卡：主要游戏外挂与辅助，平台用户较多
6.软件无法打开网页或无法爬取数据时请检查网络连接，或是网站拉黑了IP，这种情况需更换IP，或是等一会儿再爬
7.软件为学习爬虫开发的初级程序，使用过程中出现卡顿，卡死，爬取效率低下等情况纯属正常

warning：本软件仅供学习交流使用，所有数据来源于第三方，切勿用于非法用途
''')
tree.bind('<ButtonRelease-1>',show_secret)
tree.bind('<Double-1>', open_url)

tk.mainloop()
#------------------------------------------------------------------------------------------#
if __name__ == "__main__":
    pass

