import boto3
import json

# Initialize the DynamoDB resource
# Note: Ensure your terminal is still set to af-south-1
dynamodb = boto3.resource('dynamodb', region_name='af-south-1')
table = dynamodb.Table('exam-app-backend-QuestionTable-TJKB2EPIJNK2') # Make sure this matches your template.yaml

questions = [
  {
    "QuestionID": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
    "QuestionText": "A SysOps administrator is configuring an Amazon CloudWatch alarm to monitor CPU utilization for an Auto Scaling group. The alarm should trigger when average CPU utilization exceeds 80% for three consecutive periods of 5 minutes each. Which combination of settings should be used?",
    "Options": [
      "Statistic: Average, Period: 300 seconds, Evaluation Periods: 3, Datapoints to Alarm: 3",
      "Statistic: Maximum, Period: 300 seconds, Evaluation Periods: 3, Datapoints to Alarm: 1",
      "Statistic: Average, Period: 60 seconds, Evaluation Periods: 15, Datapoints to Alarm: 15",
      "Statistic: Sum, Period: 300 seconds, Evaluation Periods: 3, Datapoints to Alarm: 1"
    ],
    "CorrectAnswer": "A"
  }
]

print("Starting upload...")
with table.batch_writer() as batch:
    for q in questions:
        batch.put_item(Item=q)
print("Upload complete!")



#alternatively if you want to generate unique IDs automatically, you can use the uuid library as shown below:
import boto3
import uuid

dynamodb = boto3.resource('dynamodb', region_name='af-south-1')
table = dynamodb.Table('QuestionTable') # Use your real table name

new_questions = [
    {"text": "Which AWS service is used for object storage?", "opts": ["S3", "EC2", "RDS"], "ans": "S3"},
    # Add more here...
]

with table.batch_writer() as batch:
    for q in new_questions:
        batch.put_item(
            Item={
                'QuestionID': str(uuid.uuid4()), # Generates a unique ID automatically
                'QuestionText': q['text'],
                'Options': q['opts'],
                'CorrectAnswer': q['ans']
            }
        )
print("Seeding complete!")
