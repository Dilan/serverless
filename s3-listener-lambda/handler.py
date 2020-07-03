import json, os, sys, boto3
import Image

s3 = boto3.resource('s3')

def handle(event, context):


    size = 128

    size_split = size.split('x')

    bucket_name = "images"
    key = "shark.jpg"

    obj = s3.Object(
        bucket_name=bucket_name,
        key=key,
    )
    obj_body = obj.get()['Body'].read()

    img = Image.open(BytesIO(obj_body))
    img = img.resize((int(size_split[0]), int(size_split[1])), PIL.Image.ANTIALIAS)
    buffer = BytesIO()
    img.save(buffer, 'JPEG')
    buffer.seek(0)

    resized_key="{size}_{key}".format(size=size, key=key)
    obj = s3.Object(
        bucket_name=bucket_name,
        key=resized_key,
    )
    obj.put(Body=buffer, ContentType='image/jpeg')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
