import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

folder_id = drive.ListFile({'q': "title = 'dir1'"}).GetList()[0]['id']

file_list = drive.ListFile({'q': '"{}" in parents and trashed = false'.format(folder_id)}).GetList()

print(type(file_list))
# <class 'list'>

print(type(file_list[0]))
# <class 'pydrive.files.GoogleDriveFile'>

for f in file_list:
    print(f['title'], ' \t', f['id'])
# subdir1  	 1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck
# file12  	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11  	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9

def get_list_recursively(parent_id, l=None):
    if l is None:
        l = []

    file_list = drive.ListFile({'q': '"{}" in parents and trashed = false'.format(parent_id)}).GetList()
    l += file_list

    for f in file_list:
        if f['mimeType'] == 'application/vnd.google-apps.folder':
            get_list_recursively(f['id'], l)

    return l

for f in get_list_recursively(folder_id):
    print(f['title'], ' \t', f['id'])
# subdir1  	 1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck
# file12  	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11  	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9
# file111  	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech

def get_list_file_recursively(parent_id, l=None):
    if l is None:
        l = []

    file_list = drive.ListFile({'q': '"{}" in parents and trashed = false'.format(parent_id)}).GetList()
    l += [f for f in file_list if f['mimeType'] != 'application/vnd.google-apps.folder']

    for f in file_list:
        if f['mimeType'] == 'application/vnd.google-apps.folder':
            get_list_file_recursively(f['id'], l)

    return l

for f in get_list_file_recursively(folder_id):
    print(f['title'], '   \t', f['id'])
# file12    	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11    	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9
# file111    	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech

for f in get_list_file_recursively(folder_id):
    f.GetContentFile(os.path.join('dst', f['title']))

def download_file_recursively(parent_id, dst_dir):
    os.makedirs(dst_dir, exist_ok=True)

    file_list = drive.ListFile({'q': '"{}" in parents and trashed = false'.format(parent_id)}).GetList()

    for f in file_list:
        if f['mimeType'] == 'application/vnd.google-apps.folder':
            download_file_recursively(f['id'], os.path.join(dst_dir, f['title']))
        else:
            dst_path = os.path.join(dst_dir, f['title'])
            f.GetContentFile(dst_path)
            print('Download {} to {}'.format(f['title'], dst_path))

download_file_recursively('root', 'dst/root')
# Download file21 to dst/root/dir2/file21
# Download file111 to dst/root/dir1/subdir1/file111
# Download file12 to dst/root/dir1/file12
# Download file11 to dst/root/dir1/file11
# Download file2 to dst/root/file2
# Download file1 to dst/root/file1
