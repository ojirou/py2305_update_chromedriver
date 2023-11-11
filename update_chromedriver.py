import os
import datetime
import shutil
ZipPath=r'C:\\Users\\user\\Downloads\\chromedriver_win64.zip'
FilePath=r'C:\\Users\\user\\Downloads\\chromedriver.exe'
Dir=r'C:\\Users\\user\\Downloads'
DstDir1=r'C:\\Users\\user\\git\\py\\driver'
DstDir2=r'C:\\Users\\user\\git\\web_scraping\\driver'
DstDir3=r'C:\\Users\\user\\python\\web_scraping\\driver'
DstDirs=[DstDir1,DstDir2,DstDir3]
#shutil.unpack_archive(ZipPath, Dir)
today=datetime.date.today()
num=1
for DstDir in DstDirs:
    BkDir=DstDir+'\\version_used_until_{:%y%m%d}'.format(today)
    while os.path.exists(BkDir):
    	BkDir=DstDir+'\\version_used_until_{:%y%m%d}_{}'.format(today, num)
    	num+=1
    os.mkdir(BkDir)
    shutil.move(DstDir+'\\chromedriver.exe', BkDir)
    shutil.copy(FilePath, DstDir)