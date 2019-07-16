import os
import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

print(type(drive))
# <class 'pydrive.drive.GoogleDrive'>

f = drive.CreateFile()
print(type(f))
# <class 'pydrive.files.GoogleDriveFile'>

print(f)
# GoogleDriveFile({})

f.SetContentFile('src/lena.jpg')
print(f)
# GoogleDriveFile({'title': 'src/lena.jpg', 'mimeType': 'image/jpeg'})

f['title'] = os.path.basename('src/lena.jpg')
print(f)
# GoogleDriveFile({'title': 'lena.jpg', 'mimeType': 'image/jpeg'})

f.Upload()

pprint.pprint(f)
# {'alternateLink': 'https://drive.google.com/file/d/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/view?usp=drivesdk',
#  'appDataContents': False,
#  'capabilities': {'canCopy': True, 'canEdit': True},
#  'copyRequiresWriterPermission': False,
#  'copyable': True,
#  'createdDate': '2019-07-16T13:42:18.959Z',
#  'downloadUrl': 'https://doc-14-2c-docs.googleusercontent.com/docs/securesc/dau8ajrf53dp30a065bvma64rthbbkv8/a79cnfgqkdr0hhjgseunhbajkeurcjgk/1563278400000/15529215658844670952/15529215658844670952/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS?e=download&gd=true',
#  'editable': True,
#  'embedLink': 'https://drive.google.com/file/d/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/preview?usp=drivesdk',
#  'etag': '"_sqIxUq0fTLFIA17mBQDotbHWsg/MTU2MzI4NDUzODk1OQ"',
#  'explicitlyTrashed': False,
#  'fileExtension': 'jpg',
#  'fileSize': '32468',
#  'headRevisionId': '0BweKIFCqYN07TDJNRXhEUll4cDJ2S3MySGJtTG1sc0pvSFkwPQ',
#  'iconLink': 'https://drive-thirdparty.googleusercontent.com/16/type/image/jpeg',
#  'id': '1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS',
#  'imageMediaMetadata': {'height': 225, 'rotation': 0, 'width': 400},
#  'kind': 'drive#file',
#  'labels': {'hidden': False,
#             'restricted': False,
#             'starred': False,
#             'trashed': False,
#             'viewed': True},
#  'lastModifyingUser': {'displayName': 'nkmk on',
#                        'emailAddress': 'nkmk.on@gmail.com',
#                        'isAuthenticatedUser': True,
#                        'kind': 'drive#user',
#                        'permissionId': '15529215658844670952'},
#  'lastModifyingUserName': 'nkmk on',
#  'lastViewedByMeDate': '2019-07-16T13:42:18.959Z',
#  'markedViewedByMeDate': '1970-01-01T00:00:00.000Z',
#  'md5Checksum': '18f790b9a2e45f9d7e37174df7714249',
#  'mimeType': 'image/jpeg',
#  'modifiedByMeDate': '2019-07-16T13:42:18.959Z',
#  'modifiedDate': '2019-07-16T13:42:18.959Z',
#  'originalFilename': 'lena.jpg',
#  'ownerNames': ['nkmk on'],
#  'owners': [{'displayName': 'nkmk on',
#              'emailAddress': 'nkmk.on@gmail.com',
#              'isAuthenticatedUser': True,
#              'kind': 'drive#user',
#              'permissionId': '15529215658844670952'}],
#  'parents': [{'id': '0AAeKIFCqYN07Uk9PVA',
#               'isRoot': True,
#               'kind': 'drive#parentReference',
#               'parentLink': 'https://www.googleapis.com/drive/v2/files/0AAeKIFCqYN07Uk9PVA',
#               'selfLink': 'https://www.googleapis.com/drive/v2/files/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/parents/0AAeKIFCqYN07Uk9PVA'}],
#  'quotaBytesUsed': '32468',
#  'selfLink': 'https://www.googleapis.com/drive/v2/files/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS',
#  'shared': False,
#  'spaces': ['drive'],
#  'thumbnailLink': 'https://lh3.googleusercontent.com/lyCvx5zSBVXNO7CIyQ3ISrb9UvqWWuTJJKUrRE9kJ-R_hdbZE-CBUdoE9V0Yz5wOlVG26i39BAU=s220',
#  'title': 'lena.jpg',
#  'userPermission': {'etag': '"_sqIxUq0fTLFIA17mBQDotbHWsg/d98zwIsA2bB9SfEk4Agv9C_CkuY"',
#                     'id': 'me',
#                     'kind': 'drive#permission',
#                     'role': 'owner',
#                     'selfLink': 'https://www.googleapis.com/drive/v2/files/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/permissions/me',
#                     'type': 'user'},
#  'version': '2',
#  'webContentLink': 'https://drive.google.com/uc?id=1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS&export=download',
#  'writersCanShare': True}

f_txt = drive.CreateFile({'title': 'new_file.txt'})
f_txt.SetContentString('new text')
print(f_txt)
# GoogleDriveFile({'title': 'new_file.txt', 'mimeType': 'text/plain'})

f_txt.Upload()
