import json, os
import boto3

bucket_name = os.environ['S3_BUCKET']

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

def list(event, context):

    print("READ [" + bucket_name + "] sw3 bucket ... ")
    items = []
    resp = boto3.client('s3').list_objects_v2(Bucket=bucket_name)

    counter = 0
    for obj in resp['Contents']:
        if obj['Size'] == 0:
            continue

        counter += 1
        print(obj['Key'] + ' :: ' + str(sizeof_fmt(obj['Size'])))
        # items.append({'key': obj['Key'], 'size': sizeof_fmt(obj['Size'])})

        line = "{counter} :: {key} :: {size}".format(
            counter=counter,
            key=obj['Key'],
            size=sizeof_fmt(obj['Size'])
        )
        items.append(line)

    return {
        "statusCode": 200,
        "body": json.dumps(items)
    }
