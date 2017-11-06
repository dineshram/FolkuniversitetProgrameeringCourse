import urllib

__author__ = 'dram'

from urllib.request import urlopen

response = urlopen('http://www.python.org/')
html = response.read()


response = urlopen('http://www.voidspace.org.uk')
the_page = response.read()

