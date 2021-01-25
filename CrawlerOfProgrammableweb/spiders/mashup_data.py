import json
import scrapy
import re

pre = "https://www.programmableweb.com"


class web(scrapy.Spider):
    name = "mashup_data"

    def start_requests(self):
        f = open('./mashup_links.json', 'r')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url.split('#####')[0], callback=self.parse)

    def parse(self, response, **kwargs):
        key = list(response.xpath('//*[@id="tabs-content"]/div[1]/div/label').extract())
        value = list(response.xpath('//*[@id="tabs-content"]/div[1]/div/span').extract())
        desc = response.xpath('//*[@id="tabs-header-content"]/div/div[1]/div/div/div/text()').extract_first()
        del (value[0])
        key = list(map(lambda item: item.lstrip('<label>').split('</label>')[0], key))
        value = list(map(handle_value, value))

        key.insert(0, 'Desc')
        value.insert(0, desc)
        key.insert(0, 'Name')
        value.insert(0, re.findall(r'<h1>Mashup: (.*?)</h1>', response.xpath(
            '/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[2]/div[1]/h1').extract_first())[0])
        res = dict(zip(key, value))

        write_data('./mashup_data.json', json.dumps(res))


def handle_value(item):
    item = str(item[6:])
    if not item.startswith('<a'):
        return item.split('</span>')[0]
    else:
        return ",".join(re.findall(r'<a.*?>(.*?)</a>', item))


def write_data(file, data):
    w = open(file, 'a')
    w.write(data + '\n')
