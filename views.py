from models import *
from app import app
from flask import render_template, redirect, url_for, request, flash, Response
from flask_login import login_required, login_user, logout_user
from forms import *
from app import db, generate_frames

#landing page
@app.route("/")
def index():
    return render_template('index.html')

#profile displays the profile of the asssociated user
@app.route("/user/<int:userid>")
def profile(userid):
    user = User.query.get(userid)
    return render_template('profile.html', user=user)

# list of exercises
@app.route("/exercises")
def exercises():
    exercise_all = Exercise.query.all()
    idx = 0
    exercise_lists = []
    while(idx<len(exercise_all)):
        elist = []
        cnt = 0
        while(idx<len(exercise_all) and cnt < 3):
            elist.append(exercise_all[idx])
            cnt+=1
            idx+=1
        exercise_lists.append(elist)
    return render_template('exercises.html', exercise_lists=exercise_lists)

#progress displays the live pose analysis page
@app.route("/progress/<string:title>")
def progress(title):
    return render_template('progress.html', exercise=Exercise.query.get(title))

#processImage feeds the url passed in the query string to machine learning model
@app.route("/image/submit/<path:url>")
def processImage(url):
    #pass url to the machine learning
    pass

#login view
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        form = LoginForm(request.form)
        try:
            if form.validate_on_submit():
                login_user(User.query.get(form.username.data))
                flash('Logged in successfully.')
                return redirect(url_for('index'))
        except ValidationError:
            return render_template('login.html', form=LoginForm())
    return render_template('login.html', form=LoginForm())

#logout view
@app.route("/logout", methods=["GET"])
@login_required
def logout():
    #log user out
    logout_user()
    #redirect to index page
    return redirect(url_for('index'))

#register view
@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(id=form.id.data, email=form.email.data, password=form.password.data, authenticated=False)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=RegisterForm())

@app.route('/video/<string:exercise>')
def video(exercise):
    return Response(generate_frames(exercise), mimetype='multipart/x-mixed-replace; boundary=frame')

