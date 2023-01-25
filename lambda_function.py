import boto3
from decimal import Decimal
import json
import urllib

dynamodb=boto3.client('dynamodb')
s3=boto3.client('s3')
rekognition=boto3.client('rekognition')


#creates/adds/indexes faces in aws rekognition collection 
def add_faces(bucket,key):

    response=rekognition.index_faces(
        Image={
            "S3Object":
            {
                "Bucket":bucket,
                "Name":key
            }
        },
        CollectionId="face_rec_collection")

    return response


#updates face prints in the dynamodb table
def update_index(tableName,faceId,fullName):
    response=dynamodb.put_item(
        TableName=tableName,
        Item={
            'RekognitionId' :{'S':faceId},
            'FullName' :{'S':fullName}
        }
    )


#main function, this is called when lambda is triggered

def lambda_handler(event,context):

    #extracts bucket and its key where image is uploaded
    bucket=event['Records'][0]['s3']['bucket']['name']
    print("Recors: ",event['Records'])
    key=event['Recors'][0]['s3']['object']['key']
    print("Key: ",key)

    try:

        #calls AWS REkognition IndexFaces API to detect faces in S3Object to add into collection
        response=add_faces(bucket,key)

        #commit faceID and fullname object metaadata to dynamodb
        if response['ResponseMetadata']['HTTPStatusCode']==200:
            faceId=response['FaceRecords'][0]['Face']['FaceId']

            ret=s3.head_object(Bucket=bucket,Key=key)
            personFullName=ret['MetaData']['FullName']

            update_index('face_recognition',faceId,personFullName)
        
        print(response)

        return response

    except Exception as e:
        
        print(e)
        print("Error processing object {}  from bucket {}. ".format(key,bucket))
        raise e