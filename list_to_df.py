import pprint
import pandas as pd

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

l = [[f['title'], f['id'], f['parents'][0]['id'], f['mimeType'], f.get('fileSize')]
     for f in drive.ListFile().GetList()
     if len(f['parents'])]

pprint.pprint(l, width=200)
# [['file11', '15sy12U3d845pXjLaEWww4VLO9Vs7C4J9', '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1', 'application/octet-stream', '0'],
#  ['file12', '1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx', '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1', 'application/octet-stream', '0'],
#  ['file111', '1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech', '1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck', 'application/octet-stream', '0'],
#  ['file1', '1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo', '0AAeKIFCqYN07Uk9PVA', 'application/octet-stream', '0'],
#  ['file21', '1o-pFt-9Hrj_z3FmlsQfa8duo_ZfuEh5S', '1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9', 'application/octet-stream', '0'],
#  ['dir2', '1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9', '0AAeKIFCqYN07Uk9PVA', 'application/vnd.google-apps.folder', None],
#  ['subdir1', '1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck', '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1', 'application/vnd.google-apps.folder', None],
#  ['dir1', '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1', '0AAeKIFCqYN07Uk9PVA', 'application/vnd.google-apps.folder', None],
#  ['file2', '1HaHLB19oU_he6LI_6mkQsPr9uH_JK_oz', '0AAeKIFCqYN07Uk9PVA', 'application/octet-stream', '0']]

df = pd.DataFrame(l, columns=['title', 'id', 'parents_id', 'mimeType', 'fileSize'])
print(df)
#      title                                 id  \
# 0   file11  15sy12U3d845pXjLaEWww4VLO9Vs7C4J9   
# 1   file12  1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx   
# 2  file111  1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech   
# 3    file1  1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo   
# 4   file21  1o-pFt-9Hrj_z3FmlsQfa8duo_ZfuEh5S   
# 5     dir2  1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9   
# 6  subdir1  1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck   
# 7     dir1  1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1   
# 8    file2  1HaHLB19oU_he6LI_6mkQsPr9uH_JK_oz   
# 
#                           parents_id                            mimeType  \
# 0  1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1            application/octet-stream   
# 1  1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1            application/octet-stream   
# 2  1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck            application/octet-stream   
# 3                0AAeKIFCqYN07Uk9PVA            application/octet-stream   
# 4  1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9            application/octet-stream   
# 5                0AAeKIFCqYN07Uk9PVA  application/vnd.google-apps.folder   
# 6  1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1  application/vnd.google-apps.folder   
# 7                0AAeKIFCqYN07Uk9PVA  application/vnd.google-apps.folder   
# 8                0AAeKIFCqYN07Uk9PVA            application/octet-stream   
# 
#   fileSize  
# 0        0  
# 1        0  
# 2        0  
# 3        0  
# 4        0  
# 5     None  
# 6     None  
# 7     None  
# 8        0  

df.to_csv('dst/use_pandas.csv', index=False)

df_folder = df.query('mimeType == "application/vnd.google-apps.folder"')

d_id_title = dict(zip(df_folder['id'], df_folder['title']))
d_id_parents_id = dict(zip(df_folder['id'], df_folder['parents_id']))

pprint.pprint(d_id_title)
# {'1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck': 'subdir1',
#  '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1': 'dir1',
#  '1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9': 'dir2'}

pprint.pprint(d_id_parents_id)
# {'1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck': '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1',
#  '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1': '0AAeKIFCqYN07Uk9PVA',
#  '1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9': '0AAeKIFCqYN07Uk9PVA'}

def get_parents_path(current_id, root_id, sep='/'):
    l = []
    while current_id != root_id:
        if current_id not in d_id_title.keys():
            return None
        l.append(d_id_title[current_id])
        current_id = d_id_parents_id[current_id]
    return sep.join(reversed(l))

root_id = drive.ListFile({'q': '"root" in parents'}).GetList()[0]['parents'][0]['id']

d_id_path = {i: get_parents_path(i, root_id) for i in df_folder['id']}
d_id_path[root_id] = ''

pprint.pprint(d_id_path)
# {'0AAeKIFCqYN07Uk9PVA': '',
#  '1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck': 'dir1/subdir1',
#  '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1': 'dir1',
#  '1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9': 'dir2'}

df['parents_path'] = df['parents_id'].map(d_id_path)
df_result = df.sort_values('parents_path').reset_index(drop=True)
print(df_result[['title', 'parents_path']])
#      title  parents_path
# 0    file1              
# 1     dir2              
# 2     dir1              
# 3    file2              
# 4   file11          dir1
# 5   file12          dir1
# 6  subdir1          dir1
# 7  file111  dir1/subdir1
# 8   file21          dir2
