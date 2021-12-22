import boto3
import base64

access_key_id='AKIA3SLO3MAN7CIUHAY6'
secret_access_key='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'

photo= 'result.jpg'

sampres = {'SearchedFaceBoundingBox': {'Width': 0.3471413254737854, 'Height': 0.33482417464256287, 'Left': 0.30348652601242065, 'Top': 0.31462064385414124}, 'SearchedFaceConfidence': 99.99317932128906, 'FaceMatches': [{'Similarity': 100.0, 'Face': {'FaceId': '9db25d3b-0f44-4c4a-af21-cef1a136146c', 'BoundingBox': {'Width': 0.34714099764823914, 'Height': 0.33482399582862854, 'Left': 0.30348700284957886, 'Top': 0.3146210014820099}, 'ImageId': 'aec9f29d-1332-3196-81c3-539aa8281587', 'ExternalImageId': '123456789', 'Confidence': 99.99320220947266}}], 'FaceModelVersion': '5.0', 'ResponseMetadata': {'RequestId': '587a28a8-8563-4b4f-909e-30f0d1ef2b27', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'date': 'Thu, 13 May 2021 22:54:12 GMT', 'x-amzn-requestid': '587a28a8-8563-4b4f-909e-30f0d1ef2b27', 'content-length': '535', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}
# sampres = sampres['FaceMatches']['Face']['ExternalImageId']
# client access for rekognition
client=boto3.client('rekognition',
                    aws_access_key_id = access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name='us-east-2')



def add_faces_to_collection(bucket,photo,collection_id):

    bucket='webapplogin'
    collectionId='webappcollection2'
    photo=open('siem.jpeg', 'rb').read()
    encoded_string = base64.b64encode(photo)

    
    client=boto3.client('rekognition',
                    aws_access_key_id = access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name='us-east-2')

    response=client.index_faces(CollectionId=collectionId,
                                Image={
                                    'Bytes':encoded_string,},
                                    
                                ExternalImageId='siem.jpeg',
                                MaxFaces=1,
                                QualityFilter="AUTO",
                                DetectionAttributes=['ALL'])

    print ('Results for ' + photo) 	
    print('Faces indexed:')						
    for faceRecord in response['FaceRecords']:
         print('  Face ID: ' + faceRecord['Face']['FaceId'])
         print('  Location: {}'.format(faceRecord['Face']['BoundingBox']))

    print('Faces not indexed:')
    for unindexedFace in response['UnindexedFaces']:
        print(' Location: {}'.format(unindexedFace['FaceDetail']['BoundingBox']))
        print(' Reasons:')
        for reason in unindexedFace['Reasons']:
            print('   ' + reason)

def main():
    bucket='webapplogin'
    collection_id='webappcollection2'
    photo='siem.jpeg'
    
    
    indexed_faces_count=add_faces_to_collection(bucket, photo, collection_id)
    print("Faces indexed count: " + str(indexed_faces_count))


def uploadImage(filename, key):
    s3 = boto3.client('s3',
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_access_key,
                          region_name='us-east-2'
                          )
    with open(filename, 'rb') as f:
        s3.upload_fileobj(f, 'webapplogin', key )


def add_faces_to_collection(bucket, photo, collection_id):
    client = boto3.client('rekognition',
                            aws_access_key_id=access_key_id,
                            aws_secret_access_key=secret_access_key,
                            region_name='us-east-2'
                            )

    response = client.index_faces(CollectionId=collection_id,
                                    Image={'S3Object': {
                                        'Bucket': bucket,'Name': photo}},
                                    ExternalImageId=photo,
                                    MaxFaces=1,
                                    QualityFilter="AUTO",
                                    DetectionAttributes=['ALL'])

    print('Results for ' + photo)
    print('Faces indexed:')
    if response['FaceRecords']:
        print("Face Successfully added")
        for faceRecord in response['FaceRecords']:
            print('  Face ID: ' + faceRecord['Face']['FaceId'])
            print('  Location: {}'.format(
                faceRecord['Face']['BoundingBox']))
            # update the list of users avilable at the user end
            # self.list_faces_in_collection()
    else:
        messagebox.showerror(
            'Face not detected, Please provide clear photo!')
        print('Face not detected, Please provide clear photo!')
        for unindexedFace in response['UnindexedFaces']:
            print(' Location: {}'.format(
                unindexedFace['FaceDetail']['BoundingBox']))
            print(' Reasons:')
            for reason in unindexedFace['Reasons']:
                print('   ' + reason)
    return len(response['FaceRecords'])


def recognizeFace():
    photo= 'result.jpg'

    # client access for rekognition
    client=boto3.client('rekognition',
                        aws_access_key_id = access_key_id,
                        aws_secret_access_key=secret_access_key,
                        region_name='us-east-2')


    # encode the image and get a response
    with open(photo, 'rb') as source_image:
        source_bytes= source_image.read()

    # #  to use phot from the aws s3 storage, apply this code
    response= client.search_faces_by_image(
        CollectionId='webappcollection',
        Image={'Bytes': source_bytes}
    )

    # since response is a dictionary, we can loop it
    #print(response)
    return response



    

if __name__ == "__main__":
    # uploadImage("result.jpg",'123456789')
    # add_faces_to_collection('webapplogin', '123456789', 'webappcollection')
    resp = recognizeFace()
    print(resp['FaceMatches'][0]['Face']['ExternalImageId'])

