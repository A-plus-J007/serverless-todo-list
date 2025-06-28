import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks3')

def lambda_handler(event, context):
 body = json.loads(event['body'])
 task_id = body.get('task_id')
 if not task_id:
    return {
        'statusCode': 400,
        'body': json.dumps({'error': 'task_id is required'})
    }

 table.delete_item(Key={'TaskID': task_id})

 return {
    'statusCode': 200,
    'body': json.dumps({'message': 'Task deleted'})
 }
