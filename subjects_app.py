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
    return "Subjects API - Access /subjects endpoint"

@app.route('/subjects')
def get_subjects():
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT 
                    year,
                    status,
                    GROUP_CONCAT(course_title ORDER BY course_code) AS courses
                FROM subjects
                WHERE program = 'BSc. Computer Network and Information Security Engineering'
                GROUP BY year, status
                ORDER BY year, FIELD(status, 'Core', 'Elective')
            """)
            results = cursor.fetchall()
            formatted = {}

            for row in results:
                year = str(row['year'])
                status = row['status']
                if year not in formatted:
                    formatted[year] = {'Core': [], 'Elective': []}
                formatted[year][status] = row['courses'].split(',')

            return jsonify({
                'success': True,
                'program': 'BSc. Computer Network and Information Security Engineering',
                'subjects_by_year': formatted
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