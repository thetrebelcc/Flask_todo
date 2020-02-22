# Brings packages in
from flask import Flask, render_template, url_for


# Nameing of the app
app = Flask(__name__)


# Routing for app 
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)