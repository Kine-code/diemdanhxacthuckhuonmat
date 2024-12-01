import pypyodbc
import pypyodbc as odbc

def get_db_connection():
    conn = pypyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=DESKTOP-2MC26TB\SQLEXPRESS;'
        'DATABASE=FaceRecognitionAttendance2;'
        'UID=sa;'
        'PWD=123456'
      

    )
    return conn