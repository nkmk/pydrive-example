import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

f_folder = drive.CreateFile({'title': 'new_folder',
                             'mimeType': 'application/vnd.google-apps.folder'})
print(f_folder)
# GoogleDriveFile({'title': 'new_folder', 'mimeType': 'application/vnd.google-apps.folder'})

f_folder.Upload()

pprint.pprint(f_folder)
# {'alternateLink': 'https://drive.google.com/drive/folders/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#  'appDataContents': False,
#  'capabilities': {'canCopy': False, 'canEdit': True},
#  'copyRequiresWriterPermission': False,
#  'copyable': False,
#  'createdDate': '2019-07-16T14:04:39.276Z',
#  'editable': True,
#  'embedLink': 'https://drive.google.com/embeddedfolderview?id=1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#  'etag': '"_sqIxUq0fTLFIA17mBQDotbHWsg/MTU2MzI4NTg3OTI3Ng"',
#  'explicitlyTrashed': False,
#  'iconLink': 'https://drive-thirdparty.googleusercontent.com/16/type/application/vnd.google-apps.folder+48',
#  'id': '1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
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
#  'lastViewedByMeDate': '2019-07-16T14:04:39.276Z',
#  'markedViewedByMeDate': '1970-01-01T00:00:00.000Z',
#  'mimeType': 'application/vnd.google-apps.folder',
#  'modifiedByMeDate': '2019-07-16T14:04:39.276Z',
#  'modifiedDate': '2019-07-16T14:04:39.276Z',
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
#               'selfLink': 'https://www.googleapis.com/drive/v2/files/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz/parents/0AAeKIFCqYN07Uk9PVA'}],
#  'quotaBytesUsed': '0',
#  'selfLink': 'https://www.googleapis.com/drive/v2/files/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz',
#  'shared': False,
#  'spaces': ['drive'],
#  'title': 'new_folder',
#  'userPermission': {'etag': '"_sqIxUq0fTLFIA17mBQDotbHWsg/38oVvgHkBS5xDYba_gRDJx2lqsQ"',
#                     'id': 'me',
#                     'kind': 'drive#permission',
#                     'role': 'owner',
#                     'selfLink': 'https://www.googleapis.com/drive/v2/files/1dQT4GYkl2zHDP_7yXYcKuomX6XggF9Cz/permissions/me',
#                     'type': 'user'},
#  'version': '1',
#  'writersCanShare': True}

f_folder = drive.CreateFile()

# f_folder.SetContentFile('src')
# IsADirectoryError: [Errno 21] Is a directory: 'src'
