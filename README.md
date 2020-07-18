# django-expentrac

Objective: 
Projext expentrac allows a user to login and track her expenses in no particular order for record keeping. 

Features included:
  1) Login and logout(authentication)
  2) Creation of expense records
  3) Updating expense records
  4) Deleting expense records
  5) Filtering by month of expense
  6) Filtering by category of expense
  7) A total expense calculator after each expense line, which cumulates the expense values of all expenses
  
 Some of the system used for this are:
  1) Django authentication system with error handling for forms
  2) PyPi project for django bootstrap modal forms: https://pypi.org/project/django-bootstrap-modal-forms/
  3) Bootstrap for table styling and modal
  4) Standard date-picker for forms

Things to implement for the future:
  1) Filter fixes when both month and category filters are applied
  2) Pagination of results 
  3) Total calculation to match the currently-shown expense results (for this, filtering must occur on the server)
  4) Column sorting 
  5) Filter months to be in order 
  6) Ability to add custom category 
  
To run the project: 
  1) Start a virtual environment (venv) after cloning the repo 
  2) Do a 'pip install' to install the dependencies of the requirements.txt
  3) Once that is done, run project using 'python manage.py runserver'
  4) Default port is 3000. See the project running on http://localhost:3000.
  
  
