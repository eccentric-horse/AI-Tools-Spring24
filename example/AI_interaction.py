import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']

model_name = 'ft:gpt-3.5-turbo-0613:personal::8vqNsgCI'

template = '''You are a Q&A bot. You provide short answers to questions.
For example:
Question: What does ASL stand for? American Sign Language.
Provide the answer to the following question:
Question: '''

def answer_question(question):
    message = [{'role': 'user', 'content': template + question}]
    response = openai.chat.completions.create(
        model = model_name,
        temperature = 0,
        stop = ['\n'],
        messages = message)
    answer = response.choices[0].message.content
    return answer
