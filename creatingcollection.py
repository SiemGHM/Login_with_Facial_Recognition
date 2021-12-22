#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3

access_key_id='AKIA3SLO3MAN7CIUHAY6'
secret_access_key='e8zJrOs52oIIJ5+BgFnTKihO7tC04UsiG7/NzrU9'

def create_collection(collection_id):

    access_key_id='AKIA3SLO3MAN7CIUHAY6'
    secret_access_key='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'

    photo= 'siem.jpeg'

    # client access for rekognition
    client=boto3.client('rekognition',
                        aws_access_key_id = access_key_id,
                        aws_secret_access_key=secret_access_key,
                        region_name='us-east-2')

    #Create a collection
    print('Creating collection:' + collection_id)
    response=client.create_collection(CollectionId=collection_id)
    print('Collection ARN: ' + response['CollectionArn'])
    print('Status code: ' + str(response['StatusCode']))
    print('Done...')
    
def main():
    collection_id='webappcollection2'
    create_collection(collection_id)

# if __name__ == "__main__":
#     main()    



import boto3

def list_collections():

    max_results=2
    
    client=boto3.client('rekognition',
                        aws_access_key_id = access_key_id,
                        aws_secret_access_key=secret_access_key,
                        region_name='us-east-2')


    #Display all the collections
    print('Displaying collections...')
    response=client.list_collections(MaxResults=max_results)
    collection_count=0
    done=False

    print(response)
    
    while done==False:
        collections=response['CollectionIds']

        for collection in collections:
            print (collection)
            collection_count+=1
        if 'NextToken' in response:
            nextToken=response['NextToken']
            response=client.list_collections(NextToken=nextToken,MaxResults=max_results)
            
        else:
            done=True
    print(response)
    return collection_count   

def main():

    collection_count=list_collections()
    print("collections: " + str(collection_count))
if __name__ == "__main__":
    main()