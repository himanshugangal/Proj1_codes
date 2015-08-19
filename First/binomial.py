from __future__ import division
import sys
import numpy as np
from pylab import *
import matplotlib.pyplot as plt
path1 = "/Users/himanshu/Documents/merge/CaMKII_sweep_"
path2 = "/Users/himanshu/Documents/merge/"
## number of runs"
n = 100 
Kin = sys.argv[1]
ca_peak = 39
pp2a_input = 22
no_input = 5
f = n
## Time and interval"
T = 10000
dt = 1
npnts = int(T/dt)
#AVERAGE = numpy.zeros((npnts))
Tk = 3500
stpt = int((T-Tk)/dt)
mul = int(Tk/dt)
d = []
avg = 0.0
a = []
b = []
avg1 = []
ofile_ampseed = open(path2 + "/" +  str(Kin) + "_" + str(ca_peak) + "_" + str(pp2a_input) + "_" + str(no_input) + 'Amp_vs_seed.txt','w')

for i in range(0,n):
	try:
		f1 = open(path1 + str(Kin) + "_" + str(ca_peak) + "_" + str(pp2a_input) + "_" + str(no_input) + "/" +  str(i) + "/AMPAR_data.txt","r+")
		b = f1.readlines()
		for j in b[0:]:a.append(float(j))
		for k in range(stpt,npnts):
			avg = avg + a[k]/mul
			
		avg1.append(avg)
		ofile_ampseed.write("{} {}\n".format(avg, i))
		avg = 0    
		a = []
		
	except IOError:
		#print i
		f = f - 1
		continue
	
print f		
#print len(a), npnts
#print 100-f, "<- Number of missing Ampar files"

    
#c = []
    #for j in range(0,f):
	#for i in range(stpt,npnts):
    #avg = avg + a[i + j*npnts]/mul
	#c.append(avg)
	#ofile_ampseed.write("{} {}\n".format(avg, j))
#avg = 0.0

ofile_ampseed.close()

count = 0
#plt.plot(c)
#filename2 = path2 + "/" +  str(Kin) + "_" + str(ca_peak) + "_" + str(pp2a_input) + "_" + str(no_input) + "final_ampar_averaged.png"
#savefig(filename2)
#close()
#f2 = open(path2 + "/" +  str(Kin) + "_" + str(ca_peak) + "_" + str(pp2a_input) + "_" + str(no_input) + "final_ampar_averaged.txt","w")
#np.savetxt(f2,c)
#f2.close()

#print len(c), n

j = 0
for j in range(0,100):
	for i in range(0,f):
		if ((avg1[i]>=(40+(j*1))) and (avg1[i]<(40+(j*1)+5))): count = count + 1
	d.append(count)	 
	j = j + 20
	count = 0


fig = plt.figure()
ax = fig.add_subplot(111)
x = np.arange(40, 140, 1)
ax.plot(x, d)
filename1 = path2 + "/"  + str(Kin) + "_" + str(ca_peak) + "_" + str(pp2a_input) + "_" + str(no_input) + "final_ampar_distribution.png"
savefig(filename1)
close()
#f3 = open(path2 + "/" +  str(Kin) + "_" + str(ca_peak) + "_" + str(pp2a_input) + "_" + str(no_input) + "final_ampar_distribution.txt","w")
#np.savetxt(f3,c)
#f3.close()
