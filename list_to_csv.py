import csv
import pprint

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

l = [[f['title'], f['id']] for f in drive.ListFile().GetList()]
pprint.pprint(l)
# [['file11', '15sy12U3d845pXjLaEWww4VLO9Vs7C4J9'],
#  ['file12', '1iv9UB1pi65MqfFmqYwBoz3AfZbKr2jLx'],
#  ['file111', '1bfc7jlDobxuoyZeF8CDyXlN66zl84Ech'],
#  ['file1', '1z1vv7Zd1k14JebVghq8NlVpLWmFhZybo'],
#  ['file21', '1o-pFt-9Hrj_z3FmlsQfa8duo_ZfuEh5S'],
#  ['dir2', '1UaNdnbqCKe2ALtZp6hirvCgZl7OVpTI9'],
#  ['subdir1', '1CpPdnFTdN6DWPz7VBM1pV-RMZfcbvzck'],
#  ['dir1', '1DX1YFUdbSAeIvuXVLoosAKY2eX27Q4Y1'],
#  ['file2', '1HaHLB19oU_he6LI_6mkQsPr9uH_JK_oz']]

l.insert(0, ['title', 'id'])

with open('dst/use_csv.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(l)
