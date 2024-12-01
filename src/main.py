from flask import Flask, redirect, url_for  
from auth import auth_bp
from views import admin_bp, lecturer_bp  

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Đăng ký Blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(lecturer_bp, url_prefix='/lecturer')

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

if __name__ == '__main__':
    app.run(debug=True)
