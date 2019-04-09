
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#I = mpimg.imread('./scene0000_00_2d-label-filt/label-filt/380.png')
for i in range(10):
    I = mpimg.imread('./label/'+str(i)+'.png')
    #I = mpimg.imread('./instance/1.png')
    #print I.shape
    #print I
    colordict={}
    [row,col]=I.shape
    ans={}
    #print row,col
    for i in range(row):
        for j in range(col):
            #print str(int(I[i,j]*1000000))
            #colordict[str(int(I[i,j]*1000000))]=[row,col]
            if colordict.has_key(I[i,j]):
                colordict[I[i,j]]=colordict[I[i,j]]+1;
            else:
                colordict[I[i,j]]=1
    for k,v in colordict.items():
        rate=1.0*v/(row*col)
        if rate>0.2:
            ans[k]=v
    print ans
#I.getcolors()
#plt.imshow(I)
#plt.show()