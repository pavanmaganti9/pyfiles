#!c:/Python27/python
print "Content-type: text/html"
print
import urlparse
url = 'http://example.com/?q=abc&p=123'
par = urlparse.parse_qs(urlparse.urlparse(url).query)
print par['q'], par['p']