import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_id = drive.ListFile({'q': 'title = "lena.jpg"'}).GetList()[0]['id']

f = drive.CreateFile({'id': file_id})
f.FetchMetadata()
pprint.pprint(f['parents'])
# [{'id': '1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#   'isRoot': False,
#   'kind': 'drive#parentReference',
#   'parentLink': 'https://www.googleapis.com/drive/v2/files/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#   'selfLink': 'https://www.googleapis.com/drive/v2/files/1nUWOO8QWyqE13PMW4fzemKF8gcsOCXkJ/parents/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz'}]

f['parents'] = [{'id': 'root'}]
f.Upload()
pprint.pprint(f['parents'])
# [{'id': '0AAeKIFCqYN07Uk9PVA',
#   'isRoot': True,
#   'kind': 'drive#parentReference',
#   'parentLink': 'https://www.googleapis.com/drive/v2/files/0AAeKIFCqYN07Uk9PVA',
#   'selfLink': 'https://www.googleapis.com/drive/v2/files/1nUWOO8QWyqE13PMW4fzemKF8gcsOCXkJ/parents/0AAeKIFCqYN07Uk9PVA'}]

folder_id = drive.ListFile({'q': 'title = "new_folder"'}).GetList()[0]['id']

f['parents'] = [{'id': folder_id}]
f.Upload()
pprint.pprint(f['parents'])
# [{'id': '1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#   'isRoot': False,
#   'kind': 'drive#parentReference',
#   'parentLink': 'https://www.googleapis.com/drive/v2/files/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#   'selfLink': 'https://www.googleapis.com/drive/v2/files/1nUWOO8QWyqE13PMW4fzemKF8gcsOCXkJ/parents/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz'}]
