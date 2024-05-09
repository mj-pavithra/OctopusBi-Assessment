Django Data Import and Visualization Project
This project is a Django application that imports data from CSV files and visualizes the data using charts. The data is imported into various database models representing schools, classes, assessment areas, students, answers, awards, and subjects. The data is then visualized using Django views and templates.

Table of Contents
Software Requirements
Project Setup
Running the Program
Data Import
Data Visualization
Troubleshooting
Software Requirements
Python 3.6 or later
Django 3.2 or later
SQLite (default database for Django projects)
Other Python packages: You may need additional Python packages such as uuid and csv to be installed.
You can install the required Python packages using the following command:

shell
 
pip install -r requirements.txt
Project Setup
Clone the repository: Clone the GitHub repository to your local machine.
shell
 
git clone https://github.com/your-repo/your-project.git
Navigate to the project directory: Change your current working directory to the cloned project directory.
shell
 
cd your-project
Create a virtual environment (optional but recommended): This will isolate your project's dependencies from the rest of your system.
shell
 
python3 -m venv venv
source venv/bin/activate
Install dependencies: Install the required dependencies using the provided requirements.txt file.
shell
 
pip install -r requirements.txt
Set up the database: Run Django migrations to set up the database.
shell
 
python manage.py migrate
Place the data files: Place the CSV data files in the data directory within your Django project's root directory.
Running the Program
To run the Django project, execute the following command from the project directory:

shell
python manage.py runserver
This will start the Django development server, and you can access the application at http://127.0.0.1:8000.

Data Import
To import data from CSV files, run the following command:

shell
 
python manage.py import_data
This command will import data from the CSV files located in the data directory and populate the Django models.

Data Visualization
The application visualizes the imported data using Django views and templates. You can access the data visualization by navigating to the /data_view/ URL on your local server (e.g., http://127.0.0.1:8000/data_view/).

Troubleshooting
If you encounter any issues during data import or visualization, here are a few troubleshooting steps:

Check CSV file format: Ensure the CSV files have the correct headers and data format.
Check data directory: Make sure the data files are located in the correct directory (data/).
Review console output: Check the console output for error messages and take appropriate actions.
Database integrity: Ensure that all models have valid relationships and data constraints are met.
