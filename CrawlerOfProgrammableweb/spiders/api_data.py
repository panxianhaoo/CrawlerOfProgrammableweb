import json
import scrapy
import re

pre = "https://www.programmableweb.com"


class web(scrapy.Spider):
    name = "api_data"

    def start_requests(self):
        f = open('./api_info_links.json', 'r')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url.split('#####')[0], callback=self.parse,
                                 meta={'apiname': url.split('#####')[1].rstrip(" \n")})

    def parse(self, response, **kwargs):
        key = list(response.xpath('//*[@id="tabs-content"]/div[2]/div/label').extract())
        value = list(response.xpath('//*[@id="tabs-content"]/div[2]/div/span').extract())
        del (value[0])
        key = list(map(lambda item: item.lstrip('<label>').split('</label>')[0], key))
        value = list(map(handle_value, value))
        key.insert(0, 'Desc')
        value.insert(0, desc_format(response.xpath('//*[@id="tabs-header-content"]/div/div[1]').extract_first()))
        key.insert(0, 'Name')
        value.insert(0, response.meta['apiname'])
        key.insert(3, 'Follwers')
        # value.insert(3, response.xpath('//*[@id="myTab"]/li[8]/a/span').extract())
        value.insert(3, response.xpath('//*[@id="myTab"]/li[8]/a/span').extract_first().lstrip('<span> (').split(')</span>')[0])
        res = dict(zip(key, value))
        write_data('./api_data.json', json.dumps(res))


def handle_value(item):
    item = str(item[6:])
    if not item.startswith('<a'):
        return item.split('</span>')[0]
    else:
        return re.findall(r'<a.*?>(.*?)</a>', item)[0]


def write_data(file, data):
    w = open(file, 'a')
    w.write(data + '\n')


def desc_format(s):
    s = s.lstrip('<div class=\"api_description tabs-header_description\">')
    if s.startswith('['):
        s = s[s.find(']') + 1:-7]
    else:
        s = s[:-7]
    return s.strip()
