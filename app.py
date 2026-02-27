from flask import Flask, render_template, redirect, url_for, session
from dotenv import load_dotenv
import os

load_dotenv('.env')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return redirect(url_for('signin'))

@app.route('/register')
def register():
    return render_template('authentication.html')

@app.route('/signin')
def signin():
    return render_template('authentication.html')

@app.route('/signout')
def signout():
    pass

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/dashboard/invitation', methods=['POST'])
def invite_contact():
    pass

@app.route('/dashboard/save/settings', methods=['POST'])
def save_settings():
    pass

@app.route('/dashboard/save/medication', methods=['POST'])
def save_medication():
    pass

@app.route('/dashboard/save/contact', methods=['POST'])
def save_contact():
    pass

@app.route('/dashboard/set-reminder', methods=['POST'])
def set_reminder():
    pass

@app.route('/dashboard/generate/pdf', methods=['POST'])
def pdf_generator():
    pass

@app.route('/tasks/email')
def send_email():
    pass

@app.route('/api/users')
def users():
    pass

@app.route('/api/auth/login')
def auth_login():
    pass

@app.route('/api/settings')
def settings():
    pass

@app.route('/api/medications')
def medications():
    pass

@app.route('/api/reminders')
def reminders():
    pass

@app.route('/api/history')
def history():
    pass

@app.route('/api/contacts')
def contacts():
    pass

@app.route('/api/invite/contact')
def api_invite_contact():
    pass



if __name__ == '__main__':
    app.run(port=5666, debug=True)
