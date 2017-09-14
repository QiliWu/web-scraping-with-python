import scrapy

class GanjiSpider(scrapy.Spider):
    name = 'zufang'
    start_urls = ['http://bj.ganji.com/fang1/chaoyang/']


    def parse(self,response):
        print('aa')
        print(response)
        title_list = response.xpath(".//div[@class='f-list-item']/d1/dd[1]/a/text()").extract()
        print(title_list)
        price_list = response.xpath(".//div[@class='f-list-item']/d1/dd[5]/div[1]/span[1]/text()").extract()
        for i,j in zip(title_list, price_list):
            print(i,':',j)