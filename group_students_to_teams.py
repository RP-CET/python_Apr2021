import os
import shutil

# replace the student ids below with your student ids
t1 = [19010111,19011222,19013333,19041111]
t2 = [19010111,19011222,19013333,19041111]
t3 = [19010111,19011222,19013333,19041111]
t4 = [19010111,19011222,19013333,19041111]
t5 = [19010111,19011222,19013333,19041111]

students = [t1, t2, t3, t4, t5]

files = os.listdir('.')

# remove empty folder
for afile in files:
    # check that the file is a directory
    if os.path.isdir(afile):
        # remove directory, only empty directory can be removed
        try:
            os.rmdir(afile)
        except OSError:
            pass


# create team folder
for i in range(1, 6):
    filename = "Team " + str(i)
    if not os.path.exists (filename):
        os.mkdir(filename)
        
# copy folder
count = 1
for tt in students:
    for t in tt:
        t = str(t)
        
        for f in files:
            if f.find(t) != -1:
                t = f
        
        if os.path.exists(t):
            desc = 'Team ' + str(count) + '/' + t + '/'
            print(desc)
            if not os.path.exists(desc):
                shutil.copytree(t,desc)
        
        # remove student folder
        if os.path.exists(t):
            shutil.rmtree(t)
    
    count+=1
            
            
            

