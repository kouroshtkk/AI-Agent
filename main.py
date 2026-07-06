import os
from openai import OpenAI
from dotenv import load_dotenv
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
        "content": "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.",
    }
]
new_response = client.chat.completions.create(model="openai/gpt-oss-20b:free",messages=messages)
print(new_response.choices[0].message.content)
def main():
    print("Hello from ai-agent!")


if __name__ == "__main__":
    main()
