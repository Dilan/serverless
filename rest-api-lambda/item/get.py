import json
import os

def get(event, context):

    id = event['pathParameters']['id']

    # S3_BUCKET_STORAGE
    print(event)

    item = { 'id': id }

    return {
        "statusCode": 200,
        "body": json.dumps(item)
    }
