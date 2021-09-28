# WorkoutBuddy_V2

## Installation
`pip install -r requirements.txt`

## Inspiration
Our inspiration came from the development of Artificial Intelligence. We hope to use auto detection in a unique way and apply it to everyday situations.

In order to live a healthy lifestyle, exercises are necessary. Many people tend to set a certain goal for themselves during exercise, such as doing 20 push ups, 10 squads, 15 lunges, etc. However, sometimes it is very hard to keep track, especially when you are focusing more on the exercise itself and not the counting part. Therefore, a program that can count for you becomes the best choice. What's more, with the use of computer programs, people can also gain help to ignore the exercises that do not meet the standard (such as lunges that are way too high, push-ups that don't make a low enough angle with the ground).

With these two components in mind, the idea of Workout Buddy fully flourished. Further, when we looked more in depth, we realized we could connect front end and back end, creating a functional web app helping people to organize workouts.

## What it does
WorkoutBuddy helps you optimize your health and fitness by making sure you are using good form with your exercises and meeting your goals that you set out for your fitness regimen. It uses machine learning to take a video of your workout and detect the different exercises you are doing (lunges, squats, just to name a few). The app will only count reps that are in good form to reduce the risk of injury and ensure a proper workout. For every exercise, the user can set a goal for the number of repetitions they would like to accomplish during the session.

## How we built it
First, we designed a mockup of the website on Figma as a general guide to our website’s design, then we used Flask to construct that frontend and materialcss to style the website. By Using Flask, we were able to connect the front-end to the back-end with little fuss. A SQLite database was used to store user information and exercise descriptions.

We used OpenCV and MediaPipe to do the pose detection. We calculated angles between certain keypoints to ensure that the exercises are done correctly.

## Challenges we ran into
This hackathon we took it upon ourselves to challenge ourselves and work with tools and technologies we had little familiarity with, so we had to deal with a lot of beginner mistakes, as well as deadly errors that hindered our progress.

This was our first time working with MediaPipe pose detection, and it was challenging to learn how to do what we wanted to do. Further, this was our first time working with tools like flask, so designing the website was an intimidating task. Additionally, we had not previously worked with tools like databases, so we received a lot of friction trying to implement that feature.

The common theme with all of our challenges was an unfamiliarity with technology, however, another commonality is the fact that we persevere through all of our issues by collaborating with and consulting one another to resolve issues, or simply through perseverance and grit.

## Accomplishments that we're proud of
We’re proud of the fact that we have a functioning and polished website that implements every feature, and more, that we planned for. We take much pride in the fact that our app can correctly recognize and count a user’s exercises, as well as the fact that we built a web app that runs the program. More holistically, we’re proud of the fact that we implemented a programming process that allowed us to work on individual components (Front-end, Back-end, Database) and were able to connect them seamlessly. The organization and streamlined process of our design process was leaps and bounds above any projects we’ve worked on before.

## What we learned
We learned how to implement pose detection using the MediaPipe library and how to access the camera using OpenCV. We also learned how to use Flask to process HTTP requests and query a database for exercise and user information, and how it can be used to dynamically generate HTML content.

## What's next for Workout Buddy
All too often, people set exercise goals for themselves but don’t follow through on them. To help users keep track of their progress, we plan to add new features that will allow users to set daily exercise goals on their profile page, and the website would count their exercises through its pose detection functionality and let them know if their goal has been met for the day.

One of the greatest pressures, or rather motivators, to accomplish a goal is by involving another person in your goal. Therefore, we plan to leverage this effect by making the app social - allowing users to have friends and view their progress, as well as challenge users to meet their goals. This social network of exercise can accelerate our rep-counting web-app into a platform for health and fitness.
