import boto3
from pprint import pprint
import helper

client = boto3.client('rekognition')

#imgurl = 'https://res.cloudinary.com/crunchbase-production/image/upload/c_thumb,h_170,w_170,f_auto,g_faces,z_0.7,b_white,q_auto:eco,dpr_1/v1467720519/nbjaqjuh8ym0gqoadwnu.jpg'
imgfilename = 'images/SalamPic.jpg'
#imgbytes = helper.get_image_from_url(imgurl)
imgbytes = helper.get_image_from_file(imgfilename)
result = client.detect_faces(Image={'Bytes': imgbytes}, Attributes=['ALL'])

pprint(result)
#for label in result['Labels']:
 #   print(label['Name'],label['Confidence'])
