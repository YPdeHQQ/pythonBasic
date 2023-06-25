# _*_ coding: utf-8 _*_
# @Time: 2023/5/12 15:40
# @Author: 🎈
# @File: 爬虫调度器

from SpiderProjects.DataOutput import DataOutput
from SpiderProjects.HtmlDownloader import HtmlDownloader
from SpiderProjects.HtmlParser import HtmlParser
from SpiderProjects.UrlManager import UrlManager


class SpiderMan(object):

    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()

    def crawl(self, root_url):
        # 添加入口url
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url, 同时判断抓取了多少个url
        while self.manager.has_new_url() and self.manager.old_url_size()<100:
            try:
                # 从url管理器获取新的url
                new_url = self.manager.get_new_url()
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                # 将抽取的url添加到url管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.store_data(data)
                print('已经抓取 %s 个数据' %self.manager.old_url_size())
            except Exception as e:
                print('crawl failed')
        self.output.output_html()


if __name__ == '__main__':
    spider_man = SpiderMan()
    spider_man.crawl("https://baidu.com")