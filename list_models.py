import truststore; truststore.inject_into_ssl()
from google import genai
import sys

api_key = input("Gemini API キーを入力: ").strip()
client = genai.Client(api_key=api_key)

print("\n利用可能なモデル:")
for m in client.models.list():
    print(m.name)
