from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database.access import fetch_user_by_username

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Lấy thông tin người dùng từ cơ sở dữ liệu
        user = fetch_user_by_username(username)
        
        if user and user['Password'] == password:
            # Lưu thông tin người dùng vào session
            session['user'] = {'username': user['Username'], 'is_admin': user['IsAdmin'], 'ma_gv': user['MaGV']}
            
            # Kiểm tra xem người dùng có phải là admin hay không
            if user['IsAdmin']:
                flash(f"Xin chào {username}, bạn đã đăng nhập thành công với quyền Admin!", 'success')
                return redirect(url_for('admin.dashboard'))  # Chuyển hướng đến trang dashboard của admin
            else:
                flash('Đăng nhập thành công với quyền Giảng viên!', 'success')
                return redirect(url_for('lecturer.dashboard'))  # Chuyển hướng đến trang dashboard của giảng viên
        else:
            flash('Tên đăng nhập hoặc mật khẩu không đúng', 'danger')
    
    return render_template('auth/login.html')


# @auth_bp.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
        
#         # Thêm người dùng mới vào cơ sở dữ liệu
#         add_user(username, password)
        
#         flash('Đăng ký thành công! Vui lòng đăng nhập.', 'success')
#         return redirect(url_for('auth.login'))
    
#     return render_template('auth/register.html')

@auth_bp.route('/logout')
def logout():
    session.pop('user', None)  
    session.pop('customer_id', None)  
    flash('Bạn đã đăng xuất thành công!', 'success')
    return redirect(url_for('auth.login')) 

