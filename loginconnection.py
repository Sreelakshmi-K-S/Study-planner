from flask import Flask,request, render_template,redirect, url_for
import mysql.connector
loginconnection = Flask(__name__)
# Connect to the database

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",  # or your MySQL host
        user="Sreelakshmi",       # your MySQL username
        password="Sreelakshmiks@05",  # your MySQL password
        database="studyplanner"  # your database name
    )

@loginconnection.route('/')
def index():
    return render_template('login.html')

@loginconnection.route('/login', methods=['POST'])
def login():
    # Get the data from the form
    username = request.form['username']
    password = request.form['password']
    
    # Connect to the database
    db = connect_to_database()
    cursor = db.cursor()

    # Validate login credentials
    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        print("Login successful !")
        return redirect(url_for('dashboard'))
    else:
        return "Invalid username or password."

    cursor.close()
    db.close()
@loginconnection.route('/dashboard')
def dashboard():
    # This will render dash3.html
    return render_template('dash3.html')


if __name__ == "__main__":
    loginconnection.run(debug=True)