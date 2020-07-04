import json, os
import boto3

bucket_name = os.environ['S3_BUCKET']
bucket = boto3.resource('s3').Bucket(bucket_name)

def list(event, context):

    print("READ [" + bucket_name + "] sw3 bucket ... ")
    items = []
    for obj in bucket.objects.all():
        print(obj)
        items.append(obj)

    return {
        "statusCode": 200,
        "body": json.dumps(items)
    }
