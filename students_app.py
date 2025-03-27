from flask import Flask, jsonify
import pymysql
from pymysql.cursors import DictCursor

app = Flask(__name__)

# MySQL configuration for XAMPP
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'students_db'

def get_db_connection():
    return pymysql.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB'],
        cursorclass=DictCursor,
        autocommit=True
    )

@app.route('/')
def home():
    return "Students API - Access /students endpoint"

@app.route('/students')
def get_students():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT name, program 
                FROM students
                ORDER BY name
            """)
            students = cursor.fetchall()
            return jsonify({
                'success': True,
                'count': len(students),
                'students': students
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5000)