import boto3
from pprint import pprint
import helper
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as num


def compare_faces(sourceFile, targetFile):
    client = boto3.client('rekognition')

    imageSource = open(sourceFile, 'rb')
    imageTarget = open(targetFile, 'rb')

    response = client.compare_faces(SimilarityThreshold=80,
                                    SourceImage={'Bytes': imageSource.read()},
                                    TargetImage={'Bytes': imageTarget.read()})

    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        pprint('The face at ' +
              str(position['Left']) + ' ' +
              str(position['Top']) +
              ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()
    return len(response['FaceMatches'])


def main():
    source_file = 'images/henryOld.jpg'
    target_file = 'images/henryYoung.jpg'
    face_matches = compare_faces(source_file, target_file)
    pprint("Face matches: " + str(face_matches))
    img = mpimg.imread(target_file)
    plt.imshow(img)
    plt.show()


if __name__ == "__main__":
    main()