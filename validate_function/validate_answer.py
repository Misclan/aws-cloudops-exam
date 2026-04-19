import json
import boto3
import os

# Bedrock client
bedrock = boto3.client('bedrock-runtime', region_name='us-east-1')  # Bedrock available in us-east-1

def lambda_handler(event, context):
    """
    Validates practical exam answers using AWS Bedrock (Claude Haiku)
    """
    try:
        # Parse request body
        body = json.loads(event.get('body', '{}'))
        
        question_text = body.get('question')
        user_answer = body.get('userAnswer')
        correct_answer = body.get('correctAnswer')
        
        if not all([question_text, user_answer, correct_answer]):
            return {
                'statusCode': 400,
                'headers': cors_headers(),
                'body': json.dumps({'error': 'Missing required fields'})
            }
        
        # Build prompt for Claude
        prompt = f"""You are an AWS certification expert validator. Compare the user's answer to the correct answer for this question.

Question: {question_text}

User's Answer: {user_answer}

Expected Answer: {correct_answer}

Evaluate if the user's answer is correct. Consider:
- ARN format validity (if applicable)
- Resource type and naming
- Semantic equivalence (different but correct answers)
- Key configuration elements

Respond ONLY with JSON:
{{
  "correct": true/false,
  "feedback": "Brief explanation (max 100 words)"
}}"""

        # Call Bedrock Claude Haiku
        response = bedrock.invoke_model(
            modelId='anthropic.claude-3-haiku-20240307-v1:0',
            body=json.dumps({
                'anthropic_version': 'bedrock-2023-05-31',
                'max_tokens': 300,
                'messages': [
                    {
                        'role': 'user',
                        'content': prompt
                    }
                ]
            })
        )
        
        # Parse Bedrock response
        response_body = json.loads(response['body'].read())
        claude_response = response_body['content'][0]['text']
        
        # Extract JSON from Claude's response
        validation_result = json.loads(claude_response)
        
        return {
            'statusCode': 200,
            'headers': cors_headers(),
            'body': json.dumps(validation_result)
        }
        
    except Exception as e:
        print(f'Validation error: {str(e)}')
        return {
            'statusCode': 500,
            'headers': cors_headers(),
            'body': json.dumps({
                'correct': False,
                'feedback': 'AI validation temporarily unavailable. Check explanation below.'
            })
        }

def cors_headers():
    return {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'POST,OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
