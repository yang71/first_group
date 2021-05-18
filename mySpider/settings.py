# Scrapy settings for mySpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3493.3 Safari/537.36'

BOT_NAME = 'mySpider'
LOG_LEVEL = "WARNING"
SPIDER_MODULES = ['mySpider.spiders']
NEWSPIDER_MODULE = 'mySpider.spiders'

COMMANDS_MODULE = 'mySpider.commands'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'mySpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'mySpider.middlewares.MyspiderSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'mySpider.middlewares.DefaultMiddleware': 0,
    'mySpider.middlewares.Museum0Middleware': 407,
    'mySpider.middlewares.Collection0Middleware': 9527,
    'mySpider.middlewares.Collection8Middleware': 9528,
    'mySpider.middlewares.Collection17Middleware': 9529,
    'mySpider.middlewares.Collection22Middleware': 9530,
    'mySpider.middlewares.Collection25Middleware': 9531,
    'mySpider.middlewares.Collection33Middleware': 9532,
    'mySpider.middlewares.Collection42Middleware': 9533,
    'mySpider.middlewares.Collection49Middleware': 9534,
    'mySpider.middlewares.Collection150Middleware': 9650,
    'mySpider.middlewares.Collection153Middleware': 9653,
    'mySpider.middlewares.Collection164Middleware': 9664,
    'mySpider.middlewares.Collection172Middleware': 9672,
    'mySpider.middlewares.Collection183Middleware': 9683,
    'mySpider.middlewares.Collection190Middleware': 9690,
    'mySpider.middlewares.Collection56Middleware': 2333,
    'mySpider.middlewares.Collection61Middleware': 2334,
    'mySpider.middlewares.Collection67Middleware': 2335,
    'mySpider.middlewares.Collection69Middleware': 2336,
    'mySpider.middlewares.Collection70Middleware': 2337,
    'mySpider.middlewares.Collection76Middleware': 2338,
    'mySpider.middlewares.Collection77Middleware': 2339,
    'mySpider.middlewares.Collection78Middleware': 2340,
    'mySpider.middlewares.Collection81Middleware': 2341,
    'mySpider.middlewares.Collection92Middleware': 2342,
    'mySpider.middlewares.Collection94Middleware': 2343,
    'mySpider.middlewares.Collection95Middleware': 2344,
    'mySpider.middlewares.Collection97Middleware': 2345,
    'mySpider.middlewares.Collection98Middleware': 2346,
    'mySpider.middlewares.Exhibition0Middleware': 65535,
    'mySpider.middlewares.Exhibition8Middleware': 65536,
    'mySpider.middlewares.Exhibition11Middleware': 65537,
    'mySpider.middlewares.Exhibition23Middleware': 65538,
    'mySpider.middlewares.Exhibition24Middleware': 65539,
    'mySpider.middlewares.Exhibition61Middleware': 4540,
    'mySpider.middlewares.Exhibition67Middleware': 4541,
    'mySpider.middlewares.Exhibition70Middleware': 4542,
    'mySpider.middlewares.Exhibition73Middleware': 4543,
    'mySpider.middlewares.Exhibition77Middleware': 4544,
    'mySpider.middlewares.Exhibition98Middleware': 4545,
    'mySpider.middlewares.Exhibition30Middleware': 2347,
    'mySpider.middlewares.Exhibition34Middleware': 2348,
    'mySpider.middlewares.Exhibition36Middleware': 2349,
    'mySpider.middlewares.Exhibition37Middleware': 2350,
    'mySpider.middlewares.Exhibition38Middleware': 2351,
    'mySpider.middlewares.Exhibition42Middleware': 2352,
    'mySpider.middlewares.Exhibition49Middleware': 2353,
    'mySpider.middlewares.Exhibition52Middleware': 2354,
    'mySpider.middlewares.Exhibition53Middleware': 2355,
    'mySpider.middlewares.Exhibition55Middleware': 2356,
    'mySpider.middlewares.Exhibition56Middleware': 2357,
    'mySpider.middlewares.Exhibition57Middleware': 2358,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'mySpider.pipelines.MuseumPipeLine': 300,
    'mySpider.pipelines.CollectionPipeLine': 301,
    'mySpider.pipelines.ExhibitionPipeLine': 302,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# 连接数据MySQL
# 数据库地址
MYSQL_HOST =  '120.26.86.149'#'46.17.172.103'
# 数据库用户名:
MYSQL_USER =  'root'#'u606804608_jerAx'
# 数据库密码
MYSQL_PASSWORD =  'jk1803_SE'#'Password12345678'
# 数据库端口
MYSQL_PORT = 3306
# 数据库名称
MYSQL_DBNAME = 'u606804608_MuseumSpider'
# 数据库编码
MYSQL_CHARSET = 'utf8'
