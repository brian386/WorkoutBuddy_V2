from app import db
from models import Exercise

exercises = [['dumbbell', 'An exercise'],
['pushup', 'An exercise'],
['squat', 'An exercise'],
['lunges', 'An exercise'],
['hip thrust', 'An exercise'],
['sit up', 'An exercise'],
]

for i in range(len(exercises)):
    db.session.add(Exercise(id=exercises[i][0], description=exercises[i][1], icon="../static/"+exercises[i][0]+".png"))
db.session.commit()