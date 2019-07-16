from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)

file_list = drive.ListFile().GetList()

print(type(file_list))
# <class 'list'>

print(len(file_list))
# 9

print(type(file_list[0]))
# <class 'pydrive.files.GoogleDriveFile'>

for f in file_list:
    print(f['title'], '   \t', f['id'])
# file21    	 1hJ7WQDiZyefLCQsDBE8J5-Nz847Vp670
# dir2    	 1wmWf1fhJTgi3X1Y07t2T8KYm4GtYEgxP
# file111    	 1789K-xv4ereCSOKrDKiAQI5bBypjqtIB
# subdir1    	 1k154tW38rbXxj88fjV8IZVkgB3EZ7g2M
# file12    	 1QRndXjXG9p2MEnVuotGd-eCNE2vNpkfp
# file11    	 1nCotx1q3DEaRWQOqbPqbPS1rGMWXRt8q
# dir1    	 1qQEUlPaIiDR_WI3hNf25rXUCHrlZIK_y
# file2    	 1ewv3ht8J2T3oMFmBgpqeS8zWHyHJsEwg
# file1    	 1WY5-WfWxj-ovefoE1dzWEfzgt8wtfbwY

for f in drive.ListFile({'orderBy': 'title'}).GetList():
    print(f['title'], '   \t', f['id'])
# dir1    	 1qQEUlPaIiDR_WI3hNf25rXUCHrlZIK_y
# dir2    	 1wmWf1fhJTgi3X1Y07t2T8KYm4GtYEgxP
# file1    	 1WY5-WfWxj-ovefoE1dzWEfzgt8wtfbwY
# file11    	 1nCotx1q3DEaRWQOqbPqbPS1rGMWXRt8q
# file111    	 1789K-xv4ereCSOKrDKiAQI5bBypjqtIB
# file12    	 1QRndXjXG9p2MEnVuotGd-eCNE2vNpkfp
# file2    	 1ewv3ht8J2T3oMFmBgpqeS8zWHyHJsEwg
# file21    	 1hJ7WQDiZyefLCQsDBE8J5-Nz847Vp670
# subdir1    	 1k154tW38rbXxj88fjV8IZVkgB3EZ7g2M

for f in drive.ListFile({'orderBy': 'title desc'}).GetList():
    print(f['title'], '   \t', f['id'])
# subdir1    	 1k154tW38rbXxj88fjV8IZVkgB3EZ7g2M
# file21    	 1hJ7WQDiZyefLCQsDBE8J5-Nz847Vp670
# file2    	 1ewv3ht8J2T3oMFmBgpqeS8zWHyHJsEwg
# file12    	 1QRndXjXG9p2MEnVuotGd-eCNE2vNpkfp
# file111    	 1789K-xv4ereCSOKrDKiAQI5bBypjqtIB
# file11    	 1nCotx1q3DEaRWQOqbPqbPS1rGMWXRt8q
# file1    	 1WY5-WfWxj-ovefoE1dzWEfzgt8wtfbwY
# dir2    	 1wmWf1fhJTgi3X1Y07t2T8KYm4GtYEgxP
# dir1    	 1qQEUlPaIiDR_WI3hNf25rXUCHrlZIK_y

for i, f_list in enumerate(drive.ListFile({'maxResults': 3})):
    print('=====', 'page', i)
    for f in f_list:
        print(f['title'], '   \t', f['id'])
# ===== page 0
# file21    	 1hJ7WQDiZyefLCQsDBE8J5-Nz847Vp670
# dir2    	 1wmWf1fhJTgi3X1Y07t2T8KYm4GtYEgxP
# file111    	 1789K-xv4ereCSOKrDKiAQI5bBypjqtIB
# ===== page 1
# subdir1    	 1k154tW38rbXxj88fjV8IZVkgB3EZ7g2M
# file12    	 1QRndXjXG9p2MEnVuotGd-eCNE2vNpkfp
# file11    	 1nCotx1q3DEaRWQOqbPqbPS1rGMWXRt8q
# ===== page 2
# dir1    	 1qQEUlPaIiDR_WI3hNf25rXUCHrlZIK_y
# file2    	 1ewv3ht8J2T3oMFmBgpqeS8zWHyHJsEwg
# file1    	 1WY5-WfWxj-ovefoE1dzWEfzgt8wtfbwY

for f in drive.ListFile().GetList():
    print(f['title'], '   \t', f['id'])
# file21    	 1hJ7WQDiZyefLCQsDBE8J5-Nz847Vp670
# dir2    	 1wmWf1fhJTgi3X1Y07t2T8KYm4GtYEgxP
# file111    	 1789K-xv4ereCSOKrDKiAQI5bBypjqtIB
# subdir1    	 1k154tW38rbXxj88fjV8IZVkgB3EZ7g2M
# file12    	 1QRndXjXG9p2MEnVuotGd-eCNE2vNpkfp
# file11    	 1nCotx1q3DEaRWQOqbPqbPS1rGMWXRt8q
# dir1    	 1qQEUlPaIiDR_WI3hNf25rXUCHrlZIK_y
# file2    	 1ewv3ht8J2T3oMFmBgpqeS8zWHyHJsEwg
# file1    	 1WY5-WfWxj-ovefoE1dzWEfzgt8wtfbwY
