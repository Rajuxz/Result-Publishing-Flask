from flask import Flask,render_template,jsonify,request
from flask_sqlalchemy import SQLAlchemy

# Creating an extension
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.app_context().push()
db.init_app(app)

# App Routing

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/staffs')
def staffs():
    return render_template('staffs/root.html')

@app.route('/about')
def about():
    return render_template('about/root.html')

@app.route('/reviews')
def reviews():
    return render_template('reviews/root.html')

@app.route('/admin')
def admin():
    return render_template('admin/dashboard.html')

@app.route('/students')
def students():
    return render_template('admin/components/student.html')

  
# Student Sign in Endpoint

@app.route('/sign_in',methods=['POST'])
def sign_in():

    email = request.form['email']
    password = request.form['password']

    print(email)
    print(password)

    if email and password:
        newEmail = email[::-1]
        return jsonify({'email':newEmail})
    
    return jsonify({'error':'Something went wrong.'})


# Endpoint to handle add student request from admin section.
@app.route('/addstudent',methods=['POST'])
def addstudent():
    full_name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    password = request.form['password']

    print(full_name)
    print(number)
    print(email)
    print(password)

    return jsonify({'hi':'test'})


# Database class
class Class(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    class_name = db.Column(db.String(80),nullable = False)


class Student(db.Model):
    std_id = db.Column(db.Integer,primary_key = True)
    std_class = db.Column(db.Integer, db.ForeignKey(Class.id),nullable = False)
    std_name = db.Column(db.String(20),nullable = False)
    std_phone = db.Column(db.String(15),unique=True,nullable = False)
    std_email = db.Column(db.String(50),unique=True,nullable = False)
    std_psw = db.Column(db.String(15),unique=True,nullable = False)


class Admin(db.Model):
    admin_id = db.Column(db.Integer,primary_key=True)
    admin_name = db.Column(db.String(30),nullable=False)
    admin_email = db.Column(db.String(50),unique=True,nullable=False)
    admin_password = db.Column(db.String(40),unique=True,nullable=False)


if __name__ == '__main__':

    app.run(debug=True)