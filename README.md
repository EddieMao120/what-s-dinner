# what-s-dinner
A small Django web application to help you decide what to cook for dinner based on your usual recipes and the ingredients you have on hand.

## Getting Started

### Prerequisites
- Python 3.10+ installed (the project uses a virtual environment).

### Setup
```powershell
# clone the repo
git clone <repo-url> .

# create & activate virtualenv (optional, project already provides one)
python -m venv .venv
.\.venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

### Running the development server
```powershell
cd code
python manage.py migrate
python manage.py createsuperuser  # optional, to access admin
python manage.py runserver
```
Then open http://127.0.0.1:8000/ in your browser.

### Application flow
1. Use the admin panel (`/admin/`) to add ingredients and recipes (with quantities and instructions).
2. Visit the home page (`/`) to check off the ingredients you have.
3. The app will list recipes you can prepare given the selected ingredients.

## Features
- Save and manage recipes with ingredients and step-by-step instructions.
- Select available ingredients and receive matching dish suggestions.
- Admin interface for easy data entry and maintenance.

## Development notes
The backend is built with Django using SQLite for simplicity. You can extend the models, add APIs or a frontend framework as desired.

## Contributing
Contributions welcome — open issues or PRs with clear descriptions.

## License
TBD
