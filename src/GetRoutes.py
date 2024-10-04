import os 
import sys
from pathlib import Path
from typing import TypedDict

class route_id(TypedDict):
        name: str
        sourcecode: str
        route: str

def getRoutes(FlaskDir):
    ROUTES = []
    PATH = Path(FlaskDir)

    if not PATH.exists():
        print("Path does not exist")
        raise FileNotFoundError("The directory does not exist")
    
    APP_PATH = findApp(PATH)

    with open(APP_PATH, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "@app.route" in line:
                new_route = route_id(line.split("(")[1].split(")")[0], line, lines[lines.index(line)+1].split("def ")[1].split("(")[0])
                
        
def findApp(PATH: Path):
    for root, dirs, files in os.walk(PATH):
        for file in files:
            if file == "app.py":
                return os.path.join(root, file)
            else:
                raise FileNotFoundError("app.py not found in the directory")