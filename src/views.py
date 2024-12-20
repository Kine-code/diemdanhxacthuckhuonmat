from flask import Blueprint,  render_template, request, redirect, url_for, flash,jsonify
from database.access import add_student,fetch_all_students, fetch_student_by_id, update_student,delete_student,fetch_all_subjects,fetch_subject_by_id,update_subject,delete_subject,add_subject,delete_khoa,fetch_all_khoas,fetch_khoa_by_id,update_khoa,add_khoa,delete_giang_vien,fetch_all_giang_viens,fetch_giang_vien_by_id,update_giang_vien,add_giang_vien,get_student_count, get_teacher_count,get_subject_count, mark_attendance
import cv2
import base64
from datetime import datetime
# Định nghĩa blueprint cho Admin và Giảng viên
admin_bp = Blueprint('admin', __name__)
lecturer_bp = Blueprint('lecturer', __name__)


# Admin Routes
@admin_bp.route('/dashboard')
def dashboard():
    student_count = get_student_count()
    teacher_count = get_teacher_count()
    subject_count = get_subject_count()

    # Truyền số liệu vào template
    return render_template('admin/dashboard.html', 
                           student_count=student_count, 
                           teacher_count=teacher_count, 
                           subject_count=subject_count)

@admin_bp.route('/admin/student_list')
def student_list():
    students = fetch_all_students()  # Giả sử fetch_all_students() trả về danh sách sinh viên
    return render_template('admin/students/student_list.html', students=students)

@admin_bp.route('/admin/add_sinhvien', methods=['GET', 'POST'])
def add_student_view():
    khoa_list = fetch_all_khoas()  # Fetch danh sách Khoa
    monhoc_list = fetch_all_subjects()  # Fetch danh sách Môn học
    
    if request.method == 'POST':
        ma_sv = request.form['ma_sv']
        ho = request.form['ho']
        ten = request.form['ten']
        lop = request.form['lop']
        ma_khoa = request.form['ma_khoa']
        ma_lop = request.form['ma_lop']
        ten_lop = request.form['ten_lop']
        ma_dd = request.form['ma_dd']
        
        try:
            add_student(ma_sv, ho, ten, lop, ma_khoa, ma_lop, ten_lop, ma_dd)
            flash('Thêm sinh viên thành công!', 'success')
            return redirect(url_for('admin.sinhvien_list'))
        except Exception as e:
            flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    # Trả về danh sách Môn học theo Khoa, cũng như các dữ liệu cần thiết
    monhoc_json = []
    for mh in monhoc_list:
        monhoc_json.append({
            'MaMH': mh[0],
            'TenMH': mh[1],
            'maKhoa': mh[2]  # maKhoa là khóa ngoại của Môn học
        })
    
    return render_template('admin/students/add_student.html', 
                           khoa_list=khoa_list, 
                           monhoc_json=monhoc_json)
@admin_bp.route('/admin/edit_student/<student_id>', methods=['GET', 'POST'])
def edit_student(student_id):
    student = fetch_student_by_id(student_id)
    if request.method == 'POST':
        ho = request.form['ho']
        ten = request.form['ten']
        lop = request.form['lop']
        ma_khoa = request.form['ma_khoa']
        ma_lop = request.form['ma_lop']
        ten_lop = request.form['ten_lop']
        ma_dd = request.form['ma_dd']

        try:
            update_student(student_id, ho, ten, lop, ma_khoa, ma_lop, ten_lop, ma_dd)
            flash('Cập nhật sinh viên thành công!', 'success')
            return redirect(url_for('admin.student_list'))
        except Exception as e:
            flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return render_template('admin/students/edit_student.html', student=student)

@admin_bp.route('/admin/delete_student/<student_id>', methods=['GET', 'POST'])
def delete_student_view(student_id):
    try:
        delete_student(student_id)
        flash('Sinh viên đã được xóa thành công!', 'success')
    except Exception as e:
        flash(f'Có lỗi xảy ra: {str(e)}', 'danger')
    
    return redirect(url_for('admin.student_list'))

# Quản lý môn học
@admin_bp.route('/admin/subject_list')
def subject_list():
    subjects = fetch_all_subjects()
    return render_template('admin/subjects/subject_list.html', subjects=subjects)

@admin_bp.route('/admin/add_subject', methods=['GET', 'POST'])
def add_subject_view():
    if request.method == 'POST':
        ma_mon = request.form['ma_mon']
        ten_mon = request.form['ten_mon']
        so_tc = request.form['so_tc']
        ngay_bd = request.form['ngay_bd']

        try:
            add_subject(ma_mon, ten_mon, so_tc, ngay_bd)
            flash('Thêm môn học thành công!', 'success')
            return redirect(url_for('admin.subject_list'))
        except Exception as e:
            flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return render_template('admin/subjects/add_subject.html')

@admin_bp.route('/admin/edit_subject/<subject_id>', methods=['GET', 'POST'])
def edit_subject(subject_id):
    subject = fetch_subject_by_id(subject_id)
    if request.method == 'POST':
        ten_mon = request.form['ten_mon']
        so_tc = request.form['so_tc']
        ngay_bd = request.form['ngay_bd']

        try:
            update_subject(subject_id, ten_mon, so_tc, ngay_bd)
            flash('Cập nhật môn học thành công!', 'success')
            return redirect(url_for('admin.subject_list'))
        except Exception as e:
            flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return render_template('admin/subjects/edit_subject.html', subject=subject)

@admin_bp.route('/admin/delete_subject/<subject_id>', methods=['GET', 'POST'])
def delete_subject_view(subject_id):
    try:
        delete_subject(subject_id)
        flash('Môn học đã được xóa thành công!', 'success')
    except Exception as e:
        flash(f'Có lỗi xảy ra: {str(e)}', 'danger')
    
    return redirect(url_for('admin.subject_list'))

# Quản lý khoa
@admin_bp.route('/admin/khoa_list')
def khoa_list():
    khoas = fetch_all_khoas()
    return render_template('admin/khoas/khoa_list.html', khoas=khoas)

@admin_bp.route('/admin/add_khoa', methods=['GET', 'POST'])
def add_khoa_view():
    if request.method == 'POST':
        ma_khoa = request.form['ma_khoa']
        ten_khoa = request.form['ten_khoa']

        try:
            add_khoa(ma_khoa, ten_khoa)
            flash('Thêm khoa thành công!', 'success')
            return redirect(url_for('admin.khoa_list'))
        except Exception as e:
            flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return render_template('admin/khoas/add_khoa.html')

@admin_bp.route('/admin/edit_khoa/<khoa_id>', methods=['GET', 'POST'])
def edit_khoa(khoa_id):
    khoa = fetch_khoa_by_id(khoa_id)
    if request.method == 'POST':
        ten_khoa = request.form['ten_khoa']

        try:
            update_khoa(khoa_id, ten_khoa)
            flash('Cập nhật khoa thành công!', 'success')
            return redirect(url_for('admin.khoa_list'))
        except Exception as e:
            flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return render_template('admin/khoas/edit_khoa.html', khoa=khoa)

@admin_bp.route('/admin/delete_khoa/<khoa_id>', methods=['GET', 'POST'])
def delete_khoa_view(khoa_id):
    try:
        delete_khoa(khoa_id)
        flash('Khoa đã được xóa thành công!', 'success')
    except Exception as e:
        flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return redirect(url_for('admin.khoa_list'))

# Quản lý giảng viên
@admin_bp.route('/admin/giangvien_list')
def giangvien_list():
    
    giangviens = fetch_all_giang_viens()
    return render_template('admin/giangviens/giangvien_list.html', giangviens=giangviens)

@admin_bp.route('/admin/add_giangvien', methods=['GET', 'POST'])
def add_giangvien_view():
    if request.method == 'POST':
        ma_gv = request.form['ma_gv']
        username = request.form['username']
        password = request.form['password']
        ho = request.form['ho']
        ten = request.form['ten']
        is_admin = request.form.get('is_admin') == 'on'  # Kiểm tra xem có chọn Admin không

        try:
            add_giang_vien(ma_gv, username, password, ho, ten, is_admin)
            flash('Thêm giảng viên thành công!', 'success')
            return redirect(url_for('admin.giangvien_list'))
        except Exception as e:
            flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return render_template('admin/giangviens/add_giangvien.html')

@admin_bp.route('/admin/edit_giangvien/<ma_gv>', methods=['GET', 'POST'])
def edit_giangvien(ma_gv):
    giangvien = fetch_giang_vien_by_id(ma_gv)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        ho = request.form['ho']
        ten = request.form['ten']
        is_admin = request.form.get('is_admin') == 'on'

        try:
            update_giang_vien(ma_gv, username, password, ho, ten, is_admin)
            flash('Cập nhật giảng viên thành công!', 'success')
            return redirect(url_for('admin.giangvien_list'))
        except Exception as e:
            flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return render_template('admin/giangviens/edit_giangvien.html', giangvien=giangvien)

@admin_bp.route('/admin/delete_giangvien/<ma_gv>', methods=['GET', 'POST'])
def delete_giangvien_view(ma_gv):
    try:
        delete_giang_vien(ma_gv)
        flash('Giảng viên đã được xóa thành công!', 'success')
    except Exception as e:
        flash(f'Có lỗi xảy ra: {str(e)}', 'danger')

    return redirect(url_for('admin.giangvien_list'))

@admin_bp.route('/statistics')
def statistics():
    return render_template('admin/statistics.html')


@admin_bp.route('/admin/face_attendance', methods=['POST', 'GET'])
def face_attendance():
    if request.method == 'POST':
        # Lấy dữ liệu ảnh từ form (base64)
        photo = request.form['photo']
        student_id = request.form['student_id']  # Giả sử mã sinh viên đã được nhận diện từ khuôn mặt
        attendance_id = 'DD001'  # Mã điểm danh, có thể lấy từ hệ thống

        # Lưu thông tin điểm danh vào cơ sở dữ liệu
        mark_attendance(student_id, attendance_id, photo)
        
        return redirect(url_for('attendance_success'))

    return render_template('admin/face_attendance.html')

@admin_bp.route('/admin/attendance_success')
def attendance_success():
    return "Điểm danh thành công!"

@admin_bp.route('/admin/attendance_fail')
def attendance_fail():
    return "Không nhận diện được khuôn mặt!"

# Lecturer Routes

@lecturer_bp.route('/student_attendance')
def student_attendance():
    return render_template('lecturer/student_attendance.html')

@lecturer_bp.route('/student_list')
def lecturer_student_list():
    return render_template('lecturer/student_list.html')

@lecturer_bp.route('/course_list')
def lecturer_course_list():
    return render_template('lecturer/course_list.html')

@lecturer_bp.route('/statistics')
def lecturer_statistics():
    return render_template('lecturer/statistics.html')
