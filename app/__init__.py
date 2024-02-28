from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user_name:password@localhost:5432/database_name'
db = SQLAlchemy(app)

from app.resources.blp import blp
app.register_blueprint(blp)

if __name__ == '__main__':
    app.run(debug=True)
