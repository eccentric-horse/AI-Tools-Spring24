import os
import sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append("..")

from utilities import ChatTemplate

import json

response = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Your goal is to write a short 3 chapter sci-fi novella on the theme of AI ethics. Come up with 7 steps that will help you achieve the goal. Output these steps as a JSON array of large language model prompts.'}]})

response_json = response.completion({}).choices[0].message.content

print(response_json)
print('-------')

# Removing triple backticks from the string if present
response_json = response_json.strip('`')

# Remove the "json\n" and "\n" parts
response_json = response_json.replace('json\n', '').replace('\n', '')

plan = json.loads(response_json)

chat = ChatTemplate({
    'messages': [{'role': 'user', 'content': 'Write a short 3 chapter sci-fi novella on the theme of AI ethics.'}]})

for step in plan:
    chat.template['messages'].append({'role': 'user', 'content': step})

    message = chat.completion({}).choices[0].message
    print(message.content)
    print('-------')
    chat.template['messages'].append({'role': message.role, 'content': message.content})