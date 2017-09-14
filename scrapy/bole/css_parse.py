import re
def parse_detail(self,response):
    title = response.css('div.entry-header h::text').extract_first()
    creat_time = response.css('p.entry-meta-hide-on-mobile::text').extract_first()
    up_num = response.css('span.vote-post-up h10::text').extract_first()
    fav_num = response.css('span.bookmark-btn::text').extract_first()
    match_re = re.match('.*?(\d+).*',fav_num)
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