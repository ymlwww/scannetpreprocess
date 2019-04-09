import re
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
f = open("scene0000_00.txt")     
line = f.readline()        
while line:
    if "numColorFrames" in line: 
        framenum = re.findall("\d+",line)[0]
        print framenum
    line = f.readline()
f.close()
initvalue=0
successnum=0
clip={}
for i in range(int(framenum)):
    I = mpimg.imread('./label/'+str(i)+'.png')
    colordict={}
    [row,col]=I.shape
    ans={}
    for i in range(row):
        for j in range(col):
            if colordict.has_key(I[i,j]):
                colordict[I[i,j]]=colordict[I[i,j]]+1;
            else:
                colordict[I[i,j]]=1
    for k,v in colordict.items():
        rate=1.0*v/(row*col)
        if rate>0.2:
            ans[k]=v
    if successnum==0:
        for k,v in ans.items():
            initvalue=k
            successnum==1
            break
    else:
        if ans.has_key(initvalue):
            successnum=successnum+1
        else:
            if successnum>49:
                clip[initvalue]=[i,successnum]
            initvalue=0
            successnum=0
print clip