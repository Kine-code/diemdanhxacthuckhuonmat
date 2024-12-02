-- Tạo cơ sở dữ liệu FaceRecognitionAttendance1
CREATE DATABASE FaceRecognitionAttendance2;

-- Sử dụng cơ sở dữ liệu
USE FaceRecognitionAttendance2;

CREATE TABLE Khoa (
    maKhoa NVARCHAR(50) PRIMARY KEY,
    TenKhoa NVARCHAR(100) NOT NULL
);

-- 2. Bảng SinhVien: Lưu thông tin sinh viên
CREATE TABLE SinhVien (
    MaSV NVARCHAR(50) PRIMARY KEY,
    Lop NVARCHAR(50),
    Ho NVARCHAR(50),
    Ten NVARCHAR(50),
    maKhoa NVARCHAR(50),
    maLop NVARCHAR(50),
    TenLop NVARCHAR(100),
    MaDD NVARCHAR(50),
    FOREIGN KEY (maKhoa) REFERENCES Khoa(maKhoa)
);

-- 3. Bảng GiangVien: Lưu thông tin giảng viên
CREATE TABLE GiangVien (
    MaGV NVARCHAR(50) PRIMARY KEY,
    Username NVARCHAR(50) NOT NULL,
    Password NVARCHAR(100) NOT NULL,
    Ho NVARCHAR(50),
    Ten NVARCHAR(50),
    isAdmin BIT NOT NULL DEFAULT 0
);

-- 4. Bảng MonHoc: Lưu thông tin các môn học
CREATE TABLE MonHoc (
    MaMH NVARCHAR(50) PRIMARY KEY,
    TenMH NVARCHAR(100) NOT NULL,
    SoTC INT NOT NULL,
    NgayBD DATE
);

-- 5. Bảng DiemDanh: Lưu thông tin về các buổi điểm danh
CREATE TABLE DiemDanh (
    MaDD NVARCHAR(50) PRIMARY KEY,
    MaGV NVARCHAR(50),
    MaMH NVARCHAR(50),
    MaLop NVARCHAR(50),
    NgayDiemDanh DATE NOT NULL,
    TrangThaiDiemDanh NVARCHAR(50) DEFAULT 'Chưa thực hiện',
    FOREIGN KEY (MaGV) REFERENCES GiangVien(MaGV),
    FOREIGN KEY (MaMH) REFERENCES MonHoc(MaMH)
);

-- 6. Bảng TrangThaiDiemDanh: Lưu thông tin trạng thái của buổi học
CREATE TABLE TrangThaiDiemDanh (
    MaDD NVARCHAR(50) PRIMARY KEY,
    TrangThai NVARCHAR(50) DEFAULT 'Chưa điểm danh',
    ThoiGianCapNhat DATETIME,
    FOREIGN KEY (MaDD) REFERENCES DiemDanh(MaDD)
);

-- 7. Bảng DiemDanhSinhVien: Lưu kết quả điểm danh của từng sinh viên
CREATE TABLE DiemDanhSinhVien (
    ID INT PRIMARY KEY IDENTITY(1,1),
    MaDD NVARCHAR(50),
    MaSV NVARCHAR(50),
    TrangThai NVARCHAR(50),
    ThoiGianDiemDanh DATETIME,
    HinhAnhDiemDanh NVARCHAR(255),
    FOREIGN KEY (MaDD) REFERENCES DiemDanh(MaDD),
    FOREIGN KEY (MaSV) REFERENCES SinhVien(MaSV)
);

-- 8. Bảng Images: Lưu ảnh khuôn mặt sinh viên
CREATE TABLE Images (
    IDIMG INT PRIMARY KEY IDENTITY(1,1),
    LinkIMG NVARCHAR(255) NOT NULL,
    MaSV NVARCHAR(50),
    FOREIGN KEY (MaSV) REFERENCES SinhVien(MaSV)
);

-- Dữ liệu mẫu cho bảng Khoa
INSERT INTO Khoa (maKhoa, TenKhoa) VALUES
('K001', 'Khoa Công Nghệ Thông Tin'),
('K002', 'Khoa Kinh Tế'),
('K003', 'Khoa Điện Tử Viễn Thông'),
('K004', 'Khoa Quản Trị Kinh Doanh'),
('K005', 'Khoa Luật');

-- Dữ liệu mẫu cho bảng SinhVien
INSERT INTO SinhVien (MaSV, Lop, Ho, Ten, maKhoa, maLop, TenLop, MaDD) VALUES
('SV001', 'CNTT1', 'Nguyễn', 'An', 'K001', 'L001', 'Lớp 1', 'DD001'),
('SV002', 'KinhTe1', 'Trần', 'Bình', 'K002', 'L002', 'Lớp 2', 'DD002'),
('SV003', 'DTVT1', 'Lê', 'Cường', 'K003', 'L003', 'Lớp 3', 'DD003'),
('SV004', 'QTKD1', 'Phạm', 'Dương', 'K004', 'L004', 'Lớp 4', 'DD004'),
('SV005', 'Luat1', 'Hoàng', 'Duy', 'K005', 'L005', 'Lớp 5', 'DD005');
INSERT INTO SinhVien (MaSV, Lop, Ho, Ten, maKhoa, maLop, TenLop, MaDD) 
VALUES 
('SV006', 'CNTT1', 'Công', 'Kiên', 'K001', 'L001', 'Lớp 1', 'DD001');

-- Dữ liệu mẫu cho bảng GiangVien
INSERT INTO GiangVien (MaGV, Username, Password, Ho, Ten, isAdmin) VALUES
('admin', 'admin', '123456', 'Công', 'Kiên', 1),  
('GV001', 'GV001', 'password123', 'Nguyễn', 'Nam', 0),
('GV002', 'GV002', 'password456', 'Trần', 'Hương', 0),
('GV003', 'GV003', 'password789', 'Lê', 'Quân', 0),
('GV004', 'GV004', 'password111', 'Phạm', 'Lan', 0),
('GV005', 'GV005', 'password222', 'Hoàng', 'Khoa', 0);

-- Dữ liệu mẫu cho bảng MonHoc
INSERT INTO MonHoc (MaMH, TenMH, SoTC, NgayBD) VALUES
('MH001', 'Lập Trình Java', 3, '2024-09-01'),
('MH002', 'Kinh Tế Vi Mô', 3, '2024-09-01'),
('MH003', 'Điện Tử Cơ Bản', 3, '2024-09-01'),
('MH004', 'Quản Trị Doanh Nghiệp', 3, '2024-09-01'),
('MH005', 'Pháp Luật Đại Cương', 3, '2024-09-01');

-- Dữ liệu mẫu cho bảng DiemDanh
INSERT INTO DiemDanh (MaDD, MaGV, MaMH, MaLop, NgayDiemDanh) VALUES
('DD001', 'GV001', 'MH001', 'L001', '2024-09-01'),
('DD002', 'GV002', 'MH002', 'L002', '2024-09-02'),
('DD003', 'GV003', 'MH003', 'L003', '2024-09-03'),
('DD004', 'GV004', 'MH004', 'L004', '2024-09-04'),
('DD005', 'GV005', 'MH005', 'L005', '2024-09-05');

-- Dữ liệu mẫu cho bảng TrangThaiDiemDanh
INSERT INTO TrangThaiDiemDanh (MaDD, TrangThai, ThoiGianCapNhat) VALUES
('DD001', 'Chưa điểm danh', GETDATE()),
('DD002', 'Đã điểm danh', GETDATE()),
('DD003', 'Chưa điểm danh', GETDATE()),
('DD004', 'Đã điểm danh', GETDATE()),
('DD005', 'Chưa điểm danh', GETDATE());

INSERT INTO DiemDanhSinhVien (MaDD, MaSV, TrangThai, ThoiGianDiemDanh, HinhAnhDiemDanh)
VALUES 
('DD001', 'SV001', 'Có mặt', '2024-09-01 08:00:00', 'images/sv001.jpg'),
('DD001', 'SV002', 'Vắng mặt', '2024-09-01 08:00:00', 'images/sv002.jpg'),
('DD001', 'SV003', 'Muộn', '2024-09-01 08:10:00', 'images/sv003.jpg');

INSERT INTO Images (LinkIMG, MaSV) 
VALUES 
('attendance_images/sv006.jpg', 'SV006');

IF NOT EXISTS (SELECT 1 FROM DiemDanh WHERE MaDD = 'DD001')
BEGIN
    INSERT INTO DiemDanh (MaDD, MaGV, MaMH, MaLop, NgayDiemDanh)
    VALUES ('DD001', 'GV001', 'MH001', 'L001', '2024-09-01');  -- Tạo buổi điểm danh nếu chưa có
END

INSERT INTO DiemDanhSinhVien (MaDD, MaSV, TrangThai, ThoiGianDiemDanh, HinhAnhDiemDanh) 
VALUES 
('DD001', 'SV006', 'Có mặt', '2024-09-01 08:00:00', 'attendance_images/sv006.jpg');
 select * from DiemDanhSinhVien