# Brings packages in
from flask import Flask, render_template, url_for
from flask import flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Nameing of the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    content = db.Column(db.string(200), nullable = False)
    completed = db.Column(db.Integer, defualt = 0)
    date_created = db.Column(db.Datetime, defualt=datetime.utcnow)



# Routing for app 
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)