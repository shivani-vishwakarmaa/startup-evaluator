from services.validators import validate_form

# base valid form
base = {
    'name': 'Alice',
    'email': 'a@b.com',
    'industry': 'Other',
    'industry_other': '',
    'product_service': 'p',
    'problem_statement': 'prob',
    'target_customers': 't',
    'differentiation': 'd',
    'pricing_model': 'pr',
    'stage': 'Other',
    'stage_other': '',
    'team_size': 'Other',
    'team_size_other': '',
    'current_revenue': '0',
    'country': 'USA',
    'competitors': 'none',
    'validation': 'survey',
    'willingness_to_pay': 'Other',
    'willingness_to_pay_other': ''
}

print("Missing all customs ->", validate_form(base))
# provide custom values
for key, val in [('industry_other','CustomInd'), ('stage_other','Beta'), ('team_size_other','100+'), ('willingness_to_pay_other','Very High')]:
    base[key] = val

print("With custom values ->", validate_form(base))
