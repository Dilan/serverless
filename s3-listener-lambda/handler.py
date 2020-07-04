import json, os, sys, boto3, io
import PIL
from PIL import Image

# env --------------------------------------------------------------------------
SSC_URL = os.environ['SSC_URL']


s3 = boto3.resource('s3')

def handle(event, context):



    bucket_name = "images"
    key = "shark.jpg"

    # obj = s3.Object(
    #     bucket_name=bucket_name,
    #     key=key,
    # )
    # obj_body = obj.get()['Body'].read()

    # f = open(, "rb")

    img_path = "/Users/anton.plotnikov/Node/accenture/serverless/s3-listener-lambda/images/shark.jpg"


    maxsize = (200, 200)

    img = Image.open(img_path)
    img.thumbnail(maxsize, PIL.Image.ANTIALIAS)
    img.save("car_resized.jpg", "JPEG", optimize=True)


    # resized_key="{size}_{key}".format(size=size, key=key)
    # obj = s3.Object(
    #     bucket_name=bucket_name,
    #     key=resized_key,
    # )
    # obj.put(Body=buffer, ContentType='image/jpeg')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }


if __name__ == "__main__":
    handle({}, {})
