from flask import Flask, render_template, Response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

import cv2
import mediapipe as mp
import math
import os
from pose_detection import *
from exercises import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '5f272ff5e3251c36a77940bc'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)

csrf = CSRFProtect(app)

#if os.environ.get('WERKZEUG_RUN_MAIN') or Flask.debug is False:
camera = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def generate_frames(exercise):
    detector = pose_detector()
    cur_session = {'reps': 0, 'up': True}
    while True:
        success, frame_0 = camera.read()
        if success == True:
            frame_0 = detector.find_pose(frame_0)
            success,buffer = cv2.imencode('.jpg', frame_0)
            frame = buffer.tobytes()

            lmList = detector.find_position(frame_0)
            if len(lmList) != 0:
                if exercise == "dumbbell":
                    count_bicep_curl(cur_session, detector, lmList)
                elif exercise == "sit up":
                    count_situp(cur_session, detector, lmList)
                elif exercise == "squat":
                    count_squat(cur_session, detector, lmList)
                elif exercise == "hip thrust":
                    count_hip_thrust(cur_session, detector, lmList)
                elif exercise == "pushup":
                    count_push_ups(cur_session, detector, lmList)
                elif exercise == "lunges":
                    count_lunges(cur_session, detector, lmList)
                print(math.floor(cur_session['reps']))
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.rectangle(frame_0, (0,375),(150,500), (0,0,0), -1)
            cv2.putText(frame_0, '{}'.format(math.floor(cur_session['reps'])), (10, 450), font, 3, (255, 255, 255), 2, cv2.LINE_AA)
            success,buffer = cv2.imencode('.jpg', frame_0)
            frame = buffer.tobytes()
            yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
            print("didn't work")
            break

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
    camera.release()
    cv2.destroyAllWindows()