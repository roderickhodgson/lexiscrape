# Scrapy settings for lexiscrape_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'lexiscrape_crawler'

SPIDER_MODULES = ['lexiscrape_crawler.spiders']
NEWSPIDER_MODULE = 'lexiscrape_crawler.spiders'
ITEM_PIPELINES = [
    'lexiscrape_crawler.pipelines.CleanBody',
    'lexiscrape_crawler.pipelines.CleanTitle',
    'lexiscrape_crawler.pipelines.GenerateTags'
    ]

TITLE_WEIGHT = 2
BODY_WEIGHT = 1

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lexiscrape_crawler (+http://www.yourdomain.com)'
