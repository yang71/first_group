# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse


# useful for handling different item types with a single interface


class MyspiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TestspiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class DefaultMiddleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        return response


class Museum0Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "dpm.org.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection0Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "digicol.dpm.org.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection8Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "1937china.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection17Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "artmuseum.tsinghua.edu.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection22Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "bwy.hbdjdz.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection25Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "shanximuseum.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection33Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "cfbwg.org.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection42Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "wmhg.com.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection49Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "shanghaimuseum.net" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection56Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "njmuseum.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection61Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "czmuseum.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection67Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "csmuseum.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection69Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "zhejiangmuseum.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection70Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "zmnh.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection76Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "teamuseum.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection77Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "ywj.hangzhou.gov.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection78Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "tianyige.com.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection81Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "zsbwg.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection92Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "crt.com.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection94Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "jxmuseum.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection95Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "rjjng.com.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection97Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "aymuseum.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection98Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "bdsrjng.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection190Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "xabwy.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection183Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "tibetmuseum.com.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection172Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "zunyihy.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection164Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "cddfct.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection153Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "ypzz.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Collection150Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "gzchenjiaci.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Exhibition0Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "dpm.org.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Exhibition8Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "1937china.com" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Exhibition11Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "ciae.com.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Exhibition23Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "xbpjng.cn" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response


class Exhibition24Middleware(object):

    def process_request(self, request, spider):
        pass

    def process_response(self, request, response, spider):
        if "hdmuseum.org" in request.url:
            spider.browser.get(url=request.url)
            js = "window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            row_response = spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url, body=row_response, encoding="utf8", request=request)
        else:
            return response
