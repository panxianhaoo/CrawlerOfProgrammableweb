import scrapy

pre = "https://www.programmableweb.com"


def write_data(file, data):
    w = open(file, 'a+')
    w.write(data + '\n')


class web(scrapy.Spider):
    name = "api_info_links"

    def start_requests(self):
        f = open('./api_links.json', 'r')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        addr = str(response.xpath('//*[@id="version-details-field"]/div[4]/div[1]/span/a/@href').extract()[0])
        api_name = str(response.xpath(
            '/html/body/div[5]/div[1]/section/div[2]/section/article/header/div[1]/div[1]/div[1]/h1/text()').extract()[
                           0])
        print(addr)
        print(api_name)
        write_data('./api_info_links.json', pre + addr + '#####' + api_name)
