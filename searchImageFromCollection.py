import csv
import boto3

# with open('credentials.csv','r') as input:
#     next(input)
#     reader=csv.reader(input)
#     for line in reader:
#         access_key_id=line[2]
#         secret_access_key=line[3]
access_key_id='AKIA3SLO3MAN7CIUHAY6'
secret_access_key='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'

photo= 'siem.jpeg'

# client access for rekognition
client=boto3.client('rekognition',
                    aws_access_key_id = access_key_id,
                    aws_secret_access_key=secret_access_key,
                    region_name='us-east-2')


#encode the image and get a response
with open(photo, 'rb') as source_image:
    source_bytes= source_image.read()

# #  to use phot from the aws s3 storage, apply this code
response= client.search_faces_by_image(
    CollectionId='Collection',
    Image={'Bytes': source_bytes}
)

#since response is a dictionary, we can loop it
print(response)

for key, value in response.items():
    if key=='FaceMatches':   #go to facematch key of the response dictionary
        if value:             #check if faceMatch have value as list

            if(value[0]['Similarity']>80):  # similarity of captured image and photo at collection should be greater than 80, just to make sure it is accurate
                print(key)

                information=value[0]['Face']['ExternalImageId'].split(".")   # remove .jpg or .png

                info=information[0].split("_")     # split the names

                name=info[0]+" "+info[1]
                authorization=info[2]

                if authorization=='a':
                    print("Name: "+ name,"\nAuthorization: Employee")

                elif(authorization=="b"):
                    print("Name: ", name ,"\nAuthorization: Blacklist")

                print("Similarity rate: ", value[0]['Similarity'],
                      "\nFace ID from collection: ", value[0]['Face']['FaceId'],
                      "\nImage ID captured photo: ", value[0]['Face']['ImageId'],
                      # "\nImage Name: ", value[0]['Face']['ExternalImageId'],    ###### note: we can put the name of the person and authorization here
                      )  # value[0] is dictionary



        else:                  #if it is empty, then there is no simillary person
            print("Unknown Person")