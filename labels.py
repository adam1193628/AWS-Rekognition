import boto3
from pprint import pprint
import helper

client = boto3.client('rekognition')

imgurl = 'https://images.unsplash.com/photo-1581579186913-45ac3e6efe93?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8M3x8ZG9ncyUyMGFuZCUyMHBlb3BsZXxlbnwwfHwwfHw%3D&w=1000&q=80'
imgbytes = helper.get_image_from_url(imgurl)

result = client.detect_labels(Image={'Bytes': imgbytes})

#pprint(result)
for label in result['Labels']:
    print(label['Name'],label['Confidence'])

