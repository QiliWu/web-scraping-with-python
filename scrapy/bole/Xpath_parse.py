# -*- coding:utf-8 -*-
#using Xpath to parse the url

import re

def parse_detail(self,response):
    #title
    title = response.xpath('//[@class="entry_header"]/h1/text()').extract_first()
    # creat_time
    creat_time = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()')\
        .extract_first().replace('.','').strip()
    # up_num
    up_num = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract_first()
    #fav_num
    fav_num = response.xpath('//span[contains(@class,"bookmark_btn")]/text()').extract_first()
    #re.match(): 只匹配开头，？匹配前面的0次或1次；\d匹配任意数字
    match_re = re.match('.*?(\d+).*',fav_num)
    if match_re:
        fav_num = match_re.group(1)
    else:
        fav_num = 0

    #comment_num
    comment_num = response.xpath('//[@href="#article-comment"]/span/text()').extract_first
    match_re = re.match('.*?(\d+).*',comment_num)
    if match_re:
        comment_num = match_re.group(1)
    else:
        comment_num = 0

    #main text
    content = response.xpath('//div[@class="entry"]').extract_first()
    #tags
    tags_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
    tags_list = [element for element in tags_list if not element.strip().endswith('评论')]
    tags = ','.join(tags_list)
