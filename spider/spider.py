import re
import ssl
# from urllib import request
import urllib.request as ur


class Spider:
    # url = 'https://www.panda.tv/cate/kingglory'
    url = 'https://www.douyu.com/directory/game/wzry'
    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    headers = {'User-Agent': 'Mozilla/5.0'}

    root_pattern = '<p>([\w\W]*?)</p>'    # \s\S or \w\W
    name_pattern = '<span class="dy-name ellipsis fl">([\w\W]*?)</span>'
    number_pattern = '<span class="dy-num fr"  >([\s\S]*?)</span>'

    def __init__(self):
        pass

    def __fetch_content(self):
        # urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed
        ssl._create_default_https_context = ssl._create_unverified_context

        # urllib.error.HTTPError: HTTP Error 403: Forbidden
        req = ur.Request(Spider.url, headers=Spider.headers)

        # A string or An object
        # res = request.urlopen(Spider.url)
        res = ur.urlopen(req)
        # print(res)

        # htmls = str(res.read(), encoding='utf-8')
        # htmls = res.read()    ＃ bytes
        # A string
        htmls = res.read().decode('utf-8')
        # print(htmls)
        return htmls

    def __analyse_htmls(self, htmls):
        # A list
        root_htmls = re.findall(Spider.root_pattern, htmls)
        # print(root_htmls)
        htmls_return = []
        for htmls in root_htmls:
            name_html = re.findall(Spider.name_pattern, htmls)
            number_html = re.findall(Spider.number_pattern, htmls)
            html = {'name': name_html, 'number': number_html}
            htmls_return.append(html)
        # print(htmls_return)
        return htmls_return

    def __refine(self, anchors):
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0].strip()
        }
        # anchors_refined = map(l, anchors)
        # print(anchors_refined)
        return map(l, anchors)

    def __sort_seed(self, anchor):
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __sort(self, anchors):
        # Iterable
        return sorted(anchors, key=self.__sort_seed, reverse=True)

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('Rank ' + str(rank+1) + ': ' + anchors[rank]['name'] + '      ' + anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analyse_htmls(htmls)
        anchors_refined = self.__refine(anchors)
        anchors_sorted = self.__sort(anchors_refined)
        self.__show(anchors_sorted)


spider = Spider()
spider.go()
