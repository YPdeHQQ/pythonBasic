
"""
HTML 下载器

"""
import requests


class HtmlDownloader(object):

    def download(self, url):
        if url in None:
            return None
        user_agent = 'Mozilla/4.0 '
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            r.encoding = 'utf-8'
            return r.text
        return None