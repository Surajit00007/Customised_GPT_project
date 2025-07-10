import requests
import json

def callOLAMA(user_message, model_name="phi3"):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": model_name,
        "prompt": user_message,
        "stream": False
    }

    try:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload),
            timeout=120
        )

        if response.status_code == 200:
            result = response.json()
            bot_response = result.get("response", "Sorry, no response.")
            return bot_response.strip()
        else:
            return f"Error {response.status_code}: {response.text}"

    except Exception as e:
        return f"Exception: {str(e)}"
