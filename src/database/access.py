from database.connect import get_db_connection
import base64
from datetime import datetime
import face_recognition
# login
def fetch_user_by_username(username):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT MaGV, Username, Password, Ho, Ten, isAdmin FROM GiangVien WHERE Username = ?", (username,))
    user = cursor.fetchone()
    if user:
        return {
            'MaGV': user[0],
            'Username': user[1],  
            'Password': user[2],
            'Ho': user[3],
            'Ten': user[4],
            'IsAdmin': user[5],
        }
    return None

# Truy vấn danh sách sinh viên
def fetch_all_students():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT MaSV, Lop, Ho, Ten, MaKhoa, MaLop, TenLop, MaDD FROM SinhVien"
    cursor.execute(query)
    students = cursor.fetchall()
    cursor.close()
    conn.close()
    return students

# Thêm sinh viên
def add_student(ma_sv, ho, ten, lop, ma_khoa, ma_lop, ten_lop, ma_dd):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO SinhVien (MaSV, Ho, Ten, Lop, MaKhoa, MaLop, TenLop, MaDD) 
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(query, (ma_sv, ho, ten, lop, ma_khoa, ma_lop, ten_lop, ma_dd))
    conn.commit()
    cursor.close()
    conn.close()

# Lấy thông tin sinh viên theo ID
def fetch_student_by_id(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM SinhVien WHERE MaSV = ?"
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    cursor.close()
    conn.close()
    return student

# Cập nhật thông tin sinh viên
def update_student(student_id, ho, ten, lop, ma_khoa, ma_lop, ten_lop, ma_dd):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """UPDATE SinhVien SET Ho = ?, Ten = ?, Lop = ?, MaKhoa = ?, MaLop = ?, TenLop = ?, MaDD = ? 
               WHERE MaSV = ?"""
    cursor.execute(query, (ho, ten, lop, ma_khoa, ma_lop, ten_lop, ma_dd, student_id))
    conn.commit()
    cursor.close()
    conn.close()

# Xóa sinh viên theo ID
def delete_student(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM SinhVien WHERE MaSV = ?"
    cursor.execute(query, (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Thêm môn học
def add_subject(ma_mon, ten_mon, so_tc, ngay_bd):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO MonHoc (MaMH, TenMH, SoTC, NgayBD) 
               VALUES (?, ?, ?, ?)"""
    cursor.execute(query, (ma_mon, ten_mon, so_tc, ngay_bd))
    conn.commit()
    cursor.close()
    conn.close()

# Lấy danh sách tất cả môn học
def fetch_all_subjects():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT MaMH, TenMH, SoTC, NgayBD FROM MonHoc"
    cursor.execute(query)
    subjects = cursor.fetchall()
    cursor.close()
    conn.close()
    return subjects

# Lấy thông tin môn học theo ID
def fetch_subject_by_id(subject_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM MonHoc WHERE MaMH = ?"
    cursor.execute(query, (subject_id,))
    subject = cursor.fetchone()
    cursor.close()
    conn.close()
    return subject

# Cập nhật thông tin môn học
def update_subject(subject_id, ten_mon, so_tc, ngay_bd):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """UPDATE MonHoc SET TenMH = ?, SoTC = ?, NgayBD = ? 
               WHERE MaMH = ?"""
    cursor.execute(query, (ten_mon, so_tc, ngay_bd, subject_id))
    conn.commit()
    cursor.close()
    conn.close()

# Xóa môn học theo ID
def delete_subject(subject_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM MonHoc WHERE MaMH = ?"
    cursor.execute(query, (subject_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Thêm khoa
def add_khoa(ma_khoa, ten_khoa):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO Khoa (maKhoa, TenKhoa) 
               VALUES (?, ?)"""
    cursor.execute(query, (ma_khoa, ten_khoa))
    conn.commit()
    cursor.close()
    conn.close()

# Lấy danh sách tất cả khoa
def fetch_all_khoas():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT maKhoa, TenKhoa FROM Khoa"
    cursor.execute(query)
    khoas = cursor.fetchall()
    cursor.close()
    conn.close()
    return khoas

# Lấy thông tin khoa theo ID
def fetch_khoa_by_id(khoa_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Khoa WHERE maKhoa = ?"
    cursor.execute(query, (khoa_id,))
    khoa = cursor.fetchone()
    cursor.close()
    conn.close()
    return khoa

# Cập nhật thông tin khoa
def update_khoa(khoa_id, ten_khoa):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """UPDATE Khoa SET TenKhoa = ? 
               WHERE maKhoa = ?"""
    cursor.execute(query, (ten_khoa, khoa_id))
    conn.commit()
    cursor.close()
    conn.close()

# Xóa khoa theo ID
def delete_khoa(khoa_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM Khoa WHERE maKhoa = ?"
    cursor.execute(query, (khoa_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Thêm giảng viên
def add_giang_vien(ma_gv, username, password, ho, ten, is_admin):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """INSERT INTO GiangVien (MaGV, Username, Password, Ho, Ten, isAdmin) 
               VALUES (?, ?, ?, ?, ?, ?)"""
    cursor.execute(query, (ma_gv, username, password, ho, ten, is_admin))
    conn.commit()
    cursor.close()
    conn.close()

# Lấy danh sách tất cả giảng viên
def fetch_all_giang_viens():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT MaGV, Username, Ho, Ten, isAdmin FROM GiangVien"
    cursor.execute(query)
    giangviens = cursor.fetchall()
    cursor.close()
    conn.close()
    return giangviens

# Lấy giảng viên theo mã
def fetch_giang_vien_by_id(ma_gv):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM GiangVien WHERE MaGV = ?"
    cursor.execute(query, (ma_gv,))
    giangvien = cursor.fetchone()
    cursor.close()
    conn.close()
    return giangvien

# Cập nhật thông tin giảng viên
def update_giang_vien(ma_gv, username, password, ho, ten, is_admin):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """UPDATE GiangVien 
               SET Username = ?, Password = ?, Ho = ?, Ten = ?, isAdmin = ? 
               WHERE MaGV = ?"""
    cursor.execute(query, (username, password, ho, ten, is_admin, ma_gv))
    conn.commit()
    cursor.close()
    conn.close()

# Xóa giảng viên
def delete_giang_vien(ma_gv):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "DELETE FROM GiangVien WHERE MaGV = ?"
    cursor.execute(query, (ma_gv,))
    conn.commit()
    cursor.close()
    conn.close()

# Lấy danh sách sinh viên
def get_student_by_face(face_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
        SELECT MaSV, Ho, Ten, Lop, TenLop, maKhoa 
        FROM SinhVien 
        WHERE MaSV = ?
    """
    cursor.execute(query, (face_id,))
    student = cursor.fetchone()
    conn.close()
    return student

def add_attendance(ma_sv, ma_khoa, ma_monhoc, trang_thai, hinh_anh):
    conn = get_db_connection()
    cursor = conn.cursor()

    # Lưu thông tin vào bảng DiemDanhSinhVien
    query = """
        INSERT INTO DiemDanhSinhVien (MaSV, MaKhoa, MaMonHoc, TrangThai, ThoiGianDiemDanh, HinhAnhDiemDanh)
        VALUES (?, ?, ?, ?, GETDATE(), ?)
    """
    cursor.execute(query, (ma_sv, ma_khoa, ma_monhoc, trang_thai, hinh_anh))
    conn.commit()
    conn.close()

# Ghi điểm danh sinh viên
def record_attendance(ma_sv, ma_mh, ngay, trang_thai):
    query = """
    INSERT INTO DiemDanh (MaSV, MaMH, NgayDiemDanh, TrangThai)
    VALUES (:ma_sv, :ma_mh, :ngay, :trang_thai)
    """
    get_db_connection().execute(query, {"ma_sv": ma_sv, "ma_mh": ma_mh, "ngay": ngay, "trang_thai": trang_thai})
    get_db_connection().commit()
    return True

def save_attendance_record(student_id, image_url):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = '''INSERT INTO DiemDanhSinhVien (MaSV, HinhAnhDiemDanh) VALUES (?, ?)'''
    cursor.execute(query, (student_id, image_url))
    conn.commit()
    cursor.close()
    conn.close()

    
# Hàm lưu ảnh điểm danh và trả về đường dẫn
def save_attendance_image(photo, student_id):
    try:
        image_data = base64.b64decode(photo.split(',')[1])
        file_name = f"{student_id}_{datetime.now().strftime('%Y%m%d%H%M%S')}.jpg"
        image_path = f"static/images/attendance/{file_name}"
        with open(image_path, "wb") as f:
            f.write(image_data)

        return image_path
    except Exception as e:
        print(f"Error saving image: {e}")
    return None


# Hàm điểm danh sinh viên
def mark_attendance(student_id, attendance_id, photo):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            image_path = save_attendance_image(photo, student_id)
            timestamp = datetime.now()
            status = 'Có mặt'  # Default status
            query = """
            INSERT INTO DiemDanhSinhVien (MaDD, MaSV, TrangThai, ThoiGianDiemDanh, HinhAnhDiemDanh)
            VALUES (?, ?, ?, ?, ?)
            """
            cursor.execute(query, (attendance_id, student_id, status, timestamp, image_path))
            conn.commit()
    except Exception as e:
        print(f"Error marking attendance: {e}")
    finally:
        conn.close()

# Hàm lấy thông tin điểm danh của sinh viên
def get_attendance(student_id, attendance_id):
    """
    Lấy thông tin điểm danh của sinh viên từ bảng DiemDanhSinhVien
    :param student_id: Mã sinh viên
    :param attendance_id: Mã điểm danh
    :return: Thông tin điểm danh
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Truy vấn thông tin điểm danh
    query = "SELECT * FROM DiemDanhSinhVien WHERE MaSV = ? AND MaDD = ?"
    cursor.execute(query, (student_id, attendance_id))
    result = cursor.fetchone()

    conn.close()

    if result:
        return {
            "MaDD": result[1],
            "MaSV": result[2],
            "TrangThai": result[3],
            "ThoiGianDiemDanh": result[4],
            "HinhAnhDiemDanh": result[5]
        }
    return None


# Tìm sinh viên bằng nhận diện khuôn mặt
def find_student_by_face(face_encoding):
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            query = "SELECT Images.MaSV, SinhVien.Ho, SinhVien.Ten, Images.LinkIMG FROM Images JOIN SinhVien ON Images.MaSV = SinhVien.MaSV"
            cursor.execute(query)
            students = cursor.fetchall()

            for student in students:
                face_image = face_recognition.load_image_file(student[3])
                known_encoding = face_recognition.face_encodings(face_image)[0]

                matches = face_recognition.compare_faces([known_encoding], face_encoding)
                if True in matches:
                    return {
                        'MaSV': student[0],
                        'Ho': student[1],
                        'Ten': student[2]
                    }
    except Exception as e:
        print(f"Error finding student by face: {e}")
    finally:
        conn.close()
    return None

# Lấy thông tin chi tiết sinh viên từ Mã SV
def get_student_info(student_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    query = """SELECT MaSV, Ho, Ten, Lop, MaKhoa, MaLop, TenLop, MaDD
               FROM SinhVien WHERE MaSV = ?"""
    cursor.execute(query, (student_id,))
    student = cursor.fetchone()
    
    cursor.close()
    conn.close()
    
    if student:
        return {
            'MaSV': student[0],
            'Ho': student[1],
            'Ten': student[2],
            'Lop': student[3],
            'MaKhoa': student[4],
            'MaLop': student[5],
            'TenLop': student[6],
            'MaDD': student[7]
        }
    return None

# Lấy số lượng sinh viên
def get_student_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM SinhVien"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    conn.close()
    print(f"Student Count: {count}")  # In ra kết quả
    return count

# Lấy số lượng giảng viên
def get_teacher_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM GiangVien"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    conn.close()
    return count

# Lấy số lượng môn học
def get_subject_count():
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT COUNT(*) FROM MonHoc"
    cursor.execute(query)
    count = cursor.fetchone()[0]
    conn.close()
    return count

def save_to_database(student_id, student_name, image_path):

    conn = get_db_connection()
    cursor = conn.cursor()

    # Lệnh INSERT dữ liệu
    cursor.execute("""
        INSERT INTO DiemDanhSinhVien (MaDD, MaSV, TrangThai, ThoiGianDiemDanh, HinhAnhDiemDanh)
        VALUES (?, ?, ?, ?, ?)
    """, ('DD001', student_id, 'Đã điểm danh', datetime.now(), image_path))

    conn.commit()
    cursor.close()
    conn.close()
    print("Lưu dữ liệu vào database thành công!")

# Hàm lưu ảnh khuôn mặt vào cơ sở dữ liệu
def save_student_and_image(ma_sv, ho, ten, lop, ma_khoa, image_data):
    # Lưu ảnh vào thư mục (nếu muốn lưu dưới dạng tệp)
    image_data = image_data.split(',')[1]  # Lấy phần ảnh từ Base64
    image_data = base64.b64decode(image_data)
    
    # Lưu ảnh vào tệp (có thể lưu vào thư mục Images)
    image_filename = f"{ma_sv}_face.png"
    with open(os.path.join('static/images', image_filename), 'wb') as f:
        f.write(image_data)
    
    # Kết nối tới cơ sở dữ liệu và lưu thông tin sinh viên và ảnh
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Lưu thông tin sinh viên
    cursor.execute('''
        INSERT INTO SinhVien (MaSV, Ho, Ten, Lop, maKhoa)
        VALUES (?, ?, ?, ?, ?)
    ''', (ma_sv, ho, ten, lop, ma_khoa))

    # Lưu ảnh khuôn mặt
    cursor.execute('''
        INSERT INTO Images (LinkIMG, MaSV)
        VALUES (?, ?)
    ''', (f'static/images/{image_filename}', ma_sv))
    
    conn.commit()
    conn.close()
# # Lấy thống kê điểm danh
# def get_attendance_statistics():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     query = """SELECT MaSV, COUNT(CASE WHEN TrangThai = 'Có mặt' THEN 1 END) AS present_count,
#                       COUNT(CASE WHEN TrangThai = 'Vắng mặt' THEN 1 END) AS absent_count
#                FROM DiemDanh
#                GROUP BY MaSV"""
#     cursor.execute(query)
#     statistics = cursor.fetchall()
#     conn.close()
#     return statistics