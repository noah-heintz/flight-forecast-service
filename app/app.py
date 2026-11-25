from flask import Flask, render_template

#Creates a Flask application instance
app = Flask(__name__)

#Defines URL
@app.route("/")
def home():
    return render_template("index.html") #tells Flask to load HTML template

if __name__ == "__main__":
    app.run(debug=True)