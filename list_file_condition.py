from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

for f in drive.ListFile({'q': 'title contains "file1"'}).GetList():
    print(f['title'], '  \t', f['id'])
# file111   	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech
# file12   	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11   	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9
# file1   	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo

for f in drive.ListFile({'q': 'title contains "file1" and not "root" in parents'}).GetList():
    print(f['title'], '  \t', f['id'])
# file111   	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech
# file12   	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11   	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9

# 'title contains "file1"'
# "title contains 'file1'"
# 'title contains \'file1\''
# "title contains \"file1\""

for f in drive.ListFile({'q': 'mimeType = "application/vnd.google-apps.folder"'}).GetList():
    print(f['title'], '   \t', f['id'])
# dir2    	 1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9
# subdir1    	 1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck
# dir1    	 1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1

for f in drive.ListFile({'q': 'mimeType != "application/vnd.google-apps.folder"'}).GetList():
    print(f['title'], '  \t', f['id'])
# file21   	 1o-pFt-9Hrj_z3FmlsQfa8duo_ZfuEh5S
# file111   	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech
# file12   	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11   	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9
# file2   	 1HaHLB19oU_he6LI_6mkQsPr9uH_JK_oz
# file1   	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo

for f in drive.ListFile({'q': 'title = "file1"'}).GetList():
    print(f['title'], '  \t', f['id'])
# file1   	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo

for f in drive.ListFile({'q': 'title contains "file1"'}).GetList():
    print(f['title'], '  \t', f['id'])
# file111   	 1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech
# file12   	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11   	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9
# file1   	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo

for f in drive.ListFile({'q': 'title contains "11"'}).GetList():
    print(f['title'], '  \t', f['id'])

dir1_id = drive.ListFile({'q': 'title = "dir1"'}).GetList()[0]['id']

for f in drive.ListFile({'q': '"{}" in parents'.format(dir1_id)}).GetList():
    print(f['title'], '   \t', f['id'])
# subdir1    	 1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck
# file12    	 1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx
# file11    	 15sy12U3d845pXjLaEWww4VLO9Vs7C4J9

for f in drive.ListFile({'q': '"root" in parents'}).GetList():
    print(f['title'], '   \t', f['id'])
# dir2    	 1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9
# dir1    	 1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1
# file2    	 1HaHLB19oU_he6LI_6mkQsPr9uH_JK_oz
# file1    	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo

file1_id = drive.ListFile({'q': 'title = "file1"'}).GetList()[0]['id']
file1 = drive.CreateFile({'id': file1_id})
file1.Trash()

for f in drive.ListFile({'q': '"root" in parents'}).GetList():
    print(f['title'], '   \t', f['id'])
# file1    	 1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo
# dir2    	 1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9
# dir1    	 1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1
# file2    	 1HaHLB19oU_he6LI_6mkQsPr9uH_JK_oz

for f in drive.ListFile({'q': '"root" in parents and trashed = false'}).GetList():
    print(f['title'], '   \t', f['id'])
# dir2    	 1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9
# dir1    	 1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1
# file2    	 1HaHLB19oU_he6LI_6mkQsPr9uH_JK_oz

file1.UnTrash()
