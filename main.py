import os
from openai import OpenAI
from dotenv import load_dotenv
import argparse
parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt",type=str,help="User prompt")
parser.add_argument("--verbose",action="store_true",help="Enable verbose output")
args = parser.parse_args()
verbose=args.verbose

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")
if not api_key:
    raise Exception("api not found")
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key
)
messages=[
    {
        "role": "user",
        "content": args.user_prompt,
    }
]
new_response = client.chat.completions.create(model="openai/gpt-oss-20b:free",messages=messages)
if not new_response.usage:
    raise Exception("usage api failure")
if verbose:
    print(f"User prompt: {args.user_prompt}")
    print(f"Prompt tokens: {new_response.usage.prompt_tokens}")
    print(f"Response tokens: {new_response.usage.completion_tokens}")
print(new_response.choices[0].message.content)

