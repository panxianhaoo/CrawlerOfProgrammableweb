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
        key.insert(0, 'Name')
        value.insert(0, response.meta['apiname'])
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
