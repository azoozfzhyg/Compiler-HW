import scrapy
import re
#import the itemfeild you made in items.py
from email_scraper.items import EmailScraperItem
class EmailSpider9000(scrapy.Spider):
    name = "email_spider_9000"
    start_urls = [
        'https://ccis.ksu.edu.sa/en'#insert the url you want to scrape here
    ]
    email_regex = re.compile('[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
    
    def parse(self, response):
        page_text = response.text
        emails = set(re.findall(self.email_regex, page_text))
        for email in emails:
            item = EmailScraperItem()
            item['email'] = email
            yield item
        # Save emails to a file usually you do that in the terminal but this is a simple way to do it in the code
        with open('emails.txt', 'w') as f:
            for email in emails:
                f.write(email + '\n')