from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_id = drive.ListFile({'q': 'title = "lena.jpg"'}).GetList()[0]['id']

f = drive.CreateFile({'id': file_id})
print(f['labels']['trashed'])
# False

f.Trash()
print(f['labels']['trashed'])
# True

f.UnTrash()
print(f['labels']['trashed'])
# False

f.Delete()

# f.FetchMetadata()
# ApiRequestError: <HttpError 404 when requesting https://www.googleapis.com/drive/v2/files/1AT2UizaLXFXiAcwGMGPqcBop7-jmGiTf?alt=json returned "File not found: 1AT2UizaLXFXiAcwGMGPqcBop7-jmGiTf">

file_id = drive.ListFile({'q': 'title = "new_file.txt"'}).GetList()[0]['id']
f = drive.CreateFile({'id': file_id})
f.Delete()
