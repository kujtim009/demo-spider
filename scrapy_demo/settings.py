# settings.py

BOT_NAME = 'scrapy_demo'

SPIDER_MODULES = ['scrapy_demo.spiders']
NEWSPIDER_MODULE = 'scrapy_demo.spiders'

# Add Your ScrapeOps API Key
SCRAPEOPS_API_KEY = 'd494d174-1c5f-4d83-a572-e55e1d603723'

# Add In The ScrapeOps Extension
EXTENSIONS = {
    'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500,
}

# Update The Download Middlewares
DOWNLOADER_MIDDLEWARES = {
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
}
