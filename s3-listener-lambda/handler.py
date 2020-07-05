import json, os, sys, boto3, io, logging
import PIL
from PIL import Image

# env --------------------------------------------------------------------------
S3_BUCKET = os.environ['S3_BUCKET']

# logging ----------------------------------------------------------------------
logger = logging.getLogger()
logger.setLevel(logging.INFO)


s3 = boto3.resource('s3')

def handle(event, context):

    print("======= EVENT ==============================")
    logger.info(event)

    if 'Records' not in event or len(event['Records']) == 0 or 's3' not in event['Records'][0]:
        logger.error('Unexpected [event]: %s', event);
        return { 'statusCode': 400, 'body': json.dumps('Unexpected [event]') }

    bucket_name = event['Records'][0]['s3']['bucket']['name']
    key         = event['Records'][0]['s3']['object']['key']
    size        = event['Records'][0]['s3']['object']['size']
    filename    = os.path.basename(key)
    resized_key = "thumbnails/{filename}".format(filename=filename)

    # download image from s3 ---------------------------------------------------
    obj = s3.Object(bucket_name=bucket_name, key=key)
    f = obj.get()['Body'].read()

    maxsize = (200, 200)
    img = Image.open(io.BytesIO(f))
    img.thumbnail(maxsize, PIL.Image.ANTIALIAS)

    buffer = io.BytesIO()
    img.save(buffer, "JPEG", optimize=True)
    buffer.seek(0)

    # upload resized file to s3 ------------------------------------------------
    boto3.client('s3').put_object(
        Bucket=S3_BUCKET,
        Key=resized_key,
        Body=buffer,
        ContentType='image/jpeg',
    )

    logger.info("Resized image stores to {key}".format(key=resized_key))

    return {
        'statusCode': 200, 'body': json.dumps('Image succesfully resized')
    }

if __name__ == "__main__":
    handle({}, {})
