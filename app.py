from flask import Flask, jsonify, request, Blueprint
from flask_mysqldb import MySQL
from routes.user import user_bp
from routes.appointments import appointments_bp
from models import database

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.register_blueprint(user_bp, url_prefix='/api/user')
app.register_blueprint(appointments_bp, url_prefix='/api')

database.mysql.init_app(app)
database.create_tables(app)

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PORT'] = 3306
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'Welcome@29'
# app.config['MYSQL_DB'] = 'dental_management_system'

# mysql = MySQL(app)

# @app.before_first_request
# def create_tables():
#     cur = mysql.connection.cursor()
#     cur.execute("""
#         CREATE TABLE IF NOT EXISTS user_details (
#             id INT PRIMARY KEY auto_increment,
#             age INT DEFAULT NULL,
#             blood_group VARCHAR(255) DEFAULT NULL,
#             city VARCHAR(255) DEFAULT NULL,
#             contact BIGINT DEFAULT NULL,
#             email_id VARCHAR(255) DEFAULT NULL,
#             first_name VARCHAR(255) DEFAULT NULL,
#             last_name VARCHAR(255) DEFAULT NULL,
#             password VARCHAR(255) DEFAULT NULL,
#             pincode VARCHAR(255) DEFAULT NULL,
#             role VARCHAR(255) DEFAULT NULL,
#             sex VARCHAR(255) DEFAULT NULL,
#             street VARCHAR(255) DEFAULT NULL  
#         )
#     """)
#     cur.close()

if __name__ == '__main__':
    app.run()
