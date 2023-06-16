import openai
import os
import time


def get_completion(gpt_token, prompt, model="gpt-3.5-turbo"):
    openai.api_key = gpt_token
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,)
    return response.choices[0].message["content"]

