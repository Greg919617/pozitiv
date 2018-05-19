import urllib
import os
import re
from urlparse import urlparse, urljoin
\
if __name__ == "__main__":
  url = "https://www.cnn.com/"
  print "Hello"
  page = urllib.urlopen(url)
  html = page.read()
  print html
