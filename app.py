from flask import Flask,render_template,jsonify,request

app = Flask(__name__)

class Routing:
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


if __name__ == '__main__':
    app.run(debug=True)