#Base Python client for MEng in IoT Assignment
#consumes data from IoT Gateway
import urllib2
import numpy as np

import matplotlib.pyplot as plt
#evenly spaced time at 3ms intervals
#t=np.arange(0.,30,3.)
#red dashes, blue squares, green triangles
#plt.plot(t,t,'r--',t,t**2,'g^')

t=np.arange(0.,30,3.)
#red dashes, blue squares, green triangles
plt.title ('Graph of Temperature versus Time(s)')
plt.ylabel('Temperature (degree)')
plt.xlabel('Time (s)')
response = urllib2.urlopen('http://localhost:8080/')

resp = response.read()
#resp=[]
#for i in range (0,10):
#	resp.append(i)		****************************************
#	print resp[i]		It's printing a graph layout but can't get data onto it :(
#plt.plot(t,resp[i],'g^')
plt.show()


print resp