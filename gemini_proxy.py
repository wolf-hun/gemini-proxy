from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ide az API kulcsodat tedd
# Put your API key here
GEMINI_API_KEY = "API-KEY"
# Az API kulcs megszerzéséhez: https://aistudio.google.com/prompts és kattints a Get API Key gombra
# majd a Create API key-re
# To get the API key: https://aistudio.google.com/prompts and click on Get API Key
# then Create API key
GEMINI_MODEL = "gemini-1.5-flash-latest"
# Válaszható modellek | Available models
# gemini-2.0-flash-lite https://ai.google.dev/gemini-api/docs/pricing#gemini-2.0-flash-lite
# gemini-1.5-flash-latest -- Kedvencem | My favorite https://ai.google.dev/gemini-api/docs/pricing#gemini-1.5-flash
# gemini-1.5-pro https://ai.google.dev/gemini-api/docs/pricing#gemini-1.5-pro

GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"

@app.route("/v1/chat/completions", methods=["POST"])
def chat_completion():
    data = request.get_json()

    # Prompt összeállítása OpenAI formátumból
    # Compile prompt from OpenAI format
    messages = data.get("messages", [])
    prompt_text = "\n".join([f"{msg['role']}: {msg['content']}" for msg in messages])

    # Gemini API kérés formázása
    # Gemini API request formatting
    gemini_payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt_text}]
            }
        ]
    }

    # API hívás
    # API call
    response = requests.post(GEMINI_URL, json=gemini_payload)

    if response.status_code != 200:
        return jsonify({
            "error": "Gemini API error",
            "status": response.status_code,
            "details": response.text
        }), response.status_code

    gemini_data = response.json()

    try:
        content = gemini_data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        content = "Hiba történt a Gemini válasz feldolgozása közben."

    return jsonify({
        "id": "chatcmpl-gemini-proxy",
        "object": "chat.completion",
        "created": 0,
        "model": GEMINI_MODEL,
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": content
                },
                "finish_reason": "stop"
            }
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

