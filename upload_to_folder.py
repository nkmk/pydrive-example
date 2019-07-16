import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

folder_id = drive.ListFile({'q': 'title = "new_folder"'}).GetList()[0]['id']

f = drive.CreateFile({"parents": [{"id": folder_id}]})
f.SetContentFile('src/lena.jpg')
f['title'] = 'lena.jpg'
f.Upload()

print(type(f['parents']))
# <class 'list'>

pprint.pprint(f['parents'])
# [{'id': '1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#   'isRoot': False,
#   'kind': 'drive#parentReference',
#   'parentLink': 'https://www.googleapis.com/drive/v2/files/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#   'selfLink': 'https://www.googleapis.com/drive/v2/files/1nUWOO8QWyqE13PMW4fzemKF8gcsOCXkJ/parents/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz'}]

print(f['parents'][0]['id'] == folder_id)
# True
