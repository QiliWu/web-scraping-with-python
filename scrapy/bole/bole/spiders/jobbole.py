# -*- coding: utf-8 -*-
import scrapy
from requests import Request
import re


class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/']

    def parse(self, response):
        #get every url in the text_list, and give the url to Scrapy for downloading and parsing
        article_nodes = response.css('div#archive .floated-thumb .post-thumb a')
        #get <a..../a> in th <floated-thumb><post-thumb>..</floated-thumb></post_thumb>
        for article_node in article_nodes:
            #parse the cover picture in each text, all the src attributes in img
            font_image_url = article_node.css('img::attr(src)').extract_first('')
            #parse the url of each text
            article_url = article_node.css('::attr(href)').extract_first('')
            yield Request(url=parse.urljoin(response.url,article_url), meta={'font_image_url':parse.urljoin(response.url, font_image_url)}, callback=self.parse_detail)

        #get the url of next page and parse it
        next_url = response.css('a.next.page-numbers::attr(href)').extract_first('')
        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)


    def parse_detail(self,response):
        article_item = JobboleArticleItem()
        font_image_url = response.meta.get('font_image_url','')
        title = response.css('div.entry-header h1::text').extract_first()
        creat_time = response.css('p.entry-meta-hide-on-mobile::text').extract_first()
        up_num = response.css('span.vote-post-up h10::text').extract_first()
        fav_num = response.css('span.bookmark-btn::text').extract_first()
        match_re = re.match('.*?(\d+).*', fav_num)
        if match_re:
            fav_num = match_re.group(1)
        else:
            fav_num = 0
        comment_num = response.css('a[href="#article-comment"] span::text').extract_first()
        match_re = re.match('.*?(\d+).*', comment_num)
        if match_re:
            comment_num = match_re.group(1)
        else:
            comment_num = 0
        content = response.css('div.entry').extract_first()
        tags_list = response.css('p.entry-meta-hide-on-mobile a::text').extract()
        tags_list = [element for elememt in tags_list if not elememt.strip().endswith('评论')]
        tags = ','.join(tags_list)


        article_item['title'] = title
        article_item['creat_time'] = creat_time
        article_item['url'] = response.url
        article_item['font_image_url'] = [font_image_url]
        article_item['up_num'] = up_num
        article_item['fav_num'] = fav_num
        article_item['comment_num'] = comment_num
        article_item['content'] = content
        article_item['tags'] = tags

        yield article_item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self,results,item,info):
        for key,value in results:
            font_image_path = value['path']
        item['font_image_path'] = font_image_path
        return item
