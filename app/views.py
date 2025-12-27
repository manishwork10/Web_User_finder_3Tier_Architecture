from flask import render_template, request, redirect, url_for
from app import app
import app.db.user_db as users_db

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/search')
def search():
    raw = request.args.get('q', '')
    print('RAW QUERY:', repr(raw))
    username = request.args.get('q', '').strip()
    phone    = users_db.find_user_phone(username)
    if phone is None:
        result = 'User not found'
    else:
        result = f'Phone: {phone}'
    return render_template('homepage.html', result=result)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/users', methods=['POST'])
def users():
    users_db.register_user(request.form)
    return redirect(url_for('home'))