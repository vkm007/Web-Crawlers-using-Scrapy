import scrapy
import pandas

class BookSpider(scrapy.Spider):
    name = 'book_store'
    rows_data = []
    def start_requests(self):
        url = "http://books.toscrape.com/"
    
        yield scrapy.Request(url, callback = self.parse)
    
    def parse(self, response):
       
        for q in response.css("article.product_pod"):
            row_data = []
            link = q.css("img.thumbnail::attr(src)").get()
            title = q.css("h3 a::attr(title)").get()
            price = q.css("p.price_color::text").get()
            row_data.append(link)
            row_data.append(title)
            row_data.append(price)
            
            self.rows_data.append(row_data)
            
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None :
            next_page = response.urljoin(next_page)
            yield scrapy.Request(url = next_page, callback = self.parse)
            
        pd = pandas.DataFrame(self.rows_data, columns = {'image_url', 'book_title', 'product_price'})
        
        pd.to_csv("book_store.csv", index = False)
    
            
            
            
            
    