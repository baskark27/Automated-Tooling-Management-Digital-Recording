Automated Tooling Management and Digital Daily Recording System
Overview

A Flask-based web application to digitize tool check-in/check-out and daily recording in workshops.
Tracks tools in real time, updates their status automatically, and sends daily usage reports via email.

Features

Tool check-in/check-out with user details

Real-time status logging with timestamps

Auto-reset for tools left “Out” over 24 hours

Daily report generation and email notifications

Tech Stack

Python (Flask)

HTML, CSS (Bootstrap), JavaScript

SQLite

SMTP (Email)

Installation & Setup
git clone https://github.com/yourusername/Automated-Tooling-Management-Digital-Recording.git
cd Automated-Tooling-Management-Digital-Recording
pip install -r requirements.txt
python app.py


App will run at:

http://127.0.0.1:5001

Project Structure
├─ app.py          # Flask backend  
├─ tools.db        # SQLite database  
├─ templates/      # HTML (UI files)  
└─ requirements.txt


Contact

Developed by: Baskar K
LinkedIn: www.linkedin.com/in/baskark7
