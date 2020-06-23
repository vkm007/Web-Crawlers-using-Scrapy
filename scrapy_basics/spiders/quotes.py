import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    
    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1', 
                'http://quotes.toscrape.com/page/2',
                'http://quotes.toscrape.com/page/3']
        
        
       #Generator function
        for url in urls:
            yield scrapy.Request(url = url , callback= self.parse)
           
        
    def parse(self, response):
        page = response.url.split('/')[-2]
        filename = 'quotes-%s.html'%page
        
        for q in response.css('div.quote'):
            title = q.css('span.text::text').get()
            author = q.css('small.author::text').get()
            tags = q.css('a.tag::text').getall()
            
            yield {'title':title, 'author':author, 'tags':tags}
        
       
        
                
                