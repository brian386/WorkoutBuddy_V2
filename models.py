from app import db

class User(db.Model):
    #meta information
    id = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)
    authenticated = db.Column(db.Boolean, default=True)
    # Goals
    goals = db.relationship('Goal', backref='user', lazy=True)
    # Methods
    def __repr__(self):
        return self.id
    def is_authenticated(self):
        return self.authenticated
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self.id

class Exercise(db.Model):
    id = db.Column(db.String(100), unique=True, nullable=False, primary_key=True)
    description = db.Column(db.Text, nullable=False)
    users = db.relationship('Goal', backref='exercise', lazy=True)
    icon = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return self.id

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '%s: %s' % User.query.get(self.person_id) % Exercise.query.get(self.exercise_id)
