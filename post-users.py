import boto3, json

def my_handler(event, context):

    dynamodb = boto3.client('dynamodb')
    insert = dynamodb.put_item(TableName='users', Item={'id':{'S':event["id"]},'name':{'S':event["name"]},'status':{'S':event["active"]}})

    if insert:
        return {
            'statusCode': 200,
            'body': json.dumps('Success')
        }
    else:
        return {
            'statusCode': 500,
            'body': json.dumps('Error')
        }

