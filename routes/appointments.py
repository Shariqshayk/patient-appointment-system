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
    
@appointments_bp.route('/appointment', methods=['GET'])
def get_doctor_by_speciality():
    try:
        speciality = request.args.get('speciality')
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("Select * from doctors where speciality = %s",(speciality,))
        rows = cur.fetchall()
        print(rows)
        data_dict = {}
        keys = ['doctor_id', 'name','email','speciality','experience','hospital_name','city', 'rating']
        data_dict = [dict(zip(keys, item)) for item in rows]
        print(data_dict)
        mysql.connection.commit()
        cur.close()

        return jsonify(data_dict)
    
    except Exception as error_str:
        return jsonify({'error': str(error_str)}), 500
    
@appointments_bp.route('/appointment/<doctor_id>', methods=['GET'])
def get_doctor_by_id(doctor_id):
    try:
        #doctor_id = request.args.get('doctor_id')
        print("-->",doctor_id)
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("Select * from doctors where doctor_id = %s",(doctor_id,))
        rows = cur.fetchall()
        print(rows)
        data_dict = {}
        keys = ['doctor_id', 'name','email','speciality','experience','hospital_name','city', 'rating']
        # data_dict = [dict(zip(keys, item)) for item in rows]
        # print(data_dict)
        for i, item in enumerate(rows[0]):
            data_dict[keys[i]] = item
        print(data_dict)
        mysql.connection.commit()
        cur.close()

        return data_dict
    
    except Exception as error_str:
        return jsonify({'error': str(error_str)}), 500
    
@appointments_bp.route('/appointment/availability/<doctor_id>', methods=['GET'])
def get_doctor_by_availability(doctor_id):
    try:
        #doctor_id = request.args.get('doctor_id')
        print("-->",doctor_id)
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("Select * from doctor_availability where doctor_id = %s and status = 'Available'",(doctor_id,))
        rows = cur.fetchall()
        data_dict = {}
        keys = ['availability_id', 'doctor_id','date', 'start_time','end_time', 'status']
        data_dict = [dict(zip(keys, item)) for item in rows]
        print(data_dict)
        for item in data_dict:
            print(type(item['date']))
            start_time_hr = (datetime.datetime.min + item['start_time']).strftime('%H:%M:%S')
            end_time_hr = (datetime.datetime.min + item['end_time']).strftime('%H:%M:%S')
            item['start_time'] = start_time_hr
            item['end_time'] = end_time_hr
            item['date'] = item['date'].strftime('%Y-%m-%d')
            print("---->",type(start_time_hr))
        print(data_dict)
        mysql.connection.commit()
        cur.close()

        return jsonify(data_dict)
    
    except Exception as error_str:
        return jsonify({'error': str(error_str)}), 500
    
@appointments_bp.route('/appointment/book_appointment', methods=['POST'])
def book_appointment():
    try:
        data = request.get_json()
        print(data)
        
        patient_id = data['patient_id'] if "patient_id" in data else None
        doctor_id = data['doctor_id'] if 'doctor_id' in data else None       
        doctor_name = data['doctor_name'] if "doctor_name" in data else None 
        appointment_date = data['appointment_date'] if "appointment_date" in data else None
        appointment_start_time = data['appointment_start_time'] if "appointment_start_time" in data else None
        appointment_end_time = data['appointment_end_time'] if "appointment_end_time" in data else None
        status = data['status'] if "status" in data else None
        
        appointment_date = datetime.datetime.strptime(appointment_date, '%Y-%m-%d').date()
        appointment_start_time = datetime.datetime.strptime(appointment_start_time, '%H:%M:%S').time()
        appointment_start_time = datetime.timedelta(hours=appointment_start_time.hour, minutes=appointment_start_time.minute)
        appointment_end_time = datetime.datetime.strptime(appointment_end_time, '%H:%M:%S').time()
        appointment_end_time = datetime.timedelta(hours=appointment_end_time.hour, minutes=appointment_end_time.minute)
        
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO appointments (patient_id, doctor_id, doctor_name, appointment_date, appointment_start_time, appointment_end_time, status) VALUES (%s,%s,%s, %s,%s,%s,%s)", 
                   (patient_id, doctor_id, doctor_name, appointment_date, appointment_start_time, appointment_end_time, status))
        cur.execute("Update doctor_availability SET status = 'Not Available' where doctor_id = %s and date = %s and start_time = %s",(doctor_id, appointment_date, appointment_start_time))
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Post created successfully!'})
    
    except Exception as error_str:
        return jsonify({'error': str(error_str)}), 500
    
@appointments_bp.route('/appointment/track/<user_id>', methods=['GET'])
def track_appointment(user_id):
    try:
        #doctor_id = request.args.get('doctor_id')
        print("-->",user_id)
        mysql = MySQL()
        cur = mysql.connection.cursor()
        cur.execute("Select * from appointments where patient_id = %s",(user_id,))
        rows = cur.fetchall()
        data_dict = {}
        keys = ['appointment_id','patient_id', 'doctor_id','doctor_name','appointment_date', 'appointment_start_time','appointment_end_time', 'status']
        data_dict = [dict(zip(keys, item)) for item in rows]
        print(data_dict)
        for item in data_dict:
            print(type(item['appointment_date']))
            start_time_hr = (datetime.datetime.min + item['appointment_start_time']).strftime('%H:%M')
            end_time_hr = (datetime.datetime.min + item['appointment_end_time']).strftime('%H:%M')
            item['appointment_start_time'] = start_time_hr
            item['appointment_end_time'] = end_time_hr
            item['appointment_date'] = item['appointment_date'].strftime('%Y-%m-%d')
        print(data_dict)
        mysql.connection.commit()
        cur.close()

        return jsonify(data_dict)
    
    except Exception as error_str:
        return jsonify({'error': str(error_str)}), 500