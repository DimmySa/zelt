# File automatically generated by Transformer v1.1.1:
# https://github.com/zalando-incubator/Transformer
import re
from locust import HttpLocust
from locust import TaskSequence
from locust import TaskSet
from locust import seq_task
from locust import task
class examples_har_example_com_har_2658470587(TaskSet):
    @seq_task(1)
    def GET_https_example_com_446694490___3145776_7746910096459644853(self):
        response = self.client.get(url='https://example.com/', name='https://example.com/', timeout=30, allow_redirects=False, headers={'pragma': 'no-cache', 'cache-control': 'no-cache', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
    @seq_task(2)
    def GET_https_example_com_446694490__favicon_ico_477561983_7192282252787536822(self):
        response = self.client.get(url='https://example.com/favicon.ico', name='https://example.com/favicon.ico', timeout=30, allow_redirects=False, headers={'referer': 'https://example.com/', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    @seq_task(3)
    def GET_http_www_iana_org_515441827__domains_example_856557110_4578921858814068970(self):
        response = self.client.get(url='http://www.iana.org/domains/example', name='http://www.iana.org/domains/example', timeout=30, allow_redirects=False, headers={'host': 'www.iana.org', 'connection': 'keep-alive', 'pragma': 'no-cache', 'cache-control': 'no-cache', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
    @seq_task(4)
    def GET_https_www_iana_org_515441827__domains_reserved_972359338_1795171734712579843(self):
        response = self.client.get(url='https://www.iana.org/domains/reserved', name='https://www.iana.org/domains/reserved', timeout=30, allow_redirects=False, headers={'host': 'www.iana.org', 'connection': 'keep-alive', 'pragma': 'no-cache', 'cache-control': 'no-cache', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8'})
    @seq_task(5)
    def GET_https_www_iana_org_515441827___css_2015_1_screen_css_1379141460_3228006617118282833(self):
        response = self.client.get(url='https://www.iana.org/_css/2015.1/screen.css', name='https://www.iana.org/_css/2015.1/screen.css', timeout=30, allow_redirects=False, headers={'referer': 'https://www.iana.org/domains/reserved', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    @seq_task(6)
    def GET_https_www_iana_org_515441827___js_2013_1_jquery_js_1115621018_6384923353985991284(self):
        response = self.client.get(url='https://www.iana.org/_js/2013.1/jquery.js', name='https://www.iana.org/_js/2013.1/jquery.js', timeout=30, allow_redirects=False, headers={'referer': 'https://www.iana.org/domains/reserved', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    @seq_task(7)
    def GET_https_www_iana_org_515441827___js_2013_1_iana_js_880739731_795287843438466235(self):
        response = self.client.get(url='https://www.iana.org/_js/2013.1/iana.js', name='https://www.iana.org/_js/2013.1/iana.js', timeout=30, allow_redirects=False, headers={'referer': 'https://www.iana.org/domains/reserved', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    @seq_task(8)
    def GET_https_www_iana_org_515441827___img_2013_1_iana_logo_header_svg_2865433306_8286412772011391445(self):
        response = self.client.get(url='https://www.iana.org/_img/2013.1/iana-logo-header.svg', name='https://www.iana.org/_img/2013.1/iana-logo-header.svg', timeout=30, allow_redirects=False, headers={'referer': 'https://www.iana.org/domains/reserved', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    @seq_task(9)
    def GET_https_www_iana_org_515441827___css_2015_1_print_css_1262356225_2435680582054204959(self):
        response = self.client.get(url='https://www.iana.org/_css/2015.1/print.css', name='https://www.iana.org/_css/2015.1/print.css', timeout=30, allow_redirects=False, headers={'referer': 'https://www.iana.org/domains/reserved', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    @seq_task(10)
    def GET_https_www_iana_org_515441827___img_2015_1_fonts_NotoSans_Bold_woff_3707309165_2627938112496965459(self):
        response = self.client.get(url='https://www.iana.org/_img/2015.1/fonts/NotoSans-Bold.woff', name='https://www.iana.org/_img/2015.1/fonts/NotoSans-Bold.woff', timeout=30, allow_redirects=False, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'referer': 'https://www.iana.org/_css/2015.1/screen.css', 'origin': 'https://www.iana.org'})
    @seq_task(11)
    def GET_https_www_iana_org_515441827___img_2015_1_fonts_NotoSans_Regular_woff_102436286_7503454197711386084(self):
        response = self.client.get(url='https://www.iana.org/_img/2015.1/fonts/NotoSans-Regular.woff', name='https://www.iana.org/_img/2015.1/fonts/NotoSans-Regular.woff', timeout=30, allow_redirects=False, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'referer': 'https://www.iana.org/_css/2015.1/screen.css', 'origin': 'https://www.iana.org'})
    @seq_task(12)
    def GET_https_www_iana_org_515441827___img_2015_1_fonts_SourceCodePro_Regular_woff_1356730278_3844145179526065349(self):
        response = self.client.get(url='https://www.iana.org/_img/2015.1/fonts/SourceCodePro-Regular.woff', name='https://www.iana.org/_img/2015.1/fonts/SourceCodePro-Regular.woff', timeout=30, allow_redirects=False, headers={'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36', 'referer': 'https://www.iana.org/_css/2015.1/screen.css', 'origin': 'https://www.iana.org'})
class LocustForexamples_har_example_com_har_2658470587(HttpLocust):
    task_set = examples_har_example_com_har_2658470587
    weight = 1
    min_wait = 0
    max_wait = 10