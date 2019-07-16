import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_id = drive.ListFile({'q': 'title = "lena.jpg"'}).GetList()[0]['id']

f = drive.CreateFile({'id': file_id})
print(type(f))
# <class 'pydrive.files.GoogleDriveFile'>

print(f)
# GoogleDriveFile({'id': '1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS'})

f.FetchMetadata()
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
#  'etag': '"_sqIxUq0fTLFIA17mBQDotbHWsg/MTU2MzI4NTE0MzkwNA"',
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
#  'lastViewedByMeDate': '2019-07-16T13:52:23.904Z',
#  'markedViewedByMeDate': '1970-01-01T00:00:00.000Z',
#  'md5Checksum': '18f790b9a2e45f9d7e37174df7714249',
#  'mimeType': 'image/jpeg',
#  'modifiedByMeDate': '2019-07-16T13:52:23.904Z',
#  'modifiedDate': '2019-07-16T13:52:23.904Z',
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
#  'thumbnailLink': 'https://lh3.googleusercontent.com/q8dgtrwulazHkBlUjw2n6H7b5ooUFlypnlz8Z6-ZD_pOvd_arSA-Jl4T-LjTzeHePac7fM6zv9M=s220',
#  'title': 'lena.jpg',
#  'userPermission': {'etag': '"_sqIxUq0fTLFIA17mBQDotbHWsg/d98zwIsA2bB9SfEk4Agv9C_CkuY"',
#                     'id': 'me',
#                     'kind': 'drive#permission',
#                     'role': 'owner',
#                     'selfLink': 'https://www.googleapis.com/drive/v2/files/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/permissions/me',
#                     'type': 'user'},
#  'version': '5',
#  'webContentLink': 'https://drive.google.com/uc?id=1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS&export=download',
#  'writersCanShare': True}

print(f['title'])
# lena.jpg

print(f['mimeType'])
# image/jpeg

print(f['fileSize'])
# 32468

print(f['parents'][0]['id'])
# 0AAeKIFCqYN07Uk9PVA

f = drive.CreateFile({'id': file_id})
print(f)
# GoogleDriveFile({'id': '1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS'})

print(f['title'])
# lena.jpg

print(f)
# GoogleDriveFile({'id': '1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS', 'kind': 'drive#file', 'etag': '"_sqIxUq0fTLFIA17mBQDotbHWsg/MTU2MzI4NTE0MzkwNA"', 'selfLink': 'https://www.googleapis.com/drive/v2/files/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS', 'webContentLink': 'https://drive.google.com/uc?id=1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS&export=download', 'alternateLink': 'https://drive.google.com/file/d/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/view?usp=drivesdk', 'embedLink': 'https://drive.google.com/file/d/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/preview?usp=drivesdk', 'iconLink': 'https://drive-thirdparty.googleusercontent.com/16/type/image/jpeg', 'thumbnailLink': 'https://lh3.googleusercontent.com/m2YVjD253FpwFFiz4ekc4Il6KIhP3LE1drWmH6zaJgWTKLDvVABj0ix8qIZmKunwEBR9U6yaKkc=s220', 'title': 'lena.jpg', 'mimeType': 'image/jpeg', 'labels': {'starred': False, 'hidden': False, 'trashed': False, 'restricted': False, 'viewed': True}, 'copyRequiresWriterPermission': False, 'createdDate': '2019-07-16T13:42:18.959Z', 'modifiedDate': '2019-07-16T13:52:23.904Z', 'modifiedByMeDate': '2019-07-16T13:52:23.904Z', 'lastViewedByMeDate': '2019-07-16T13:52:23.904Z', 'markedViewedByMeDate': '1970-01-01T00:00:00.000Z', 'version': '5', 'parents': [{'kind': 'drive#parentReference', 'id': '0AAeKIFCqYN07Uk9PVA', 'selfLink': 'https://www.googleapis.com/drive/v2/files/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/parents/0AAeKIFCqYN07Uk9PVA', 'parentLink': 'https://www.googleapis.com/drive/v2/files/0AAeKIFCqYN07Uk9PVA', 'isRoot': True}], 'downloadUrl': 'https://doc-14-2c-docs.googleusercontent.com/docs/securesc/dau8ajrf53dp30a065bvma64rthbbkv8/a79cnfgqkdr0hhjgseunhbajkeurcjgk/1563278400000/15529215658844670952/15529215658844670952/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS?e=download&gd=true', 'userPermission': {'kind': 'drive#permission', 'etag': '"_sqIxUq0fTLFIA17mBQDotbHWsg/d98zwIsA2bB9SfEk4Agv9C_CkuY"', 'id': 'me', 'selfLink': 'https://www.googleapis.com/drive/v2/files/1urYj2HbvV6kNfYsT8A-2PsmEjdiR2nZS/permissions/me', 'role': 'owner', 'type': 'user'}, 'originalFilename': 'lena.jpg', 'fileExtension': 'jpg', 'md5Checksum': '18f790b9a2e45f9d7e37174df7714249', 'fileSize': '32468', 'quotaBytesUsed': '32468', 'ownerNames': ['nkmk on'], 'owners': [{'kind': 'drive#user', 'displayName': 'nkmk on', 'isAuthenticatedUser': True, 'permissionId': '15529215658844670952', 'emailAddress': 'nkmk.on@gmail.com'}], 'lastModifyingUserName': 'nkmk on', 'lastModifyingUser': {'kind': 'drive#user', 'displayName': 'nkmk on', 'isAuthenticatedUser': True, 'permissionId': '15529215658844670952', 'emailAddress': 'nkmk.on@gmail.com'}, 'capabilities': {'canCopy': True, 'canEdit': True}, 'editable': True, 'copyable': True, 'writersCanShare': True, 'shared': False, 'explicitlyTrashed': False, 'appDataContents': False, 'headRevisionId': '0BweKIFCqYN07TDJNRXhEUll4cDJ2S3MySGJtTG1sc0pvSFkwPQ', 'imageMediaMetadata': {'width': 400, 'height': 225, 'rotation': 0}, 'spaces': ['drive']})

f['title'] = 'lena_new.jpg'
f.Upload()

print(f['title'])
# lena_new.jpg

f['fileSize'] = '100'
f.Upload()

print(f['fileSize'])
# 32468

f = drive.CreateFile({'id': file_id})
f['title'] = 'lena.jpg'
f.Upload()

print(f['title'])
# lena_new.jpg

f = drive.CreateFile({'id': file_id})
f.FetchMetadata()
f['title'] = 'lena.jpg'
f.Upload()

print(f['title'])
# lena.jpg
