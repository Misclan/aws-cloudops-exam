import json
import boto3
import os

# Grab the Table Name from environment variables (best practice!)
TABLE_NAME = os.environ.get('TABLE_NAME', 'QuestionTable')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # Scan the table to get all questions
        response = table.scan()
        items = response.get('Items', [])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"  # Required for browser access
            },
            "body": json.dumps(items)
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to fetch questions"})
        }