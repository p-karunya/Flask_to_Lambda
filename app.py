import argparse
from pathlib import Path
import boto3

parser = argparse.ArgumentParser()
parser.add_argument('path', help='The path to main flask directory')

session = boto3.Session()
creds = session.get_credentials()
s3 = session.client('s3')

print(s3.list_buckets())
