-- Tạo cơ sở dữ liệu
CREATE DATABASE FaceRecognitionAttendance1;

-- Sử dụng cơ sở dữ liệu
USE FaceRecognitionAttendance1;

-- Bảng Khoa
CREATE TABLE Khoa (
    maKhoa NVARCHAR(50) PRIMARY KEY,
    TenKhoa NVARCHAR(100) NOT NULL
);

-- Bảng SinhVien
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

-- Bảng GiangVien
CREATE TABLE GiangVien (
    MaGV NVARCHAR(50) PRIMARY KEY,
    Password NVARCHAR(100) NOT NULL,
    Ho NVARCHAR(50),
    Ten NVARCHAR(50)
);

-- Bảng Images
CREATE TABLE Images (
    IDIMG INT PRIMARY KEY IDENTITY(1,1),
    LinkIMG NVARCHAR(255) NOT NULL,
    MaSV NVARCHAR(50),
    FOREIGN KEY (MaSV) REFERENCES SinhVien(MaSV)
);

-- Bảng MonHoc
CREATE TABLE MonHoc (
    MaMH NVARCHAR(50) PRIMARY KEY,
    TenMH NVARCHAR(100) NOT NULL,
    SoTC INT NOT NULL,
    NgayBD DATE
);

-- Bảng DiemDanh
CREATE TABLE DiemDanh (
    MaDD NVARCHAR(50) PRIMARY KEY,
    MaGV NVARCHAR(50),
    MaMH NVARCHAR(50),
    MaLop NVARCHAR(50),
    FOREIGN KEY (MaGV) REFERENCES GiangVien(MaGV),
    FOREIGN KEY (MaMH) REFERENCES MonHoc(MaMH)
);

-- Bảng TrangThai
CREATE TABLE TrangThai (
    MaDD NVARCHAR(50),
    NgayHT DATE,
    TrangThaiHT NVARCHAR(50),
    PRIMARY KEY (MaDD),
    FOREIGN KEY (MaDD) REFERENCES DiemDanh(MaDD)
);

-- Bảng CtDiemDanh
CREATE TABLE CtDiemDanh (
    MaDD NVARCHAR(50),
    NgayDD DATE NOT NULL,
    SoNV INT NOT NULL,
    NgayBDMH DATE,
    NgayKTMH DATE,
    PRIMARY KEY (MaDD, NgayDD),
    FOREIGN KEY (MaDD) REFERENCES DiemDanh(MaDD)
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

-- Dữ liệu mẫu cho bảng GiangVien
INSERT INTO GiangVien (MaGV, Password, Ho, Ten) VALUES
('GV001', 'password123', 'Nguyễn', 'Nam'),
('GV002', 'password456', 'Trần', 'Hương'),
('GV003', 'password789', 'Lê', 'Quân'),
('GV004', 'password111', 'Phạm', 'Lan'),
('GV005', 'password222', 'Hoàng', 'Khoa');

-- Dữ liệu mẫu cho bảng Images
INSERT INTO Images (LinkIMG, MaSV) VALUES
('https://example.com/image1.jpg', 'SV001'),
('https://example.com/image2.jpg', 'SV002'),
('https://example.com/image3.jpg', 'SV003'),
('https://example.com/image4.jpg', 'SV004'),
('https://example.com/image5.jpg', 'SV005');

-- Dữ liệu mẫu cho bảng MonHoc
INSERT INTO MonHoc (MaMH, TenMH, SoTC, NgayBD) VALUES
('MH001', 'Lập Trình Java', 3, '2024-09-01'),
('MH002', 'Kinh Tế Vi Mô', 3, '2024-09-01'),
('MH003', 'Điện Tử Cơ Bản', 3, '2024-09-01'),
('MH004', 'Quản Trị Doanh Nghiệp', 3, '2024-09-01'),
('MH005', 'Pháp Luật Đại Cương', 3, '2024-09-01');

-- Dữ liệu mẫu cho bảng DiemDanh
INSERT INTO DiemDanh (MaDD, MaGV, MaMH, MaLop) VALUES
('DD001', 'GV001', 'MH001', 'L001'),
('DD002', 'GV002', 'MH002', 'L002'),
('DD003', 'GV003', 'MH003', 'L003'),
('DD004', 'GV004', 'MH004', 'L004'),
('DD005', 'GV005', 'MH005', 'L005');

-- Dữ liệu mẫu cho bảng TrangThai
INSERT INTO TrangThai (MaDD, NgayHT, TrangThaiHT) VALUES
('DD001', '2024-09-01', 'Đã điểm danh'),
('DD002', '2024-09-02', 'Chưa điểm danh'),
('DD003', '2024-09-03', 'Đã điểm danh'),
('DD004', '2024-09-04', 'Chưa điểm danh'),
('DD005', '2024-09-05', 'Đã điểm danh');

-- Dữ liệu mẫu cho bảng CtDiemDanh
INSERT INTO CtDiemDanh (MaDD, NgayDD, SoNV, NgayBDMH, NgayKTMH) VALUES
('DD001', '2024-09-01', 30, '2024-09-01', '2024-09-01'),
('DD002', '2024-09-02', 28, '2024-09-02', '2024-09-02'),
('DD003', '2024-09-03', 32, '2024-09-03', '2024-09-03'),
('DD004', '2024-09-04', 25, '2024-09-04', '2024-09-04'),
('DD005', '2024-09-05', 35, '2024-09-05', '2024-09-05');
