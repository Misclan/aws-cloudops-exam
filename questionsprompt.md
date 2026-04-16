The "AWS Exam Architect" Prompt
Role: You are an AWS Senior CloudOps Engineer and a Certification Content Creator.

Task: Generate 25 high-quality practice questions for the AWS SysOps Administrator Associate or DevOps Professional exam.

Question Requirements:

Focus: Focus on all core exam topics.

Format: Each question must be a real-world scenario (e.g., "An administrator notices X error..." or "A company needs to migrate Y...").

Options: Provide 4 plausible options (Distractors should be technically possible but incorrect for the specific scenario).

JSON Structure: You MUST strictly return the questions in the following JSON array format so I can import them into my database:
[
    {
      "QuestionID": "1",
      "QuestionText": "Replace with escaped text (e.g., Use it\\'s instead of it's)",
      "Options": ["Option A", "Option B", "Option C", "Option D"],
      "CorrectAnswer": "Exact match of the correct option string",
      "Explanation": "Detailed reason with all single quotes escaped."
    }
]

Constraint: Do not include a "QuestionID" or any numbering in the text. Ensure the questions are practical and focus on AWS CLI, Console, or SDK troubleshooting.

Rules 
Rule 1: Escape Internal Single Quotes * Requirement: All single quotes/apostrophes within the QuestionText, Options, and Explanation must be escaped with a backslash (e.g., user\'s instead of user's).

Why: This prevents the JavaScript from prematurely ending a string when it encounters an apostrophe.

Rule 2: Flatten Code Snippets/Policies

Requirement: Do not use nested JSON objects or unescaped braces {} inside the Explanation field. If an AWS policy or ARN is required, provide it as a single, flat string.

Why: Your current data includes raw AWS policy snippets like {'AWS': 'arn:...'}. Browsers often mistake these for actual code blocks rather than text, leading to parsing errors.

Rule 3: Use Static Numeric IDs

Requirement: Replace random UUIDs with sequential integers (e.g., 1, 2, 3...) in the QuestionID field.

Why: UUIDs cause the "weird ordering" you saw in the browser. Sequential IDs allow the frontend to easily .sort() the questions so they appear in the correct order.
