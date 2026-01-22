from flask import Flask, render_template, request, redirect, session
import os
import logging
from dotenv import load_dotenv
load_dotenv()

from services.make_service import send_to_make
from services.validators import validate_form

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Config (single source of truth)
app.config["MAKE_WEBHOOK_URL"] = os.getenv("MAKE_WEBHOOK_URL")
app.config["MAKE_API_KEY"] = os.getenv("MAKE_API_KEY")

# Home route
@app.route("/")
def home():
    return render_template("welcome.html")

# Form page
@app.route("/form")
def form():
    return render_template("index.html")

# Form submission
@app.route("/submit", methods=["POST"])
def submit():
    form_data = validate_form(request.form)

    if not form_data:
        logger.warning("Form validation failed")
        return redirect("/error")

    # Send to Make and check response
    success = send_to_make(form_data)
    if not success:
        logger.error("Failed to send form data to Make webhook")
        return redirect("/error")

    session["form_data"] = form_data
    return redirect("/thankyou")

# Thank you page
@app.route("/thankyou")
def thankyou():
    return render_template(
        "thankyou.html",
        form_data=session.get("form_data")
    )

# Error page
@app.route("/error")
def error():
    return render_template("error.html")

if __name__ == "__main__":
    app.run()
