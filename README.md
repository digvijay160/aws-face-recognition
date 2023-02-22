# AWS Face Recognition

- This is a Face Recognition Project using AWS


The image of a famous person given by the user is identified by the program.

In the background, the image is detected by Amazon Rekognition and compared with the dataset in its Collection and in the DynamoDB table.

The dataset is created by uploading images of famous people in S3 bucket, which triggers a Lambda function to create a faceprint using Rekognition, and store it in  DynamoDB table.
