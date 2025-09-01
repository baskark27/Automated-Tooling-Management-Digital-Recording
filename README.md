This project is a Flask-based web application designed to streamline tool management and daily recording in workshops and labs.
It helps track tools in real time, automate tool status updates, and generate daily reports that are emailed automatically to the concerned authority.
The system replaces manual registers and spreadsheets with a digital, error-free solution that improves accountability and efficiency.



Key Features :

Tool check-in/check-out with user details

Real-time tool status updates (In/Out)

Automatic reset for tools marked "Out" for more than 24 hours

Daily activity report generation and email notifications

Simple and user-friendly dashboard (Bootstrap UI)



Tech Stack :

Backend: Python (Flask)

Frontend: HTML, CSS (Bootstrap), JavaScript

Database: SQLite

Other: SMTP (for automated email notifications)



Project Structure
Automated-Tooling-Management-Digital-Recording/
 ┣ templates/        -> HTML files (index.html)  
 ┣ app.py            -> Main Flask app  
 ┣ tools.db          -> SQLite database file  
 ┣ requirements.txt  -> Dependencies  
 ┣ README.md         -> Documentation  



Installation & Setup

Clone the repository

git clone https://github.com/yourusername/Automated-Tooling-Management-Digital-Recording.git
cd Automated-Tooling-Management-Digital-Recording


Install dependencies : pip install -r requirements.txt


Run the Flask app : python app.py


Open in browser : http://127.0.0.1:5001




Contact :

Developed by: Baskar K

LinkedIn: www.linkedin.com/in/baskark7
