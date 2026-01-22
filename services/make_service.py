
    
import requests
from flask import current_app

def send_to_make(form_data):
    try:
        headers = {
            "Content-Type": "application/json",
            "x-make-apikey": current_app.config["MAKE_API_KEY"]
        }

        response = requests.post(
            current_app.config["MAKE_WEBHOOK_URL"],
            json=form_data,
            headers=headers,
            timeout=10
        )

        return response.status_code == 200

    except requests.exceptions.RequestException:
        return False
