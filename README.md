# Game-Club

Game-Club is a computer club management tool for administrators.

## Features

- The administrator can turn on computers for a specified amount of time
- A list of computers is displayed, with available computers marked in green and occupied computers marked in red
- Two pages are available: `general`, which displays all computers in the general area, and `vip`, which displays all computers in the VIP area

## Installation

To clone the repository:

git clone git@github.com:NurzhigitAtashbaev/Game-Club.git

To set up the project, follow these steps:

1. Set up a virtual environment: `python3 -m venv venv`
2. Activate the virtual environment: `source venv/bin/activate`
3. Run database migrations: `python manage.py makemigrations` and `python manage.py migrate`
4. Run the development server: `python manage.py runserver`

## Usage

To use the application, open your web browser and go to the URL specified in the terminal (e.g. `http://127.0.0.1:8000/`). You will be able to access the computer lists on the `general` and `vip` pages.
