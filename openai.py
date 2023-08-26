openai.api_key = "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"

import os
import openai
response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "Write a python program to get first 10 fibonacci numbers."
    }
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response)

print(response['choices'][0]['message']['content'])