from flask import Flask, render_template
import app
FlaskApp = Flask(__name__)

@FlaskApp.route("/")
def hello_world():
    return render_template("index.html")

@FlaskApp.route("/home")
def home():
    sample()
    return ""
def sample():
    print("Test")
    app.main()
if __name__ == '__main__':
    FlaskApp.run(debug=True)