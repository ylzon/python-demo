#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests,time,json
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
def get_detail(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
# url = "https://book.douban.com/subject/34869428/"
    web_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(web_data.text,'lxml')
    dom = soup.select('#interest_sectl > div > div.rating_self.clearfix > strong')
    if dom:
        rank = dom[0].get_text().strip()
        return rank
    else: 
        return '未找到'
def get_book(title):
    url = "https://book.douban.com/j/subject_suggest?q=%s"%title
    rsp = requests.get(url,headers=headers)
    rs_dict = json.loads(rsp.text)
    # print(rs_dict)
    if rs_dict:
        url_ = rs_dict[0]['url']
        return title,get_detail(url_)
    else:
        return title,'未找到'

if __name__ == '__main__':
    book_list=[
        "持续增长：从零搭建企业新媒体运营体系",
        "客户成功：持续复购和利润陡增的基石",
        "企业IT架构转型之道",
        "商业的本质",
        "本质",
        "SaaS创业路线图",
        "数字化转型的道与术",
        "赋能：打造应对不确定性的敏捷团队",
        "商业的力量",
        "联盟：互联网时代的人才变革",
        "重新定义公司：谷歌是如何运营的",
        "影响力（珍藏版）",
        "深度思考：不断逼近问题的本质",
        "责任病毒：如何分派任务和承担责任",
        "凤凰项目：一个IT运维的传奇故事 修订版",
        "创业维艰：如何完成比难更难的事",
        "掌控：开启不疲惫、不焦虑的人生",
        "高效休息法",
        "商业银行IT运维智能化方法与实践",
        "数据赋能：IT团队技术管理实战",
        "心",
        "卓有成效的管理者",
        "销售运营管理：世界500强如何运筹帷幄、决胜市场",
        "关键对话：如何高效能沟通（原书第2版）（珍藏版）",
        "领导梯队：全面打造领导力驱动型公司（原书第2版）（珍藏版）",
    ]
    for i in book_list:
        name,rank = get_book(i)
        print(name,rank)