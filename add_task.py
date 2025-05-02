import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Tasks')

def lambda_handler(event, context):
 body = json.loads(event['body'])
 task_id = str(uuid.uuid4())
 task_name = body.get('task_name', 'Untitled Task')
 table.put_item(Item={'TaskID': task_id, 'TaskName': task_name})

 return {
    'statusCode': 200,
    'body': json.dumps({'message': 'Task added', 'task_id': task_id})
 }
