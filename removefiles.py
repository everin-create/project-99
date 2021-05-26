import os
import shutil

path=input("Enter the path you desire to be organised")
days=input('Number of days old the file has to be.')

path=path+'/'
days=time.time(days)

if os.path.exists(path):
    list_of_files= os.walk(path)
    for file in list_of_files:
         path=os.path.join(path+'/'+file)
         ctime=os.stat(path).st_ctime
         return ctime
         if ctime>days:
             shutil.rmtree(path)

else:
    print('file not found')


