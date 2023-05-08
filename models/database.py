from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def create_tables(app):
    with app.app_context():
        conn = mysql.connection
        cur = conn.cursor()
        
        cur.execute("Create database if not exists medical_management_system")
        conn.select_db('medical_management_system')

        cur.execute('''CREATE TABLE IF NOT EXISTS doctors (
                        doctor_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        name VARCHAR(50) NOT NULL,
                        email VARCHAR(255) NOT NULL,
                        speciality VARCHAR(50),
                        experience INT NOT NULL,
                        hospital_name VARCHAR(255) NOT NULL,
                        city VARCHAR(50) NOT NULL,
                        rating FLOAT NOT NULL
                        )''')
        # Insert data into doctors table only if it is newly created
        cur.execute("SELECT COUNT(*) FROM doctors")
        count = cur.fetchone()[0]
        if count == 0:
            cur.execute('''INSERT INTO doctors (name, email, speciality, experience, hospital_name, city, rating)
                        VALUES
                        ('Frank Doe', 'frankdoe@gmail.com', 'Cardiology',10,'Heart Hospital', 'Guildford', 4.7),
                        ('Jane Smith', 'janesmith@gmail.com','Pediatrics', 5,'Smith Clinic','London', 4.5),
                        ('Bob Johnson', 'bobjohnson@gmail.com', 'Dermatology',9,'Skin clinic','Birmingham', 4.9),
                        ('Preeti Mehra','preetimehra@gmail.com','General Physician',15,'Health care hospital','London', 4.8)''')
        
        cur.execute("""
                    CREATE TABLE IF NOT EXISTS doctor_availability (
                    availability_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                    doctor_id INT NOT NULL,
                    date DATE NOT NULL,
                    start_time TIME NOT NULL,
                    end_time TIME NOT NULL,
                    status ENUM('Available', 'Not Available') NOT NULL,
                    FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
                    )""")

        # Insert data into doctors table only if it is newly created
        cur.execute("SELECT COUNT(*) FROM doctor_availability")
        count = cur.fetchone()[0]
        if count == 0:
            cur.execute("""INSERT INTO doctor_availability (doctor_id, date, start_time, end_time, status) VALUES
                        (1, '2023-05-15', '08:00:00', '12:00:00', 'Available'),
                        (1, '2023-05-15', '13:00:00', '17:00:00', 'Available'),
                        (1, '2023-05-16', '09:00:00', '12:00:00', 'Available'),
                        (1, '2023-05-17', '14:00:00', '18:00:00', 'Available'),
                        (2, '2023-05-01', '10:00:00', '14:00:00', 'Available'),
                        (2, '2023-05-01', '15:00:00', '18:00:00', 'Available'),
                        (2, '2023-05-02', '09:00:00', '12:00:00', 'Not Available'),
                        (2, '2023-05-02', '14:00:00', '17:00:00', 'Available');
                        """)
                    
        cur.execute("""
            CREATE TABLE IF NOT EXISTS user_details (
                user_id INT PRIMARY KEY auto_increment,
                age INT DEFAULT NULL,
                blood_group VARCHAR(255) DEFAULT NULL,
                city VARCHAR(255) DEFAULT NULL,
                contact BIGINT DEFAULT NULL,
                email_id VARCHAR(255) DEFAULT NULL,
                first_name VARCHAR(255) DEFAULT NULL,
                last_name VARCHAR(255) DEFAULT NULL,
                password VARCHAR(255) DEFAULT NULL,
                pincode VARCHAR(255) DEFAULT NULL,
                role VARCHAR(255) DEFAULT NULL,
                sex VARCHAR(255) DEFAULT NULL,
                street VARCHAR(255) DEFAULT NULL  
            )
        """)

        cur.execute('''CREATE TABLE IF NOT EXISTS appointments (
                        appointment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                        patient_id INT,
                        doctor_id INT,
                        doctor_name VARCHAR(255) NOT NULL,
                        appointment_date DATE NOT NULL,
                        appointment_start_time TIME NOT NULL,
                        appointment_end_time TIME NOT NULL,
                        status ENUM('Pending', 'Confirmed', 'Cancelled'),
                        FOREIGN KEY (patient_id) REFERENCES user_details(user_id) ON DELETE CASCADE,
                        FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id) ON DELETE CASCADE
                        )''')

        mysql.connection.commit()
        cur.close()

# @app.before_first_request
# def initialize_database():
#     create_tables()