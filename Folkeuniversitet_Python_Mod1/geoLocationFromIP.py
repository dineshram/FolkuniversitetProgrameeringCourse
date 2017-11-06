import bs4

__author__ = 'dram'

import re
import sys
from urllib.request import urlopen
from bs4 import BeautifulSoup

usage = "Run the script: ./geolocate.py IPAddress"

# if len(sys.argv)!=2:
#     print(usage)
#     sys.exit(0)
#
# if len(sys.argv) > 1:
#     ipaddr = sys.argv[1]

ipaddr = '95.34.158.184'

geody = "http://www.geody.com/geoip.php?ip=" + ipaddr
html_page = urlopen(geody).read()
soup = bs4.BeautifulSoup(html_page)

# Filter paragraph containing geolocation info.
paragraph = soup('p')[3]

# Remove html tags using regex.
geo_txt = re.sub(r'<.*?>', '', str(paragraph))
print(geo_txt[32:].strip())
