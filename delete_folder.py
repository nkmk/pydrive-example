import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_id = drive.ListFile({'q': 'title = "lena.jpg"'}).GetList()[0]['id']

f_file = drive.CreateFile({'id': file_id})
pprint.pprint(f_file['parents'])
# [{'id': '1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#   'isRoot': False,
#   'kind': 'drive#parentReference',
#   'parentLink': 'https://www.googleapis.com/drive/v2/files/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#   'selfLink': 'https://www.googleapis.com/drive/v2/files/1nUWOO8QWyqE13PMW4fzemKF8gcsOCXkJ/parents/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz'}]

f_folder = drive.CreateFile({'id': f_file['parents'][0]['id']})

f_folder.Trash()

f_folder.FetchMetadata()
print(f_folder['labels']['trashed'])
# True

print(f_folder['explicitlyTrashed'])
# True

f_file.FetchMetadata()
print(f_file['labels']['trashed'])
# False

print(f_file['explicitlyTrashed'])
# False

f_folder.UnTrash()

f_folder.FetchMetadata()
print(f_folder['labels']['trashed'])
# False

print(f_folder['explicitlyTrashed'])
# False

f_file.FetchMetadata()
print(f_file['labels']['trashed'])
# False

print(f_file['explicitlyTrashed'])
# False

f_folder.Delete()

# f_folder.FetchMetadata()
# ApiRequestError: <HttpError 404 when requesting https://www.googleapis.com/drive/v2/files/144fD0jujJEyCdaM5jv8Fgp-czXLZNfBe?alt=json returned "File not found: 144fD0jujJEyCdaM5jv8Fgp-czXLZNfBe">

# f_file.FetchMetadata()
# ApiRequestError: <HttpError 404 when requesting https://www.googleapis.com/drive/v2/files/1-j36c901moQ3gsTXwnvwLK3lRRKhS1CT?alt=json returned "File not found: 1-j36c901moQ3gsTXwnvwLK3lRRKhS1CT">
