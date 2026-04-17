import json
import boto3
import os
from decimal import Decimal

# 1. This is the "Translator" helper
# DynamoDB sends numbers as 'Decimal' objects which React/JSON can't read.
# This converts them to standard numbers so the loading screen disappears.
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

# Ensure this matches your long table name from the seeder
TABLE_NAME = os.environ.get('TABLE_NAME', 'exam-app-backend-QuestionTable-TJKB2EPIJNK2')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # 2. Get the items
        response = table.scan()
        items = response.get('Items', [])

        # 3. Return a standard Proxy Response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            # We use the helper here to sanitize the JSON body
            "body": json.dumps(items, default=decimal_default)
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": { "Access-Control-Allow-Origin": "*" },
            "body": json.dumps({"error": str(e)})
        }