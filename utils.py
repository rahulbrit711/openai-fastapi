from openai import AzureOpenAI
import os

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version="2024-02-01"
)


def generate_description(input):
    response = client.chat.completions.create(
        model="gpt-35-turbo",
        messages=[
            {"role": "system", "content": "You are an advanced social media content creator specializing in generating viral content. Your expertise helps users create highly engaging and shareable posts. Generate powerful and viral keywords and video captions."},
            {"role": "user", "content": input},
        ]
    )

    reply = response.choices[0].message.content
    return reply
