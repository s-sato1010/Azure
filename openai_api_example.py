import os
import openai

# APIキーとエンドポイントを環境変数から取得
openai.api_key = os.getenv("6104f0288cf246fda4e1468f2c902bca")
openai.api_base = os.getenv("https://openai-sdpf-gpt4custom.openai.azure.com/")

# Azure OpenAIにリクエストを送る
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Azure OpenAIを使って何ができますか？",
    max_tokens=50
)

print(response.choices[0].text.strip())
