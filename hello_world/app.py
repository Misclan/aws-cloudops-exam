import json
import boto3
import os
from decimal import Decimal

# Grab the Table Name from environment variables (best practice!)
TABLE_NAME = os.environ.get('TABLE_NAME', 'exam-app-backend-QuestionTable-TJKB2EPIJNK2')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

# Helper to convert DynamoDB Decimals to int/float
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

def lambda_handler(event, context):
    try:
        # Scan the table to get all questions
        response = table.scan()
        items = response.get('Items', [])

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps(items, default=decimal_default)
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Failed to fetch questions"})
        }