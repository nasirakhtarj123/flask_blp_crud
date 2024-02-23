from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.resources.blp import blp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nazir:123456789@localhost:5432/database'
db = SQLAlchemy(app)

app.register_blueprint(blp)

if __name__ == '__main__':
    app.run(debug=True)
