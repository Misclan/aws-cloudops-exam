import json
import boto3
import os

# Use the exact table name from your SAM/CloudFormation
TABLE_NAME = os.environ.get('TABLE_NAME', 'exam-app-backend-QuestionTable-TJKB2EPIJNK2')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # 1. Get the data
        response = table.scan()
        items = response.get('Items', [])

        # 2. Return EXACTLY what React fetch() needs
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            # This must be a raw JSON string of the list
            "body": json.dumps(items)
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": { "Access-Control-Allow-Origin": "*" },
            "body": json.dumps({"error": str(e)})
        }