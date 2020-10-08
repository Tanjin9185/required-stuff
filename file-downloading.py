#using requests

import requests

url =" link of file or location" 

myfile = requests.get(url)

open("location/filename",'wb').write(myfile.content).close()

#using wget
#pip3 install wget
import wget
url = "link of file location"

wget.downlaod(url,"new download file name with location")

#download all jp images for a site

wget -A "*.jpg" -r http://www.yoursite.com

