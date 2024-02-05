import os
from flask import Flask, jsonify, request
from discord_interactions import verify_key_decorator
import openai
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi

DISCORD_PUBLIC_KEY = os.environ.get("PUBKEY")

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)

@app.route("/", methods=["POST"])
async def interactions():
    print(f"👉 Request: {request.json}")
    raw_request = request.json
    return interact(raw_request)

@verify_key_decorator(DISCORD_PUBLIC_KEY)
def interact(raw_request):
    if raw_request["type"] == 1:  # PING
        response_data = {"type": 1}  # PONG
    else:
        data = raw_request["data"]
        command_name = data["name"]

        if command_name == "echo":

            api_token = os.environ.get("GPTTOKEN")
            openai.api_key = api_token
            model = 'gpt-3.5-turbo-instruct'

            original_message = data["options"][0]["value"]
            prompt = "Respond to this message as if you are Albert Wesker from Resident Evil: " + original_message

            response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            max_tokens=300  # Adjust as needed
            )
            message_content = response.choices[0].text

        response_data = {
            "type": 4,
            "data": {"content": message_content},
        }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run(debug=True)