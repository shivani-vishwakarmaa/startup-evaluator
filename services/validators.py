import re
from html import escape

def validate_email(email):
    """Validate email format using regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def sanitize_string(value):
    """Remove HTML/script content and trim whitespace."""
    if not isinstance(value, str):
        return ""
    return escape(value.strip())

def validate_form(form):
    email = form.get("email", "").strip()
    name = form.get("name", "").strip()

    # Validate required fields
    if not name or len(name) < 2:
        return None
    if not email or not validate_email(email):
        return None

    # Sanitize and return form data
    return {
        "name": sanitize_string(name),
        "email": sanitize_string(email),
        "industry": sanitize_string(form.get("industry", "")),
        "phone": sanitize_string(form.get("phone", "")),
        "product_service": sanitize_string(form.get("product_service", "")),
        "target_customers": sanitize_string(form.get("target_customers", "")),
        "pricing_model": sanitize_string(form.get("pricing_model", "")),
        "stage": sanitize_string(form.get("stage", "")),
        "team_size": sanitize_string(form.get("team_size", "")),
        "current_revenue": sanitize_string(form.get("current_revenue", "")),
        "country": sanitize_string(form.get("country", "")),
    }
