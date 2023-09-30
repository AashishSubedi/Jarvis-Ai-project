import os
import openai
from config import apikey


openai.api_key = os.getenv("apikey")

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k-0613",
  messages=[
    {
      "role": "system",
      "content": "write an email to a professor about assignment\n"
    },
    {
      "role": "user",
      "content": ""
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(response)

'''
{
  "id": "chatcmpl-823OOKWEoCnsFM4hGUPt8SG4hv7PN",
  "object": "chat.completion",
  "created": 1695500388,
  "model": "gpt-3.5-turbo-16k-0613",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Dear Professor [Professor's Last Name],\n\nI hope this email finds you well. I am writing to inquire about the upcoming assignment for your [Course Name] class.\n\nI have been reviewing the syllabus and lecture notes, and I wanted to confirm the details of the assignment. Could you please clarify the requirements and expectations for the assignment, such as the specific topic or question, the length, and any formatting guidelines? Additionally, when is the assignment due?\n\nI want to ensure that I am fully prepared to submit a high-quality assignment that meets all the necessary criteria. If there are any additional resources or readings that you would recommend for this assignment, please let me know as well.\n\nThank you for your time and assistance. I appreciate your guidance and look forward to your response.\n\nBest regards,\n[Your Name]"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 162,
    "total_tokens": 182
  }
}
'''