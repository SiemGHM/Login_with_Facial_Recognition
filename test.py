import boto3

img = open("siem.jpeg", "rb")
dmx=img.read()

def add_faces_to_collection(bucket, photo, collection_id, idn):
        client = boto3.client('rekognition',
                              aws_access_key_id=access_key_id,
                              aws_secret_access_key=secret_access_key,
                              region_name='us-east-2'
                              )

        response = client.index_faces(CollectionId=collection_id,
                                      Image={'S3Object': {
                                          'Bytes': photo,
                                          'Bucket': bucket,'Name': photo}},
                                      ExternalImageId=idn,
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

            print('Face not detected, Please provide clear photo!')
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
        CollectionId='Collection',
        Image={'Bytes': source_bytes}
    )

    # since response is a dictionary, we can loop it
    #print(response)
    return response




access_key_id='AKIA3SLO3MAN7CIUHAY6'
secret_access_key='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'


client = boto3.client('rekognition',
                              aws_access_key_id=access_key_id,
                              aws_secret_access_key=secret_access_key,
                              region_name='us-east-2'
                              )


s3 = boto3.client('s3',
                              aws_access_key_id=access_key_id,
                              aws_secret_access_key=secret_access_key,
                              region_name='us-east-2'
                              )


client = boto3.client('rekognition',
                              aws_access_key_id=access_key_id,
                              aws_secret_access_key=secret_access_key,
                              region_name='us-east-2')

 

response = client.list_faces(CollectionId='webappcollection',
                                         MaxResults=10)
# response = client.index_faces(
#     CollectionId='webappcoll',
#     Image={
#         'Bytes': img,
#         'S3Object': {
#             'Bucket': 'webapplogin',
#             'Name': 'string',
#             'Version': 'string'
#         }
#     },
#     ExternalImageId='siem',
#     DetectionAttributes=[
#         'DEFAULT',
#     ],
#     MaxFaces=123,
#     QualityFilter='NONE'
# )


# response = add_faces_to_collection('webapplogin', img, 'webappcoll', 'asdhjk')

print(response)

# ress3 = s3.upload_fileobj(img, 'webapplogin', 'username')

# response = recognizeFace()
# print(response)



# {'StatusCode': 200, 'CollectionArn': 'aws:rekognition:us-east-2:795338301467:collection/webappcollection', 'FaceModelVersion': '5.0', 'ResponseMetadata': {'RequestId': '6a131768-3ff1-4135-bceb-8df4cd3f52d4', 'HTTPStatusCode': 200, 'HTTPHeaders': {'content-type': 'application/x-amz-json-1.1', 'date': 'Sun, 25 Apr 2021 13:58:47 GMT', 'x-amzn-requestid': '6a131768-3ff1-4135-bceb-8df4cd3f52d4', 'content-length': '128', 'connection': 'keep-alive'}, 'RetryAttempts': 0}}