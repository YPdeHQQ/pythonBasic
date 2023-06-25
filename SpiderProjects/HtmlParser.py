
"""HTML 解析器"""


class HtmlParser(object):

    def parser(self, page_url, html_cont):
        """
        用于解析器网页内容，抽取url和数据
        :param page_url: 下载网页的url
        :param html_cont: 下载的网页内容
        :return: 返回url和数据
        """
        if page_url in None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self, page_url, soup):
        """
        抽取新的url集合
        :param page_url: 下载页面的url
        :param soup: BeautifulSoup对象
        :return: 返回新的url集合
        """
        new_urls = set()
        # 抽取符号要求的a标记
        links = soup.find_all('a', href=re.compile(r'/view/\d+\.html'))
        for link in links:
            # 提取href属性
            new_url = link['href']
            # 拼接成完整网址
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        """
        抽取有效数据
        :param page_url: 下载页面的url
        :param soup:
        :return: 返回有效数据
        """
        data = {}
        data['url'] = page_url
        title = soup.find('dd', class_='test').find('h1')
        data['title'] = title.get_text()
        summary = soup.find('div', class_='lemma')
        # 获取tag中包含的所有文本内容，包括子孙tag中的内容，并将结果作为Unicode字符串返回
        data['summary'] = summary.get_text()
        return data

