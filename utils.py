import openai
import os

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def generate_description(input):
    completion = client.chat.completions.create(

        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": """
                        You are a highly advance social media viral content maker. you help users by generating highly viral content. 
                        Generate powerful and viral keywords and video captiono. """
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": input
                    }
                ]
            }
        ]
    )
    reply = completion.choices[0].message.content
    return reply
