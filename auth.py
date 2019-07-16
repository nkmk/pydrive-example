import os

from pydrive.auth import GoogleAuth

os.chdir(os.path.dirname(os.path.abspath(__file__)))

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
