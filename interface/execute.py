from flask import Flask, render_template, request

from interface.supplyLogin import supplyInit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods = ['POST'])
def login():
    userName = request.form['userName']
    passWord = request.form['passWord']
    login = supplyInit()
    authorization = login.supplyLogin(userName,passWord)
    print(authorization)
    return authorization

if __name__ == "__main__":
    app.run()