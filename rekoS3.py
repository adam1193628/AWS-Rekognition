import boto3
from pprint import pprint
import helper

if __name__=="__main__":
    bucket = 'salambucket3'
    photo = 'Picture1.jpg'

client = boto3.client('rekognition')

#use this for fetching image from URL
#imgurl = 'https://c8.alamy.com/comp/HRF76Y/the-pentagon-HRF76Y.jpg'
#imgbytes = helper.get_image_from_url(imgurl)

#result = client.detect_labels(Image={'Bytes': imgbytes})
response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':photo}},MaxLabels=10)
#pprint(result)
for label in response['Labels']:
    print(label['Name'],label['Confidence'])

