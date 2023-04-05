import os
import wget
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y'
zip_name = "rawdata.csv"
wget.download(url, zip_name)
