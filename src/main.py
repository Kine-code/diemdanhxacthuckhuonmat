from flask import Flask, redirect, url_for ,request ,jsonify
from auth import auth_bp
from views import admin_bp, lecturer_bp  
from flask import Flask
import os
import base64
from werkzeug.utils import secure_filename
from database.access import save_attendance_record
from PIL import Image
import io

app = Flask(__name__)

app.secret_key = 'your_secret_key'

# Đăng ký Blueprint
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(lecturer_bp, url_prefix='/lecturer')
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

@app.route('/')
def home():
    return redirect(url_for('auth.login'))

UPLOAD_FOLDER = './static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Kiểm tra định dạng tệp ảnh hợp lệ
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload_image', methods=['POST'])
def upload_image():
    # Lấy dữ liệu ảnh từ Base64
    image_data = request.form['captured_image']
    
    # Tách phần dữ liệu Base64 sau "data:image/png;base64,"
    image_data = image_data.split(",")[1]
    
    # Giải mã Base64
    image = base64.b64decode(image_data)
    
    # Mở ảnh từ dữ liệu giải mã Base64
    img = Image.open(io.BytesIO(image))
    img = img.resize((int(img.width * 0.5), int(img.height * 0.5)))
    
    # Tạo tên file ngẫu nhiên cho ảnh
    filename = secure_filename("captured_image.png")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    
    # Kiểm tra xem thư mục có tồn tại không, nếu không thì tạo mới
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    
    # Lưu ảnh vào thư mục static/images
    with open(filepath, 'wb') as f:
        f.write(image)
    
    # Lấy mã sinh viên từ form (hoặc có thể là từ request)
    student_id = request.form['student_id']
    
    # Lưu tên ảnh vào cơ sở dữ liệu
    save_attendance_record(student_id, f"/static/images/{filename}")
    
    # Trả lại URL của ảnh để hiển thị
    return jsonify({"image_url": f"/static/images/{filename}"})


if __name__ == '__main__':
    app.run(debug=True)
