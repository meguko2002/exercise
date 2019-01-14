import shutil,os
print(os.getcwd())
for n in range(1 , 10):
    shutil.copy('fileEdit/201rawdata.csv',  'fileEdit/{}rawdata.csv'.format(100+n))