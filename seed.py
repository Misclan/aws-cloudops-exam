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