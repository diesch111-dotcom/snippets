#!/usr/bin/env python3
# -*- coding: utf-8 -*-
''' url_retrieve_image.py

Retrieve and save an image from a web page using ...
urlretrieve(url[, filename[, reporthook[, data]]])

tested with Spyder IDE on LinuxMint  vegaseat 19jul2026
'''

try:
    # Python2
    from urllib import urlretrieve
except ImportError:
    # Python3
    from urllib.request import urlretrieve

# find yourself an image on an internet web page you like
# (MSW: right click on the image, look under properties and copy the address)
# actually a rare find!
image_url = "http://www.google.com/intl/en/images/logo.gif"


# extract the filename from the url
url_list = image_url.split('/')
print(url_list)  # test
image_filename = url_list[-1]

# retrieve the image from the url and save it to a file in the working directory
urlretrieve(image_url, image_filename)

print("image saved as %s"  % image_filename)

# try to show the saved image file ...
import webbrowser
webbrowser.open(image_filename)
