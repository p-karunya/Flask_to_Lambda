import os 
import sys
from pathlib import Path

def getRoutes(FlaskDir):
    PATH = Path(FlaskDir)
    print("yay")
    if not PATH.exists():
        print("Path does not exist")
        raise FileNotFoundError("The directory does not exist")
    