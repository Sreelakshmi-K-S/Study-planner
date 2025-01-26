from flask import Flask, request, render_template, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to the database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="Sreelakshmi",
        password="Sreelakshmiks@05",
        database="studyplanner"
    )

# Login routes
@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    db = connect_to_database()
    cursor = db.cursor()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()

    if result:
        print("Login successful!")
        return redirect(url_for('dashboard'))
    else:
        return "Invalid username or password."

# Dashboard routes
@app.route('/dashboard')
def dashboard():
    return render_template('dash3.html')

@app.route('/timetable')
def timetable():
    return render_template('time.html')

@app.route('/todo')
def todo():
    return render_template('todo.html')

@app.route('/quiz')
def quiz():
    return render_template('quiz.html')



@app.route('/quiz/science')
def quiz_science():
    return render_template('quizs.html') 

@app.route('/quiz/math')
def quiz_math():
    return render_template('quizm.html') 

@app.route('/quiz/social_studies')
def quiz_social_studies():
    return render_template('quizss.html') 

@app.route('/quiz/english')
def quiz_english():
    return render_template('quize.html')

@app.route('/game')
def game():
    return render_template('game1.html')

@app.route('/study_materials')
def study_materials():
    return render_template('study.html')

@app.route('/progress')
def progress():
    return render_template('progress.html')

@app.route('/settings')
def settings():
    return render_template('settings.html')

if __name__ == "__main__":
    app.run(debug=True, port=8080)
