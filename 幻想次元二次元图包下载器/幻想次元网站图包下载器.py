import os
import requests
from requests.packages.urllib3.exceptions import *
from lxml import etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36'
}
page_num = input('(动漫图片小爬虫)请输入你要爬取的页数(不超过8)：')
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
dir = os.getcwd()
print(dir)
if not os.path.exists(dir +'\\动漫图片'):
    path = os.makedirs(dir + '\\动漫图片')
    print('已创建文件夹[动漫图片]......')
else:
    pass

page = 0
while page != int(page_num):
    session = requests.session()
    page = page + 1
    url = 'https://acg18.life/category/picture/normal/page/'+ str(page)
    print('第'+str(page)+'页链接：'+url)
    html = session.get(url,headers = headers,verify=False).text
    html = etree.HTML(html)
    titlelist = html.xpath('//ul[@class="posts-ul"]//h2/a/text()')
    hreflist  = html.xpath('//ul[@class="posts-ul"]//h2/a/@href')
    print(hreflist)
    for title,href in zip(titlelist,hreflist):
        print('正在下载此链接所有图册：'+href +title)
        try:
            html = requests.get(href,headers = headers,verify = False).text
        except:
            continue
        html = etree.HTML(html)
        hreflist = html.xpath('//div[@class="entry"]//@lazydata-src')
        i = 0
        for href in hreflist:
            try:
                res = session.get(href,headers = headers,verify=False).content
            except:
                continue
            i = i+1
            dirname = title.replace('/','')
            if not os.path.exists(dir + '\\动漫图片\\' + dirname):
                path = os.makedirs(dir + '\\动漫图片\\' + dirname)
                print('已创建文件夹[' + dirname+']......')
            else:
                pass
            filename = dir + '\\动漫图片\\' + dirname +'\\' + title.replace('/','') + href.split('/')[-1]
            if not os.path.exists(filename):
                with open(filename,'wb') as f:
                    f.write(res)
                    print(href+'下载完成......')
            else:
                continue

        print('此链接所有图册：' + href + title + "下载完成......\n")
