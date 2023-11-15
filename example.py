import openai
openai.api_base = 'https://api.closeai-asia.com/v1'
openai.api_key = 'sk-KRNffiXJrD4K5DYi9E00qsYUdCk3q0fqop9Rv0eGyAHC3lbC'

from openai import OpenAI

client = OpenAI(
  api_key='sk-KRNffiXJrD4K5DYi9E00qsYUdCk3q0fqop9Rv0eGyAHC3lbC',
  base_url = 'https://api.closeai-asia.com/v1'
)

def get_completion(prompt, model="gpt-3.5-turbo-1106"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.7,
    )
    return response.choices[0].message.content

prompt = "hello chatgpt"

print(get_completion(prompt))