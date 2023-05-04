from flask import Blueprint, request, jsonify, current_app
import hashlib
from flask_mysqldb import MySQL
import datetime

appointments_bp = Blueprint('appointments', __name__)

@appointments_bp.route('/appointment/all_doctors', methods=['GET'])
def get_all_doctors():
    try:      
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("Select * from doctors")
        rows = cur.fetchall()
        data_dict = {}
        keys = ['doctor_id', 'name','email','speciality','experience','hospital_name','city', 'rating']
        data_dict = [dict(zip(keys, item)) for item in rows]
        print(data_dict)
        mysql.connection.commit()
        cur.close()

        return jsonify(data_dict)
    
    except Exception as error_str:
        return jsonify({'error': str(error_str)}), 500
    
