import boto3
import json
import uuid

# Configuration
REGION = 'af-south-1'
TABLE_NAME = 'exam-app-backend-QuestionTable-TJKB2EPIJNK2' # Double check this matches your YAML

def seed_data():
    dynamodb = boto3.resource('dynamodb', region_name=REGION)
    table = dynamodb.Table(TABLE_NAME)

    # 1. Load the JSON file
    try:
        with open('newq.json', 'r') as f:
            questions = json.load(f)
    except FileNotFoundError:
        print("Error: newq.json not found!")
        return

    print(f"Found {len(questions)} questions. Starting upload...")

    # 2. Use batch_writer for efficiency (it handles 25 items at a time automatically)
    with table.batch_writer() as batch:
        for q in questions:
            # Generate the UUID here so it's fresh and unique
            q_id = str(uuid.uuid4())
            
            batch.put_item(
                Item={
                    'QuestionID': q_id,
                    'QuestionText': q['QuestionText'],
                    'Options': q['Options'],
                    'CorrectAnswer': q['CorrectAnswer'],
                    'Explanation': q.get('Explanation', 'No explanation provided.')
                }
            )
            print(f"Uploaded: {q_id}")

    print("✅ All questions successfully synced to DynamoDB!")

if __name__ == "__main__":
    seed_data()