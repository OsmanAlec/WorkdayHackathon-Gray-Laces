import os
from openai import OpenAI

client = OpenAI(api_key="GONEFORSECURITY")

def chatWithGerry(task_name, deadline, description):
    prompt = (
        f"I have a task called '{task_name}' due on {deadline}. "
        f"Here is the description: {description}"
        "Can you help me plan how to complete this task on time?"
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()