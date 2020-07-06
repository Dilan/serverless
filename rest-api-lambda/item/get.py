import json, os, boto3, base64

bucket_name = os.environ['S3_BUCKET']

def get(event, context):

    id = int(event['pathParameters']['id'])

    # S3_BUCKET_STORAGE
    print(event)


    resp = boto3.client('s3').list_objects_v2(Bucket=bucket_name)
    counter = 0
    for obj in resp['Contents']:

        print(obj)

        if obj['Size'] == 0:
            continue

        counter += 1
        if counter == id:
            obj = boto3.resource('s3').Object(bucket_name=bucket_name, key=obj['Key'])
            payload = obj.get()['Body'].read()

            return {
                "isBase64Encoded": True,
                "statusCode": 200,
                "headers": { "content-type": "image/jpg"},
                'body': base64.b64encode(payload).decode("utf-8")

            }



    return {
        "statusCode": 200,
        "body": json.dumps("not found image...")
    }
