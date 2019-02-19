import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0.01,1,0.01)
y=-x*np.log2(x)-(1-x)*np.log2(1-x)

#fig=plt.figure()
#ax=fig.add_subplot(111)
#ax.scatter(x,y)
plt.plot(x,y)
plt.show()
