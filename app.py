from flask import Flask, render_template, request, redirect, session, url_for
import csv, os
from dotenv import load_dotenv
import gspread
from google.oauth2.service_account import Credentials

load_dotenv()

app = Flask(__name__)
app.secret_key = 'some_random_secret_key'

USERNAME = os.getenv("ADMIN_USERNAME", "admin")
PASSWORD = os.getenv("ADMIN_PASSWORD", "adminpass")

#CSV_FILE = "reports.csv"

scope = ["https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive"]
creds = Credentials.from_service_account_file("creds.json", scopes=scope)
client = gspread.authorize(creds)

sheet = client.open_by_key("1YFsDn--_6z9DU5Nz6W7-XZldR0GAQT1cKB4-dOFLuKI")
worksheet = sheet.sheet1  

def save_report_to_gsheet(name, issue):
    worksheet.append_row([name, issue])


@app.route('/')
def home():
    return redirect('/report')

@app.route('/report', methods=['GET', 'POST'])
def report():
    if request.method == 'POST':
        name = request.form['name']
        issue = request.form['issue']
        
        save_report_to_gsheet(name or "Anonymous", issue)
        
        return render_template('thanks.html')
    return render_template('form.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']
        if user == USERNAME and pwd == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('admin'))
        error = "Invalid credentials"
    return render_template('login.html', error=error)

@app.route('/admin')
def admin():
    if not session.get('logged_in'):
        return redirect('/login')

    try:
        
        data = worksheet.get_all_values()

        if not data or len(data) == 1:
            return "<h3>No reports submitted yet.</h3>"

        
        reports = data[1:]

        reports = [row if len(row) == 2 else ["", ""] for row in reports]

        return render_template('admin.html', reports=reports)

    except Exception as e:
        return f"<h3>Error loading admin page:</h3><pre>{str(e)}</pre>"

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect('/login')

if __name__ == '__main__':
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Issue"])
    app.run(debug=True)
