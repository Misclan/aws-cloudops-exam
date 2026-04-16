import boto3
import json
import uuid

# Configuration
REGION = 'af-south-1'
TABLE_NAME = 'exam-app-backend-QuestionTable-TJKB2EPIJNK2'

def seed_data():
    dynamodb = boto3.resource('dynamodb', region_name=REGION)
    table = dynamodb.Table(TABLE_NAME)

    # Load the JSON file
    try:
        with open('newq.json', 'r', encoding='utf-8') as f:
            questions = json.load(f)
    except FileNotFoundError:
        print("Error: newq.json not found!")
        return
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format - {e}")
        return

    print(f"Found {len(questions)} questions. Starting upload...")

    # Use batch_writer for efficiency
    with table.batch_writer() as batch:
        for idx, q in enumerate(questions, 1):
            q_id = str(uuid.uuid4())
            
            # Determine question type (default to multiple_choice)
            question_type = q.get('QuestionType', 'multiple_choice')
            
            item = {
                'QuestionID': q_id,
                'QuestionText': q['QuestionText'],
                'QuestionType': question_type,
                'CorrectAnswer': q['CorrectAnswer'],
                'Explanation': q.get('Explanation', 'No explanation provided.')
            }
            
            # Add Options for multiple choice questions
            if question_type == 'multiple_choice' or 'Options' in q:
                item['Options'] = q['Options']
            
            # Add practical question fields if present
            if 'ValidationType' in q:
                item['ValidationType'] = q['ValidationType']
            if 'AcceptedFormats' in q:
                item['AcceptedFormats'] = q['AcceptedFormats']
            
            batch.put_item(Item=item)
            print(f"✓ Uploaded question {idx}/{len(questions)}: {q_id}")

    print("\n✅ All questions successfully synced to DynamoDB!")
    print(f"\n📊 Summary:")
    print(f"   Total questions: {len(questions)}")
    
    # Count question types
    types = {}
    for q in questions:
        qtype = q.get('QuestionType', 'multiple_choice')
        types[qtype] = types.get(qtype, 0) + 1
    
    for qtype, count in types.items():
        print(f"   - {qtype}: {count}")

if __name__ == "__main__":
    print("=" * 60)
    print("AWS CloudOps Exam Question Seeder")
    print("=" * 60)
    print(f"Region: {REGION}")
    print(f"Table: {TABLE_NAME}")
    print("=" * 60 + "\n")
    
    seed_data()
