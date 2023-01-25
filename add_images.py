import boto3

s3=boto3.resource('s3')

#list of images fro indexing
images=[
        ('dhoni1.jpg','MS Dhoni'),
        ('dhoni2.jpeg','MS Dhoni'),
        ('dhoni3.jpg','MS Dhoni'),
        ('dhoni4.jpg','MS Dhoni'),
        ('cr1.jpg','Cristiano Ronaldo'),
        ('cr2.jpg','Cristiano Ronaldo'),
        ('cr3.jpg','Cristiano Ronaldo'),
        ('cr4.jpg','Cristiano Ronaldo'),
        ('jlaw1.jpg','Jennifer Lawrence'),
        ('jlaw2.jpg','Jennifer Lawrence'),
        ('jlaw3.jpg','Jennifer Lawrence'),
        ('jlaw4.jpg','Jennifer Lawrence'),
        ('nooyi1.jpg','Indra Nooyi'),
        ('nooyi2.jpg','Indra Nooyi'),
        ('nooyi3.jpg','Indra Nooyi'),
        ('nooyi4.jpg','Indra Nooyi')
    ]

#iterate through images to upload to s3
for image in images:
    file=open(image[0],'rb')
    object=s3.Object('face-rec-pics','index/'+image[0])
    ret=object.put(Body=file,
                    Metadata={'FullName':image[1]})

