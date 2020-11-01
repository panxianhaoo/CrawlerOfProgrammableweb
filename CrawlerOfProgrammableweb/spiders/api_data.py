import json
import scrapy

pre = "https://www.programmableweb.com"


class web(scrapy.Spider):
    name = "api_data"

    def start_requests(self):
        f = open('./api_info_link.json', 'r')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        name = \
        response.xpath('/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[1]/div[1]/h1').extract()[0]
        key = list(response.xpath('//*[@id="tabs-content"]/div[2]/div/label').extract())
        value = list(response.xpath('//*[@id="tabs-content"]/div[2]/div/span').extract())
        del (value[0])
        key = list(map(lambda item: item.lstrip('<label>').rstrip('</label>'), key))
        value = list(map(handle_value, value))
        key.insert(0, 'Name')
        value.insert(0, name.lstrip('<h1>').rstrip('</h1>'))
        res = dict(zip(key, value))
        write_data('./api_data.json', json.dumps(res))


def handle_value(item):
    item = str(item.lstrip('<span>').rstrip('</span>'))
    item = item.strip()
    if item.startswith('href="http'):
        return item.split('">')[1]
    if item.startswith('href="/'):
        return item.split('">')[1]
    else:
        return item


def write_data(file, data):
    w = open(file, 'a')
    w.write(data + '\n')
