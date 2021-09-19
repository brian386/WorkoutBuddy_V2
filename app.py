from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5f272ff5e3251c36a77940bc'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

#Models
from models import *

#forms 
from forms import *

#views
from views import *

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)