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

    # determine industry selection, allow custom value when "Other" chosen
    industry = form.get("industry", "").strip()
    if industry == "Other":
        industry_other = form.get("industry_other", "").strip()
        if not industry_other:
            return None
        industry = industry_other

    # determine stage selection
    stage = form.get("stage", "").strip()
    if stage == "Other":
        stage_other = form.get("stage_other", "").strip()
        if not stage_other:
            return None
        stage = stage_other

    # determine team size selection
    team_size = form.get("team_size", "").strip()
    if team_size == "Other":
        team_size_other = form.get("team_size_other", "").strip()
        if not team_size_other:
            return None
        team_size = team_size_other

    # determine willingness to pay selection
    willingness = form.get("willingness_to_pay", "").strip()
    if willingness == "Other":
        willingness_other = form.get("willingness_to_pay_other", "").strip()
        if not willingness_other:
            return None
        willingness = willingness_other

    # Sanitize and return form data
    return {
        "name": sanitize_string(name),
        "email": sanitize_string(email),
        "industry": sanitize_string(industry),
        "phone": sanitize_string(form.get("phone", "")),
        "product_service": sanitize_string(form.get("product_service", "")),
        "problem_statement": sanitize_string(form.get("problem_statement", "")),
        "target_customers": sanitize_string(form.get("target_customers", "")),
        "differentiation": sanitize_string(form.get("differentiation", "")),
        "pricing_model": sanitize_string(form.get("pricing_model", "")),
        "stage": sanitize_string(stage),
        "team_size": sanitize_string(team_size),
        "current_revenue": sanitize_string(form.get("current_revenue", "")),
        "country": sanitize_string(form.get("country", "")),
        "competitors": sanitize_string(form.get("competitors", "")),
        "validation": sanitize_string(form.get("validation", "")),
        "willingness_to_pay": sanitize_string(willingness),
    }
