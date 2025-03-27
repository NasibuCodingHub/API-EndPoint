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
    return "Students and Subjects API - Access /students or /subjects endpoints"

if __name__ == '__main__':
    app.run(debug=True, port=5000)