import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = False
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, sql):
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
    except Error as e:
        print(e)


def create_student(conn, student):
    sql = '''INSERT INTO student(fullname,mark,hobby,is_married)
    VALUES (?,?,?,?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student)
        conn.commit()
    except Error as e:
        print(e)


def read_student(conn):
    try:
        sql = '''SELECT * FROM student'''
        cursor = conn.cursor()
        cursor.execute(sql)
        row = cursor.fetchall()
        for i in row:
            print(i)
    except Error as e:
        print(e)


def delete_student(conn, student_id):
    sql = '''DELETE FROM student WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (student_id,))
        conn.commit()
    except Error as e:
        print(e)


def update_student(conn, student_id, student):
    sql = '''UPDATE student
    SET fullname=?, mark=?, hobby=?, is_married=?
    WHERE id=?'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, student + (student_id,))
        conn.commit()
    except Error as e:
        print(e)


database = 'user.db'

sql_create_table = '''
CREATE TABLE student( 
id INTEGER PRIMARY KEY AUTOINCREMENT,
fullname VARCHAR (50) NOT NULL,
mark FLOAT NOT NULL DEFAULT 0.0,
hobby TEXT DEFAULT NULL,
is_married BOOLEAN DEFAULT FALSE
);
'''

connection = create_connection(database)
if connection is not None:
    print('все окей')
    # create_table(connection,sql_create_table)
    # create_student(connection, ('данияр', 10.0, 'Sleep', True))
    # read_student(connection)
    # delete_student(connection, 1)
    # update_student(connection, 1, ('Jane Doe', 9.0, 'Reading', False))
    read_student(connection)