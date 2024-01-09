import requests

#Get raw image data given a URL
def get_image_from_url(imgurl):
    resp=requests.get(imgurl)
    imgbytes = resp.content
    return imgbytes

#Get raw image data from local directory
def get_image_from_file(filename):
    with open(filename, 'rb') as imgfile:
        return imgfile.read()