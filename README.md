# Logisolutions

 
<img src="media/screenshots/LogiSolutions%20Homepage.PNG">


## Installation

Follow these steps to set up and run the LogiSolutions Django web app on your local machine:

1. **Clone the Repository:** 
   ```bash
   git clone https://github.com/Vladislav-Vasilev96/LogiSolutions.git
   
2. Change your working directory to the location where you've cloned the repository: 
   ```bash
   cd LogiSolutions
   
3. Create and Activate Virtual Environment:
   ```bash
    pip install virtualenv
    virtualenv venv
    venv\Scripts\activate      # On Windows
    source venv/bin/activate   # On macOS and Linux
   
4. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
   
5. Apply necessary database migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. Create a superuser account for admin access:
   ```bash
    python manage.py createsuperuser

7. Start the Django development server:
   ```bash
    python manage.py runserver
    
8. Open a web browser and go to http://127.0.0.1:8000/ to see the LogiSolutions web app.
