import argparse
from pathlib import Path
import boto3
from src.GetRoutes import getRoutes

# Check if AWS credentials are available if not exit (will have to change this to use the credentials from the CLI)
session = boto3.Session()
creds = session.get_credentials()
if not creds:
    print("No AWS credentials found")
    

# Get the path to the main flask directory
parser = argparse.ArgumentParser()
parser.add_argument('path', help='The path to main flask directory')

getRoutes(parser.parse_args().path)


