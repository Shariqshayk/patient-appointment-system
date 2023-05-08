from flask import Blueprint, request, jsonify, current_app
import hashlib
from flask_mysqldb import MySQL

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register_api():
    try:
        data = request.get_json()
        print(data)
        
        age = data['age'] if "age" in data else None
        bloodGroup = data['bloodGroup'] if 'bloodGroup' in data else None       
        city = data['city'] if "city" in data else None 
        contact = data['contact'] if "contact" in data else None
        emailId = data['emailId'] if "emailId" in data else None
        firstName = data['firstName'] if "firstName" in data else None
        lastName = data['lastName'] if "lastName" in data else None
        password = data['password'] if "password" in data else None
        pincode = data['pincode'] if "pincode" in data else None
        role = data['role'] if "role" in data else None
        street = data['street'] if "street" in data else None
        sex = data['sex'] if "sex" in data else None
        
        salt = 'appointment'
        dataBase_password = password+salt
        hashed_password = hashlib.sha256(dataBase_password.encode('utf-8'))
        hashed_password = hashed_password.hexdigest()
        print(hashed_password)
        
        mysql = MySQL()
        conn = mysql.connection
        cur = conn.cursor()
        conn.select_db('medical_management_system')
        cur.execute("Select email_id from user_details where email_id = %s", 
            (emailId,))
        rows = cur.fetchall()
        if len(rows) == 0:
            cur.execute("INSERT INTO user_details (age, blood_group, city, contact, email_id, first_name, last_name, password, pincode, role, street, sex) VALUES (%s,%s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)", 
                        (age, bloodGroup,city,contact, emailId,firstName,lastName,hashed_password, pincode,role,street, sex))
        else:
            return jsonify({'error': 'Email ID already exists'}), 500
        mysql.connection.commit()
        cur.close()

        return jsonify({'message': 'Post created successfully!'})
    
    except Exception as error_str:
        return jsonify({'error': str(error_str)}), 500
    
@user_bp.route('/login', methods=['POST'])
def login_api():
    try:
        # Get the request data
        data = request.get_json()

        emailId = data['email']
        password = data['password']
        salt = 'appointment'
        dataBase_password = password+salt
        hashed_password = hashlib.sha256(dataBase_password.encode('utf-8'))
        hashed_password = hashed_password.hexdigest()
        
        mysql = MySQL()
        conn = mysql.connection
        cur = conn.cursor()
        conn.select_db('medical_management_system')
        cur.execute("Select user_id, age, blood_group,city,contact,email_id,first_name,last_name,pincode,role,sex,street from user_details where email_id = %s and password = %s", 
                    (emailId, hashed_password))
        rows = cur.fetchall()
        if len(rows) != 0:
            keys = ['user_id', 'age', 'bloodGroup','city','contact','emailId','firstName','lastName','pincode','role','sex','street']
            data_dict = {}
            for i, item in enumerate(rows[0]):
                data_dict[keys[i]] = item
            data_dict['Message'] = 'Login Successful!'
            print(data_dict)
        else:
            data_dict = {'Message': 'Email Id or password incorrect'}
        mysql.connection.commit()
        cur.close()

        return data_dict
    
    except Exception as error_str:
        return jsonify({'error': str(error_str)}), 500