from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

def send_notification(subject, message_body, email_to):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = '@gmail.com'  # Replace with your Gmail
    msg['To'] = email_to
    text = message_body
    html = f"""
    <html>
    <body>
        <h2 style="color: #007BFF;">Automated Tooling Management and Digital Daily Recording System</h2>
        <p>{message_body.replace('\n', '<br>')}</p>
        <p>Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
    </body>
    </html>
    """
    msg.attach(MIMEText(text, 'plain'))
    msg.attach(MIMEText(html, 'html'))
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('@gmail.com', '')  # Replace with 16-character app password
            server.sendmail('@gmail.com', email_to, msg.as_string())
    except Exception as e:
        print(f"Email failed: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tools', methods=['GET', 'POST', 'PUT'])
def tools():
    try:
        conn = sqlite3.connect('tools.db')
        c = conn.cursor()
        # Create table if it doesn't exist
        c.execute('CREATE TABLE IF NOT EXISTS tools (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, status TEXT, user TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
        
        if request.method == 'POST':
            data = request.json
            if not all(key in data for key in ['name', 'status', 'user']):
                return jsonify({'error': 'Missing required fields (name, status, user)'}), 400
            c.execute('INSERT INTO tools (name, status, user) VALUES (?, ?, ?)',
                      (data['name'], data['status'], data['user']))
            conn.commit()
            # Digital Daily Recording: Generate summary after each addition
            c.execute('SELECT * FROM tools WHERE DATE(timestamp) = DATE("now")')
            rows = c.fetchall()
            message_body = "Daily Tooling Summary:\n\n" + \
                           ( "".join(f"Tool: {row[1]}, Status: {row[2]}, User: {row[3]}, Time: {row[4]}\n" for row in rows) if rows else "No tools logged today." ) + \
                           f"\nTotal tools logged today: {len(rows)}"
            send_notification('Tooling Update', message_body, '@gmail.com') # Replace with receive email
        
        elif request.method == 'PUT':
            data = request.json
            if not all(key in data for key in ['id', 'status']):
                return jsonify({'error': 'Missing required fields (id, status)'}), 400
            c.execute('UPDATE tools SET status = ?, timestamp = CURRENT_TIMESTAMP WHERE id = ?',
                      (data['status'], data['id']))
            conn.commit()
            # Automated Tooling Management: Auto-update "Out" >24 hours to "In"
            c.execute('SELECT id, timestamp FROM tools WHERE status = "Out"')
            for row in c.fetchall():
                if datetime.now() - datetime.fromisoformat(row[1]) > timedelta(hours=24):
                    c.execute('UPDATE tools SET status = "In", timestamp = CURRENT_TIMESTAMP WHERE id = ?', (row[0],))
            conn.commit()
        
        rows = c.execute('SELECT * FROM tools ORDER BY timestamp DESC').fetchall()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/daily-report', methods=['POST'])
def daily_report():
    try:
        conn = sqlite3.connect('tools.db')
        c = conn.cursor()
        c.execute('SELECT * FROM tools WHERE DATE(timestamp) = DATE("now")')
        rows = c.fetchall()
        conn.close()
        message_body = "Daily Recording Summary:\n\n" + \
                       ( "".join(f"Tool: {row[1]}, Status: {row[2]}, User: {row[3]}, Time: {row[4]}\n" for row in rows) if rows else "No tools logged today." ) + \
                       f"\nTotal tools logged today: {len(rows)}"
        send_notification('TANSCST Daily Report', message_body, '@gmail.com')  # Replace with receive email
        return jsonify({'status': 'success', 'summary': message_body})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':

    app.run(debug=True, port=5001)
