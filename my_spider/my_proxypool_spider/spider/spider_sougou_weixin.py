import requests
from bs4 import BeautifulSoup
import pymysql

class Spider(object):
    def __init__(self):
        self.headers = {
            "User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
            'Cookie':'SUV=00BD69F8DB524C7B5989864D98F0F548; dt_ssuid=5689606512; pex=C864C03270DED3DD8A06887A372DA219231FFAC25A9D64AE09E82AED12E416AC; ssuid=886764192; CXID=8C3782759866A82AAC0BD04C12F5C5ED; sct=3; SUID=8CDF52DB5D68860A590BE945000614B1; wuid=AAFZIyx4IgAAAAqLFD3O7QQAGwY=; IPLOC=CN3301; ad=nyllllllll2zsnSKQCOa1CZDOzVbQUsFnuyN3lllll9lllllROxlw@@@@@@@@@@@; ABTEST=0|1547523633|v1; SNUID=8E41055A60652029B328086460177CD4; weixinIndexVisited=1; JSESSIONID=aaaIbW4b7CGk5-jh9yfDw; ppinf=5|1547548317|1548757917|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZToxODolRTUlQTQlOUMlRTklQTMlOEV8Y3J0OjEwOjE1NDc1NDgzMTd8cmVmbmljazoxODolRTUlQTQlOUMlRTklQTMlOEV8dXNlcmlkOjQ0Om85dDJsdUFhWjhPRGNudkFILW9TSm9FMklkQklAd2VpeGluLnNvaHUuY29tfA; pprdig=n0sy2X3gfhIpHDSFeSzwCsrYJ2_yHGsK01trZp3yS08NgWAr13YhDXhh6PP429DrO4Vl4QK51QYcAWgMvAvtGhLQJk8CDG0gAp1mlMApFEsxZwwYuRcgCNW-LXs9NoPgANMg-IoY3aDqeJEtDIvz2PXeVsuAcK8eTzV96LdsqXE; sgid=01-36684935-AVw9tp2ibQsPEiazE9R82ofyw; ppmdig=15475483180000001fef908dd273db9afb9e6cf0dd865d59'
        }
        self.base_sougou_url = "https://weixin.sogou.com/weixin?"
        self.proxy = None



    def get_sougou_html(self,keyword,page_num):
        params = {
            'query':keyword,
            'type':2,
            'page':page_num,
        }
        if not self.proxy:
            response = requests.get(self.base_sougou_url,params=params,headers=self.headers,allow_redirects=False)
        else:
            print('携带代理访问',self.proxy)
            response = requests.get(self.base_sougou_url,proxies=self.proxy,params=params,headers=self.headers,allow_redirects=False)
        if response.status_code == 200:
            return response.text
        elif response.status_code == 302:
            proxy_info = requests.get('http://127.0.0.1:5000/get').text
            self.proxy = {'http':proxy_info}
            print('302,替换代理为：',proxy_info)
            self.get_sougou_html(keyword,page_num)


    def parse_sougou_html(self,html):
        soup = BeautifulSoup(html,'lxml')
        urls = soup.select(".news-list > li > .txt-box h3 a")
        for a in urls:
            yield a.attrs['href']


    def get_weixin_html(self,url):
        # print('当前访问的微信url：',url)
        response = requests.get(url,headers=self.headers)
        return response.text

    def parse_weixin_html(self,html):
        soup = BeautifulSoup(html,'lxml')
        try:
            title = soup.select("#activity-name")[0].text.strip()
            auther = soup.select('#js_profile_qrcode > div > strong')[0].text.strip()
            number = soup.select('#js_profile_qrcode > div .profile_meta_value')[0].text.strip()
            info = soup.select('#js_profile_qrcode > div .profile_meta_value')[1].text.strip()
            self.cursor.execute('insert into weixin_news(title,auther,number,info) values(%s,%s,%s,%s)',(title,auther,number,info))
            print('标题：',title)
        except:pass


if __name__ == "__main__":
    spider = Spider()
    for page_num in range(1,100):
        html = spider.get_sougou_html('校花',page_num)
        generator = spider.parse_sougou_html(html)

        spider.conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='test', charset='utf8')
        spider.cursor = spider.conn.cursor()
        for i in generator:

            spider.parse_weixin_html(spider.get_weixin_html(i))

        spider.conn.commit()#记得保存。。。