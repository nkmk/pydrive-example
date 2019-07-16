import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile({'q': 'title contains "file1" and trashed = false'}).GetList()

for f in file_list:
    print(f['title'], '  \t', f['id'])
# file1   	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo
# file111   	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech
# file12   	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11   	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9

dst_dir = 'dst'

for f in file_list:
    f.GetContentFile(os.path.join(dst_dir, f['title']))

for f in file_list:
    f['title'] = 'XXX_' + f['title']
    f.Upload()

for f in file_list:
    print(f['title'], '  \t', f['id'])
# XXX_file1   	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo
# XXX_file111   	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech
# XXX_file12   	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# XXX_file11   	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9

for f in file_list:
    f['title'] = f['title'][4:]
    f.Upload()

for f in file_list:
    print(f['title'], '  \t', f['id'])
# file1   	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo
# file111   	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech
# file12   	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11   	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9
