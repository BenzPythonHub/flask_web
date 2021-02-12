from flask import Flask
from flask import render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if(request.method == 'POST'):
        #save data
        username = request.form['username']
        email = request.form['email']
        user = User(
            id=3,
            username=username,
            email=email,
        )

        db.session.add(user)
        db.session.commit()
        return "Success"


    elif(request.method == 'GET'):
        # return "Hello World XD"
        return render_template("test.html")

@app.route('/hello')
def hello():
    return "Bello Banana XDDDDDDDDD"

@app.route('/hello_int/<int:user_id>')
def hello_userid(user_id):
    return f"Bello {user_id} Banana XDDDDDDD"

@app.route('/hello_str/<username>')
def hello_username(username):
    return f"Bello {username} Banana XDDDDDDD"
    # return "Bello" + url_for("hello")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
