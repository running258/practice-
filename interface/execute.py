from flask import Flask, render_template, request

from interface.supplyLogin import supplyLogin

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login', methods = ['POST'])
def login():
    userName = request.form['userName']
    passWord = request.form['passWord']
    authorization = supplyLogin(userName,passWord)
    print(authorization)
    return authorization
    # if request.method == "POST":
    #     email = request.form['email']
    #     return render_template("success.html", email = email)
    # else:
    #     pass

if __name__ == "__main__":
    app.run()