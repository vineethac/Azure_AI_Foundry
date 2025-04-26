'''
Sample code to interact with Azure OpenAI model with streaming response.

'''

from openai import AzureOpenAI

ENDPOINT = "your_endpoint"
MODEL_NAME = "model_name"
DEPLOYMENT = "deployment_name"

SUBSCRIPTION_KEY = "your_api_key"
API_VERSION = "2024-12-01-preview"

client = AzureOpenAI(
    api_version = API_VERSION,
    azure_endpoint = ENDPOINT,
    api_key = SUBSCRIPTION_KEY,
)

response = client.chat.completions.create(
    stream=True,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful travel planner and assistant.",
        },
        {
            "role": "user",
            "content": "I am planning for a roadtrip across India for 3 weeks during mid December. \
                        Where all should I visit? I will be traveling by car from Bangalore. \
                        Can you plan the itenary for 3 weeks? How about North East?",
        }
    ],
    max_completion_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    model=DEPLOYMENT
)

for update in response:
    if update.choices:
        print(update.choices[0].delta.content or "", end="")

client.close()
