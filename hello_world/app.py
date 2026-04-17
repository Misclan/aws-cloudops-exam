import json
import boto3
import os
from decimal import Decimal

# Helper to handle DynamoDB numbers so React doesn't freeze
def decimal_default(obj):
    if isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    raise TypeError

# Explicitly using your Cape Town table name
TABLE_NAME = 'exam-app-backend-QuestionTable-TJKB2EPIJNK2'
REGION = 'af-south-1'

def lambda_handler(event, context):
    # Initialize inside the handler to ensure correct region
    dynamodb = boto3.resource('dynamodb', region_name=REGION)
    table = dynamodb.Table(TABLE_NAME)
    
    try:
        # Scan the table
        response = table.scan()
        items = response.get('Items', [])
        
        print(f"Success: Found {len(items)} items in {TABLE_NAME}")

        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,OPTIONS",
                "Access-Control-Allow-Headers": "Content-Type"
            },
            "body": json.dumps(items, default=decimal_default)
        }
    except Exception as e:
        print(f"Database Error: {str(e)}")
        return {
            "statusCode": 500,
            "headers": { "Access-Control-Allow-Origin": "*" },
            "body": json.dumps({"error": "Lambda could not reach DynamoDB", "details": str(e)})
        }