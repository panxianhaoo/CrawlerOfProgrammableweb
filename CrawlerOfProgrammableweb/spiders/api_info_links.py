import scrapy

pre = "https://www.programmableweb.com"


def write_data(file, data):
    w = open(file, 'a')
    w.write(data + '\n')


class web(scrapy.Spider):

    name = "api_info_links"

    def start_requests(self):

        f = open('./api_links.json', 'r')
        urls = f.readlines()
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        addr = response.xpath('//*[@id="version-details-field"]/div[4]/div[1]/span/a/@href').extract()
        for i in range(len(addr)):
            print(addr[i])
            write_data('./api_info_link.json', pre + addr[i])
