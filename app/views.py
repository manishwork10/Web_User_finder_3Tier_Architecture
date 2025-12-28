# -------------  P R E S E N T A T I O N   T I E R  -------------
from flask import render_template, request, redirect, url_for
from app import app
import app.db.user_db as service   # business tier

@app.route('/')
def home():
    """Display the search form."""
    return render_template('homepage.html')

@app.route('/search')
def search():
    """Ask business tier for phone number."""
    username = request.args.get('q', '').strip()
    phone    = service.find_user_phone(username)
    result   = f'Phone: {phone}' if phone else 'User not found'
    return render_template('homepage.html', result=result)

@app.route('/register')
def register():
    """Show empty registration form."""
    return render_template('register.html')

@app.route('/users', methods=['POST'])
def users():
    """Delegate user creation to business tier."""
    service.register_user(request.form)
    return redirect(url_for('home'))