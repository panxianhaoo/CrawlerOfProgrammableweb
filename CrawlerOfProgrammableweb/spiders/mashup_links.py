import scrapy

pre = "https://www.programmableweb.com"


class web(scrapy.Spider):
    name = "mashup_links"

    def start_requests(self):
        urls = [
            'https://www.programmableweb.com/category/all/mashups']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        f = open('./mashup_links.json', 'a')
        links = response.xpath(
            '//*[@id="block-system-main"]/article/div[7]/div[1]/table/tbody/tr/td[1]/a/@href').extract()
        for item in links:
            print(item)
            f.write(pre + item + "\n")
        next_page = response.css('li.pager-last a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
