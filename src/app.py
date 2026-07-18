"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")

# In-memory activity database
activities = {
    "Chess Club": {
        "description": "Learn strategies and compete in chess tournaments",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Learn programming fundamentals and build software projects",
        "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Gym Class": {
        "description": "Physical education and sports activities",
        "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Practice drills and compete in interscholastic soccer matches",
        "schedule": "Tuesdays, Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 25,
        "participants": ["alex@mergington.edu", "mia@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Develop skills and play friendly basketball games",
        "schedule": "Wednesdays, Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 20,
        "participants": ["noah@mergington.edu", "chloe@mergington.edu"]
    },
    "Art Studio": {
        "description": "Explore painting, drawing, and mixed media art projects",
        "schedule": "Mondays and Wednesdays, 3:45 PM - 5:15 PM",
        "max_participants": 18,
        "participants": ["ava@mergington.edu", "liam@mergington.edu"]
    },
    "Drama Club": {
        "description": "Rehearse scenes and prepare performances for the school community",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["sophia@mergington.edu", "ethan@mergington.edu"]
    },
    "Debate Team": {
        "description": "Build public speaking and argumentation skills through competitive debate",
        "schedule": "Mondays, Wednesdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["isabella@mergington.edu", "mason@mergington.edu"]
    },
    "Science Club": {
        "description": "Conduct experiments and explore scientific topics in depth",
        "schedule": "Fridays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["sophia@mergington.edu", "lucas@mergington.edu"]
    }
}

# Additional activities
activities.update({
    "Tennis Club": {
        "description": "Practice tennis techniques and play matches",
        "schedule": "Mondays and Thursdays, 4:00 PM - 5:30 PM",
        "max_participants": 16,
        "participants": ["oliver@mergington.edu", "emma@mergington.edu"]
    },
    "Swimming Team": {
        "description": "Swim training and competitive swim meets",
        "schedule": "Tuesdays, Thursdays, 5:00 PM - 6:30 PM",
        "max_participants": 20,
        "participants": ["liam@mergington.edu", "ava@mergington.edu"]
    },
    "Photography Club": {
        "description": "Learn photography techniques and work on photo projects",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "noah@mergington.edu"]
    },
    "Ceramics Studio": {
        "description": "Explore pottery and ceramic art forms",
        "schedule": "Fridays, 3:45 PM - 5:15 PM",
        "max_participants": 12,
        "participants": ["mia@mergington.edu", "ethan@mergington.edu"]
    },
    "Math Club": {
        "description": "Tackle challenging math problems and prepare for competitions",
        "schedule": "Mondays, 3:30 PM - 4:30 PM",
        "max_participants": 20,
        "participants": ["sophia@mergington.edu", "mason@mergington.edu"]
    },
    "Robotics Club": {
        "description": "Design, build, and program robots for challenges",
        "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
        "max_participants": 15,
        "participants": ["lucas@mergington.edu", "chloe@mergington.edu"]
    }
})


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    # Get the specific activity
    activity = activities[activity_name]

    # Validate student is not already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Student already signed up for this activity")  

    # Add student
    activity["participants"].append(email)
    return {"message": f"Signed up {email} for {activity_name}"}
