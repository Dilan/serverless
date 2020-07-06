import json, os, boto3

bucket_name = os.environ['S3_BUCKET']

def get(event, context):

    id = int(event['pathParameters']['id'])

    # S3_BUCKET_STORAGE
    print(event)


    resp = boto3.client('s3').list_objects_v2(Bucket=bucket_name)
    counter = 0
    for obj in resp['Contents']:

        if obj['Size']:

            if counter == id:
                obj = boto3.resource('s3').Object(bucket_name=bucket_name, key=obj['Key'])
                f = obj.get()['Body'].read()

                return {
                    "statusCode": 200,
                    "headers": {
                      'Content-Type': 'image/png'
                    },
                    "body": f,
                    "isBase64Encoded": True
                }


            counter += 1



    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }
