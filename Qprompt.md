You are an AWS CloudOps certification expert. Generate 25 realistic practice exam questions for the AWS SysOps Administrator Associate certification.

REQUIREMENTS:
1. Each question must be scenario-based (e.g., "A SysOps administrator notices...", "A company needs to...")
2. Provide exactly 4 plausible answer options
3. Make distractors technically valid but incorrect for the specific scenario
4. Include detailed explanations that teach the concept
5. Cover these domains:
   - Monitoring & Logging (CloudWatch, X-Ray, CloudTrail)
   - Reliability & Business Continuity (Backups, DR, Auto Scaling)
   - Deployment & Provisioning (CloudFormation, Systems Manager)
   - Security & Compliance (IAM, Config, GuardDuty)
   - Networking (VPC, Route 53, Load Balancers)
   - Cost Optimization

OUTPUT FORMAT (strict JSON array):
[
  {
    "QuestionText": "Scenario-based question here",
    "Options": [
      "Option A",
      "Option B", 
      "Option C",
      "Option D"
    ],
    "CorrectAnswer": "Exact text of correct option",
    "Explanation": "Detailed explanation including why the correct answer works and why others don't",
    "Difficulty": "easy|medium|hard",
    "Domain": "networking|security|monitoring"
  }
]

CRITICAL RULES:
- Return ONLY the JSON array, no markdown, no preamble
- Ensure all text is properly escaped (use plain quotes, no special characters)
- Make questions test understanding, not memorization
- Focus on real-world troubleshooting and best practices