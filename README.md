# StartupSignal

A web application that collects and evaluates startup information through a user-friendly form, integrating with Make.com for automated data processing.

## Overview

The StartupSignal is a Flask-based web application designed to gather comprehensive information about startups and route it to Make.com for processing and evaluation. The application features a multi-step evaluation process with robust form validation and error handling.

## Features

- **Welcome Page**: Introduction to the evaluation process
- **Comprehensive Form**: Collects detailed startup information including:
  - Basic details (name and email)
  - Business information (industry with "Other" option that reveals a custom text field, product/service, problem statement, target customers, differentiation)
  - Financial data (pricing model, current revenue)
  - Stage and team size (each with "Other" alternatives)
  - Customer insights (validation evidence)
- **Form Validation**: Server-side validation for data integrity (phone, country, competitors, willingness-to-pay fields removed)
- **Make.com Integration**: Automated webhook submission to Make.com for processing
- **Thank You Page**: Confirmation page with submitted data summary
- **Error Handling**: Dedicated error pages for validation and submission failures

## Project Structure

```
startup-evaluator/
├── app.py                     # Flask application & routes
├── README.md                  # Project documentation
├── services/
│   ├── make_service.py        # Make.com webhook integration
│   └── validators.py          # Service-level validators
├── templates/                 # HTML templates
│   ├── base.html              # Base template
│   ├── welcome.html           # Welcome/intro page
│   ├── index.html             # Startup evaluation form
│   ├── thankyou.html          # Thank you page
│   └── error.html             # Error page
└── static/
    └── style.css              # Stylesheet
```

## Architecture (MVC Pattern)

The application follows the **Model-View-Controller** pattern:

- **View (V)**: HTML templates in `templates/` + CSS in `static/` - what users see and interact with
- **Controller (C)**: Flask routes in `app.py` - handle HTTP requests, coordinate between View and Model
- **Model (M)**: Business logic in `services/validators.py` and `services/make_service.py` - data processing and Make.com integration

### Request Flow

```
User fills form (View)
        ↓
POST /submit (Controller)
        ↓
Validate form data (Model)
        ↓
Send to Make.com webhook (Model)
        ↓
Redirect with session data (Controller)
        ↓
Display thank you page (View)
```

## Installation

### Prerequisites

- Python 3.8+
- Flask
- python-dotenv
- Requests library

### Setup

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp .env.example .env
   ```

4. Edit `.env` and fill in your values:
   ```
   SECRET_KEY=your_secret_key_here
   MAKE_WEBHOOK_URL=your_make_webhook_url
   MAKE_API_KEY=your_make_api_key
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open your browser and navigate to `http://localhost:5000`

## Routes

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Welcome page |
| `/form` | GET | Startup evaluation form |
| `/submit` | POST | Process form submission |
| `/thankyou` | GET | Thank you page with submitted data |
| `/error` | GET | Error page for failed submissions |

## Form Validation

The application validates the following required fields:

- **Name**: Minimum 2 characters
- **Email**: Must contain "@" symbol
- **Optional fields**: Industry, product/service, target customers, pricing model, stage, team size, revenue

Validation occurs at two levels:
1. **Client-side** (HTML5 attributes)
2. **Server-side** (Python validators in `validators.py`)

## Environment Variables

Create a `.env` file with the following:

```
SECRET_KEY=your_flask_secret_key
MAKE_WEBHOOK_URL=https://hook.make.com/...
MAKE_API_KEY=your_make_api_key
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3
- **Integration**: Make.com Webhooks
- **Configuration**: python-dotenv for environment management

## Error Handling

- **Form Validation Error**: Redirects to `/error` if form validation fails
- **Make.com Integration Error**: Redirects to `/error` if webhook submission fails
- **Logging**: All errors and warnings are logged for debugging

## Session Management

The application uses Flask sessions to store form data temporarily, allowing the thank you page to display submitted information without additional data processing.

## Development

To modify the application:

1. **Add form fields**: Update HTML in `templates/index.html` and validation in `validators.py`
2. **Modify Make.com integration**: Edit `services/make_service.py`
3. **Change styling**: Update `static/style.css`
4. **Add routes**: Extend `app.py` with new Flask routes

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues or questions, please contact the development team.

