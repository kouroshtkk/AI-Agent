import sys
import os
import json
from openai import OpenAI
from dotenv import load_dotenv
import argparse
from prompts import system_prompt
from call_function import available_functions,call_function
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
        "role": "system",
        "content": system_prompt
    },
    {
        "role": "user",
        "content": args.user_prompt,
    }
]
for _ in range(20):
    new_response = client.chat.completions.create(model="openrouter/free",messages=messages,tools=available_functions)
    if not new_response.usage:
        raise Exception("usage api failure")
    if verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {new_response.usage.prompt_tokens}")
        print(f"Response tokens: {new_response.usage.completion_tokens}")
    messages.append(dict(new_response.choices[0].message))
    if new_response.choices[0].message.tool_calls:
        for tool_call in new_response.choices[0].message.tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            if verbose:
                result_message=call_function(tool_call,True)
            else:
                result_message=call_function(tool_call)
            if not result_message:
                raise Exception("result empty")
            if verbose:
                print(f"->\n {result_message['content']}")
            messages.append(result_message)
    else:
        print(new_response.choices[0].message.content)
        sys.exit(0)

sys.exit(1)