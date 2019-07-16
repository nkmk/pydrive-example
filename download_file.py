import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_id = drive.ListFile({'q': 'title = "lena.jpg"'}).GetList()[0]['id']

f = drive.CreateFile({'id': file_id})
f.GetContentFile('dst/download_img.jpg')

f = drive.CreateFile({'id': file_id})
f.GetContentFile(os.path.join('dst', f['title']))
