import json
import boto3
import os

# Use the environment variable set by your SAM/CloudFormation template
TABLE_NAME = os.environ.get('TABLE_NAME')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    try:
        # 1. Pull all items from DynamoDB
        response = table.scan()
        items = response.get('Items', [])

        # 2. Return the standard AWS Proxy Response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*", # Matches your HTML's fetch needs
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "GET,OPTIONS"
            },
            # This turns your Python list into a valid JSON array for React
            "body": json.dumps(items)
        }
        
    except Exception as e:
        print(f"Error scanning table: {str(e)}")
        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "body": json.dumps({"error": "Internal Server Error", "details": str(e)})
        }