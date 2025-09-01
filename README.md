# Automated Tooling Management and Digital Daily Recording System

## Overview
This project is a Flask-based web application that digitizes the process of tool management in workshops and labs.  
It allows users to check tools in and out, automatically logs activity with timestamps, and generates daily usage reports that are emailed to the concerned authority.  
The system reduces manual errors, improves accountability, and saves time compared to traditional registers or spreadsheets.  

## Features
- Tool check-in/check-out with user details  
- Real-time status logging with timestamps  
- Automatic reset for tools marked "Out" for over 24 hours  
- Daily report generation and automated email notifications  
- Simple, user-friendly dashboard (Bootstrap UI)  

## Tech Stack
- **Backend:** Python (Flask)  
- **Frontend:** HTML, CSS (Bootstrap), JavaScript  
- **Database:** SQLite  
- **Other:** SMTP (for email notifications)  

## Installation & Setup
1. Clone the repository:  
   ```bash
   git clone https://github.com/yourusername/Automated-Tooling-Management-Digital-Recording.git
   cd Automated-Tooling-Management-Digital-Recording
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:  
   ```bash
   python app.py
   ```

4. Open in your browser:  
   ```
   http://127.0.0.1:5001
   ```

## Project Structure
```
Automated-Tooling-Management-Digital-Recording/
├── app.py            # Flask backend
├── tools.db          # SQLite database
├── templates/        # HTML (UI files)
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

## Contact
Developed by: **Baskar K**  
LinkedIn: [https://www.linkedin.com/in/baskark7](https://www.linkedin.com/in/baskark7)
